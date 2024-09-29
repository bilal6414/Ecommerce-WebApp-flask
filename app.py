from flask import Flask, render_template, request, redirect, url_for
import main as crud
from flask_cors import CORS
app = Flask("My App")
CORS(app)

@app.get("/")
def home():
    return render_template('index.html')

@app.get("/products")
def web_get_products():
    return crud.show_data().to_json(orient='records')

@app.get("/products/<product_id>")
def web_get_product(product_id):
    return crud.get_product(product_id).to_json(orient='records')
@app.post("/products")
def web_add_product():
    product=request.get_json()
    print(product)
    crud.add_product(product['pid'],
                     product['name'],
                     product['description'],
                     product['price'],
                     product['rating'])

    return "Products added"
@app.patch("/products")
def web_update_rating():
    product=request.get_json()
    crud.update_product(product['pid'],product['rating'])
    return "Update the product"
@app.delete("/products")
def web_delete_rating():
    product=request.get_json()
    crud.delete_product(product['pid'])
    return "Deleted succesfully"
if __name__ == '__main__':
    app.run(debug=True)
