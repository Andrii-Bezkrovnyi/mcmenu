document.addEventListener("DOMContentLoaded", function() {
    const path = window.location.pathname;
    if (path.includes("index.html") || path === "/") {
        fetchAllProducts();
    } else if (path.includes("product.html")) {
        const urlParams = new URLSearchParams(window.location.search);
        const productName = urlParams.get('name');
        fetchProductByName(productName);
    }

    const fieldForm = document.getElementById("fieldForm");
    if (fieldForm) {
        fieldForm.addEventListener("submit", function(event) {
            event.preventDefault();
            const urlParams = new URLSearchParams(window.location.search);
            const productName = urlParams.get('name');
            const fieldName = document.getElementById("fieldInput").value;
            fetchProductField(productName, fieldName);
        });
    }
});

async function fetchAllProducts() {
    try {
        const response = await fetch('http://localhost:8000/all_products');
        const data = await response.json();
        displayProducts(data);
    } catch (error) {
        displayError("Error fetching products.");
        console.error("Error fetching products:", error);
    }
}

function displayProducts(products) {
    const productsContainer = document.getElementById("products");
    productsContainer.innerHTML = '';
    products.forEach(product => {
        const productItem = document.createElement("div");
        productItem.className = "product-item";
        productItem.innerHTML = `
            <h3>${product.name}</h3>
            <a href="product.html?name=${product.name}">View Details</a>
        `;
        productsContainer.appendChild(productItem);
    });
}

async function fetchProductByName(name) {
    try {
        const response = await fetch(`http://localhost:8000/products/${name}`);
        const product = await response.json();
        displayProductDetails(product);
    } catch (error) {
        displayError("Error fetching product details.");
        console.error("Error fetching product:", error);
    }
}

function displayProductDetails(product) {
    const productContainer = document.getElementById("product");
    productContainer.innerHTML = '';
    const productDetail = document.createElement("div");
    productDetail.className = "product-detail";
    productDetail.innerHTML = `
        <h3>${product.name}</h3>
        <p>${product.desc}</p>
        <p><a href="#" class="clickable" data-field="calories">Калории: ${product.calories}</span></p>
        <p><a href="#" class="clickable" data-field="fat">Жиры: ${product.fat}</span></p>
        <p><a href="#" class="clickable" data-field="carbs">Углеводы: ${product.carbs}</span></p>
        <p><a href="#" class="clickable" data-field="protein">Белки: ${product.protein}</span></p>
        <p><a href="#" class="clickable" data-field="saturated_fat">Насыщенные жиры: ${product.saturated_fat}</span></p>
        <p><a href="#" class="clickable" data-field="sugar">Сахар: ${product.sugar}</span></p>
        <p><a href="#" class="clickable" data-field="salt">Соль: ${product.salt}</span></p>
        <p><a href="#" class="clickable" data-field="portion">Порция: ${product.portion}</span></p>
    `;
    productContainer.appendChild(productDetail);

    // Add event listeners to clickable fields
    document.querySelectorAll('.clickable').forEach(element => {
        element.addEventListener('click', function() {
            displayFieldResult({
                [this.dataset.field]: product[this.dataset.field]
            });
        });
    });
}

async function fetchProductField(name, field) {
    try {
        const response = await fetch(`http://localhost:8000/products/${name}/${field}`);
        if (response.ok) {
            const data = await response.json();
            displayFieldResult(data);
        } else {
            const error = await response.json();
            displayFieldResult({ error: error.detail });
        }
    } catch (error) {
        console.error("Error fetching product field:", error);
        displayFieldResult({ error: "An error occurred while fetching the field." });
    }
}

function displayFieldResult(result) {
    const fieldResultContainer = document.getElementById("fieldResult");
    fieldResultContainer.innerHTML = '';
    if (result.error) {
        fieldResultContainer.innerHTML = `<p>Error: ${result.error}</p>`;
    } else {
        const field = Object.keys(result)[0];
        const value = result[field];
        fieldResultContainer.innerHTML = `<p>${field}: ${value}</p>`;
    }
}

function displayError(message) {
    const errorContainer = document.getElementById("error");
    errorContainer.innerHTML = `<p>${message}</p>`;
}
