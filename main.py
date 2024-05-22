import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json

# Load data from menu.json
with open("menu.json", "r", encoding="utf-8") as file:
    menu_data = json.load(file)

app = FastAPI()

# Configure CORS
origins = [
    "http://localhost:5500",
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/all_products")
async def get_all_products():
    return menu_data


@app.get("/products/{product_name}")
async def get_product_by_name(product_name: str):
    for product in menu_data:
        if product["name"] == product_name:
            return product
    raise HTTPException(status_code=404, detail="Product not found")


@app.get("/products/{product_name}/{product_field}")
async def get_product_field(product_name: str, product_field: str):
    for product in menu_data:
        if product["name"] == product_name:
            if product_field in product:
                return {product_field: product[product_field]}
            else:
                raise HTTPException(status_code=404, detail="Field not found")
    raise HTTPException(status_code=404, detail="Product not found")

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
