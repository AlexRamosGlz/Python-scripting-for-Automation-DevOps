from Vehiculo import Vehicle

class Customer:
    
    """Clase que representa a un cliente, 'name' es un string y
    'purchased_vehicles' es una lista de Vehicles"""
    
    name: str
    purchased_vehicles: list = []
    
    def __init__(self, name: str):
        self.name = name
        
    def buy_vehicle(self, vehicle: Vehicle) -> None:
        if not vehicle.is_available:
            print(f"El Vehiculo {vehicle.model} no esta disponible, es imposible comprar")
            return
        
        vehicle.sell()
        self.purchased_vehicles.append(vehicle)
        print(f"Haz comprado el vehiculo {vehicle.model} por {vehicle.price} pesos")
        
    def inquire_vehicle(self, vehicle: Vehicle) -> None:
        availability = "disponible" if vehicle.is_available else "no disponible"
        print(f"El vehiculo {vehicle.model} esta {availability} y cuesta {vehicle.price} pesos")
        