from Vehiculo import Vehicle

class Car(Vehicle):
    
    def start_enginge(self) -> None:
        if not self.is_available:
            return f"El coche con modelo {self.model} no esta disponible"
        
        return f"El motor esta en marcha"
    
    def stop_enginge(self) -> None:
        if not self.is_available:
            return f"El coche con modelo {self.model} no esta disponible"
        
        return f"El motor se ha parado"



    

