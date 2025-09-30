from Vehiculo import Vehicle

class Bicicle(Vehicle):
    
    def start_enginge(self) -> None:
        if not self.is_available:
            return f"La bicicleta con modelo {self.model} no esta disponible"
        
        return f"La bicicleta esta en marcha"
    
    def stop_enginge(self) -> None:
        if not self.is_available:
            return f"La bicicleta con modelo {self.model} no esta disponible"
        
        return f"La bicicleta se ha parado"