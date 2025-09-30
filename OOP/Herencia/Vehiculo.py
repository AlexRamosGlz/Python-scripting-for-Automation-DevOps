class Vehicle:
    
    def __init__(self, brand: str, model: str, price: float):
        self.brand =  brand
        self.model = model
        self.price = price
        self.is_available = True
        
        
    def sell(self):
        if(self.is_available == False):
            print(f"El Vehiculo {self.model} no esta disponible")
            return 
        
        self.is_available = False
        print(f"El Vehiculo {self.model} ha sido vendido")
        
    def get_price(self):
        return self.price
            
    def get_is_available(self):
        return self.is_available