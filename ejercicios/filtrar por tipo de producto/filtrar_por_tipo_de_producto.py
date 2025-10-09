#!/usr/bin/env python3

import os
import csv

FILE_PATH =  f"{os.getcwd()}/CODIGOS.csv"

single_products: list = []



def get_base_sku(sub_sku: str):

    tallas: list = ["4xl", "3xl", "2xl", "xl", "xs", "s", "m", "l"]
    
    for talla in tallas:
        if sub_sku.endswith(talla.upper()):
            sub_sku = sub_sku[:- len(talla)]
            break
    
    return sub_sku[:-3];

try:
    with open(FILE_PATH, 'r') as file:
        
        csv_reader: list = csv.DictReader(file)
        
        for line in csv_reader:
            sku: str = get_base_sku(line['sku actual'])
            
            single_products.append({"sku": sku, "tipo": line['']})
            
except Exception as error:
    print(f"Algo salio mal: {error}")      

single_products = list(filter(lambda product: product['tipo'] == "BAJO PEDIDO", single_products))

filtered_skus: list = []

for product in single_products:
    if(product not in filtered_skus):
        filtered_skus.append(product)
    else:
        pass
    
for product in filtered_skus:
    print(product['sku'])


                  



    
     
        