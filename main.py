import uvicorn
from fastapi import FastAPI, HTTPException
import json

# Load data from menu.json
with open("menu.json", "r", encoding="utf-8") as file:
    menu_data = json.load(file)

app = FastAPI()

@app.get("/all_products")
async def get_all_products():
    """
    Endpoint to get information about all products.

    Returns:
        dict: All products data.
    """
    return menu_data

@app.get("/products/{product_name}")
async def get_product_by_name(product_name: str):
    """
    Endpoint to get information about a specific product by its name.

    Args:
        product_name (str): The name of the product.

    Returns:
        dict: Information about the product.

    Raises:
        HTTPException: If the product is not found.
    """
    for product in menu_data:
        if product["name"] == product_name:
            return product
    raise HTTPException(status_code=404, detail="Product not found")

@app.get("/products/{product_name}/{product_field}")
async def get_product_field(product_name: str, product_field: str):
    """
    Endpoint to get information about a specific field of a specific product.

    Args:
        product_name (str): The name of the product.
        product_field (str): The field to retrieve information about.

    Returns:
        dict: Information about the specified field of the product.

    Raises:
        HTTPException: If the product or field is not found.
    """
    for product in menu_data:
        if product["name"] == product_name:
            if product_field in product:
                return {product_field: product[product_field]}
            else:
                raise HTTPException(status_code=404, detail="Field not found")
    raise HTTPException(status_code=404, detail="Product not found")


if __name__ == "__main__":
    uvicorn.run(app, port=8000)