import csv

# Leer un archivo CSV
with open("products.csv", "r") as file:
    csv_reader = csv.reader(file)
    
        # csv.reader(file)...
        #
        #  Este objeto reader itera sobre lineas en el archivo CSV
        #  y las convierte en listas
        #
        #  ['Microphone', '110', '18', 'VoiceClear', 'Audio', '2024-05-10']
    
    for line in csv_reader:
        print(line)
        
        
with open("products.csv", "r") as file:
    csv_dict_reader = csv.DictReader(file)
    
        # csv.DictReader(file)...
        #   
        #  Es otro objeto reader, pero mapea cada file como un diccionario
        #
        #  {'name': 'Microphone', 'price': '110', 'quantity': '18', 'brand': 'VoiceClear', 'category': 'Audio', 'entry_date': '2024-05-10'}
    
    # Imprimir columas especificas
    for row in csv_dict_reader:
        print(f"Producto: {row['name']}, Precio: {row['price']}")
        
        

# Escribir o append en una archivo csv

new_product: dict = {'name': 'tu cola', 'price': '200', 'quantity': '12', 'brand': 'tu mama', 'category': 'gefas', 'entry_date': '2024-05-10'}

with open('products.csv', mode="a", newline=None) as file:
    
    csv_writter = csv.DictWriter(file, fieldnames=new_product.keys())
    csv_writter.writerow(new_product)
    
    
# # Agregar una nueva columna 

try:
    open("updated_products.csv", 'x')
except FileExistsError as error:
    print(error)

with open("products.csv", mode="r") as file:
    csv_reader = csv.DictReader(file)
    
    # Obtener el nombre de las columnas de un csv
    column_names = csv_reader.fieldnames + ['total_value']
    
    with open("updated_products.csv", mode="w", newline=None) as new_fle:
        
        csv_writter = csv.DictWriter(new_fle, fieldnames=column_names)
        csv_writter.writeheader();
        
        for row in csv_reader:
            row['total_value'] = float(row['price']) * int(row['quantity'])
            csv_writter.writerow(row)