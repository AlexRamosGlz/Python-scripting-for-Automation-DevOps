import json
import os


FILE_PATH = f"{os.getcwd()}/products.json" 

# Leer un archivo .json
with open(FILE_PATH, mode="r") as file:
    products: list = json.load(file)

        # la funcion json.load(...) se usa para leer un archivo tipo JSON y convertirlo
        # a un objeto tipo Python, tipicamente un dictionary o una lista.
        
for product in products:
    print(f"Producto: {product['name']}, Precio: {product['price']}")
    



# Escribir a un archivo .json

new_product: dir =   {
        "name": "stich aplaca colicos",
        "price": 75,
        "quantity": 10,
        "brand": "temu",
        "category": "Aplacacolicos",
        "entry_date": "2024-07-01"
    }

with open(FILE_PATH, mode="r") as file:
    new_products: list = json.load(file)
    
new_products.append(new_product)

with open("new_products.json", mode="w") as file:
    json.dump(new_products, file, indent=4)
    
        # La funcion json.dump(obj, fp, indent) convierte de un objeto Python a json
        # y ademas escribe directamente a un archivo la nueva data convertida.
        #
        #   obj ->  Es el objeto python a convertir
        #   fp  ->  Es el archivo al que se escribira la data (file-like object) con el modo escritura
        #   indent ->   Se refiere al nivel de identacion
