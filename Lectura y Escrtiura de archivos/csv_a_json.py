import csv
import json
import re

# Convertir de JSON a CSV
def convert_to_csv():
    
    file_path: str = input("Introdusca el path al archivo:\n")

    
    if not re.search(r".json$", file_path):
        return print("La extension es incorrecta, .json esperado")
    
    try:
        with open(file_path, "r") as file:
            products: list = json.load(file)
    except FileNotFoundError as error:
        return print(f"Erro al abrir el archivo: {error}")
        
    field_names = products[0].keys()
    print(field_names)
        
    with open(file_path.replace(".json", "_new.csv"), mode="w", newline=None) as file:
        csv_writer = csv.DictWriter(file, fieldnames=field_names)
        csv_writer.writeheader()
        
        for product in products:
            csv_writer.writerow(product)
        
        
# Convertir de CSV a JSON
def convert_to_json():
    
    json_products: list = []
    
    file_path: str = input("Introdusca el path al archivo:\n")
    
    if not re.search(r".csv$", file_path):
        return print("La extension es incorrecta, .csv esperado")
    
    
    try:
        with open(file_path, mode="r") as file:
            csv_products = csv.DictReader(file)
            
            for prduct in csv_products:
                json_products.append(prduct)
                    
    except FileNotFoundError as error:
        return print(f"Erro al abrir el archivo: {error}")
    
    with open(file_path.replace(".csv", "_converted.json"), "w") as file:
        json.dump(json_products, file, indent=4)


def main():
    mode = input("""
     Escriba el modo:
        1.- JSON a CSV
        2.- CSV a JSON\n""")
    
    if int(mode) == 1:
        convert_to_csv()
    else:
        convert_to_json()
        

main()