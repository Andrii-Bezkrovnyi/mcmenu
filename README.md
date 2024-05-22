# FastAPI Menu Endpoint

This Python code provides an API using FastAPI for retrieving information about products stored in a `menu.json` file.

## Description

The script utilizes Selenium to scrape the McDonald's menu from the website [mcdonalds.com](https://www.mcdonalds.com/ua/uk-ua/eat/fullmenu.html). It collects information such as product name, description, calories, fat, carbohydrates, protein, saturated fat, sugar, salt, and portion size for each item on the menu.

The code consists of three main endpoints:

1. `/all_products`: Retrieves information about all products stored in the `menu.json` file.
2. `/products/{product_name}`: Retrieves information about a specific product by its name.
3. `/products/{product_name}/{product_field}`: Retrieves information about a specific field of a specific product.

## Requirements

- Python 3.x
- Selenium
- tqdm
- fastapi
- uvicorn

## How to Use

1. Clone this repository to your local machine.

    ```bash
    git clone https://github.com/Andrii-Bezkrovnyi/mcmenu.git
    ```

2. Navigate to the project directory:

    ```bash
    cd mcmenu
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the parser script:

    ```bash
    python mcmenu_parser.py
    ```

5. Install live-server:

    ```bash
    npm install live-server
    ```

6. Run the server using `python main.py`.

7. Run live-server using `live-server --port=5500`.

8. Access the endpoints using your browser or an API client (e.g., Postman).

9. Open the site with products using url `http://127.0.0.1:5500/index.html`

### Endpoints

#### Get All Products
- **URL:** `/all_products`  - Returns information about all products.
#### Get Product by Name
- **URL:** `/products/{product_name}` - Returns information about a specific product by its name.
**Parameters:**
  - `product_name`: The name of the product.

#### Get Product Field
- **URL:** `/products/{product_name}/{product_field}`  -  Returns information about a specific field of a specific product.
- **Parameters:**
  - `product_name`: The name of the product.
  - `product_field`: The field to retrieve information about.

## Data Format

The data is stored in JSON format in the `menu.json` file. Each product is represented as an object with various fields such as name, description, calories, fat, carbs, etc.

## Example

#### json


```bash
{
    "name": "Спрайт® середній",
    "desc": "Всесвітньо відомий освіжаючий напій.",
    "calories": "110ккал",
    "fat": "0.0г",
    "carbs": "27г",
    "protein": "0.0г",
    "saturated_fat": "0.0г",
    "sugar": "27г",
    "salt": "0.0г",
    "portion": "400мл"
}
```