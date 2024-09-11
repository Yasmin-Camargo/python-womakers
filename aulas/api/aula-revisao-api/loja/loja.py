from flask import Flask, request

app = Flask(__name__)


# db memoria
products = [
    {
        "code": 1,
        "name": 'Smartphone',
        "price": 990.90,
    },
    {
        "code": 2,
        "name": 'Ventilador',
        "price": 70.90,
    },
]

@app.route("/")
def hello():
    return "Hello, World!"

# List all products
@app.route("/products", methods=['GET'])
def list_products():
    return products,200


# Create product
@app.route("/products", methods=['POST'])
def create_products():
    new_product = request.get_json()
    products.append(new_product)

    return {"message": "Product created",
            "product": new_product}, 201

# Get product
@app.route("/products/<int:code>", methods=['GET'])
def get_products(code):
    product_result = None

    for product in products:
        if product["code"] == code:
            product_result = product
            break

    if not product_result:
        return {"error": "Product not found"}, 404

    return {"product": code}, 200

# delete product
@app.route("/products/<int:code>", methods=['DELETE'])
def delete_products(code):
    product_result = None

    for product in products:
        if product["code"] == code:
            product_result = product
            break

    if not product_result:
        return {"error": "Product not found"}, 404

    products.remove(product_result)

    return {"deleted"}, 200

