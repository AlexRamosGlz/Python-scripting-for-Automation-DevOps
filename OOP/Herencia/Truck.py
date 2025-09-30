from Vehiculo import Vehicle

class Truck(Vehicle):
    
    def start_enginge(self) -> None:
        if not self.is_available:
            return f"El camion con modelo {self.model} no esta disponible"
        
        return f"El camion esta en marcha"
    
    def stop_enginge(self) -> None:
        if not self.is_available:
            return f"El camion con modelo {self.model} no esta disponible"
        
        return f"El camion se ha parado"