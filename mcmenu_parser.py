from selenium import webdriver
from selenium.webdriver.common.by import By
import json
from tqdm import tqdm



BASE_URL = "https://www.mcdonalds.com/ua/uk-ua/eat/fullmenu.html"

class McDonaldsMenuParser:
    """Class to parse McDonald's menu from the website."""

    def __init__(self):
        """Initialize Chrome webdriver and its options."""
        self.options = webdriver.ChromeOptions()  # Options for Chrome webdriver.
        self.options.add_argument('--headless=new')  # Setting Chrome to headless mode.
        self.driver = webdriver.Chrome(options=self.options)  # Initializing Chrome webdriver.


    def get_product(self, url):
        """Get details of a product from its URL.
        
        Args:
            url (str): The URL of the product.
        
        Returns:
            dict: Details of the product.
        """
        self.driver.get(url)
        self.driver.implicitly_wait(0.5)
        name = self.driver.find_element(By.CLASS_NAME, 'cmp-product-details-main__heading').text
        desc = self.driver.find_element(By.CLASS_NAME, 'cmp-product-details-main__description').text

        try:
            energy_data = [item.get_attribute('innerText').strip().split()[0]
                          for item in self.driver.find_elements(By.CLASS_NAME, 'cmp-nutrition-summary__heading-primary-item')]
            calories, fat, carbs, protein = energy_data[:4]

            ingredients = (self.driver.find_element(By.CLASS_NAME, 'cmp-nutrition-summary__details-column-view-desktop')
                          .find_elements(By.CSS_SELECTOR, 'li > span.value > span.sr-only'))
            ingredients_data = [item.get_attribute('innerText').strip().split()[0] for item in ingredients]
            saturated_fat, sugar, salt, portion = ingredients_data[:4]

            product = {'name': name, 
                       'desc': desc, 
                       'calories': calories, 
                       'fat': fat, 
                       'carbs': carbs, 
                       'protein': protein,
                       'saturated_fat': saturated_fat,
                        'sugar': sugar, 
                        'salt': salt, 
                        'portion': portion}
            return product

        except Exception as err:
            print(f'Error is {name}. Info: {err}')
            return None

    def get_menu(self, menu_url):
        """Get the entire menu from the provided menu URL.
        
        Args:
            menu_url (str): The URL of the menu.
        
        Returns:
            list: List of dictionaries containing details of all products in the menu.
        """
        self.driver.get(menu_url)
        product_links = [item.get_attribute('href') for item in self.driver.find_elements(By.CLASS_NAME, 'cmp-category__item-link')]
        products = [self.get_product(link) for link in tqdm(product_links, desc="Parsing Menu") if self.get_product(link)]
        return products

    def quit_driver(self):
        """Quit the Chrome webdriver."""
        self.driver.quit()

if __name__ == "__main__":
    parser = McDonaldsMenuParser()
    products = parser.get_menu(BASE_URL)
    parser.quit_driver()

    with open('menu.json', 'w') as file:
        json.dump(products, file, ensure_ascii=False, indent=4)
