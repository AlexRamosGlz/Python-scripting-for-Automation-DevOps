
count: int = 0
with open("cuento.txt", "r") as file:
    for line in file:
        count += 1
    
print(f"El archivo tiene {count} lineas")