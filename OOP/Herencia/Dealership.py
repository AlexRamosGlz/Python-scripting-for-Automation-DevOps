from Vehiculo import Vehicle
from Custumer import Customer

class Dealership:
    customers: list
    vehicles: list
    
    def __init__(self):
        self.customers = []
        self.vehicles = []
        
    def add_vehicles(self, vehicle: Vehicle) -> None:
        self.vehicles.append(vehicle)
        print(f"El vehiculo {vehicle.model} se ha añadido al inventario.")
        
    def register_customer(self, customer: Customer) -> None:
        self.customers.append(customer)
        print(f"El Cliente {customer.name} se ha registrado")
    
    def show_available_vehicles(self) -> None:
        for vehicle in self.vehicles:
            if vehicle.is_available:
                print(f" -  {vehicle.model} por {vehicle.price} pesos - ")
                
                
