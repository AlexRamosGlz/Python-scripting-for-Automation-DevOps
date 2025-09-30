from Car import Car
from Truck import Truck
from Bicicle import Bicicle
from Dealership import Dealership
from Custumer import Customer

def main():
    dealership = Dealership()
    
    car_1 = Car("Toyota Corolla", 20000, True)
    car_2 = Car("Honda Civic", 22000, False)
    
    truck_1 = Truck("Ford F-150", 30000, True)
    truck_2 = Truck("Chevrolet Silverado", 35000, True)
    
    bicicle_1 = Bicicle("Giant Escape 3", 500, True)
    bicicle_2 = Bicicle("Trek FX 1", 600, False)
    
    dealership.add_vehicles(car_1)
    dealership.add_vehicles(car_2)
    dealership.add_vehicles(truck_1)
    dealership.add_vehicles(truck_2)
    dealership.add_vehicles(bicicle_1)
    dealership.add_vehicles(bicicle_2)
    
    customer_1 = Customer("Alice")
    customer_2 = Customer("Bob")
    
    dealership.register_customer(customer_1)
    dealership.register_customer(customer_2)
    
    print("\nVehiculos disponibles en el concesionario:")
    dealership.show_available_vehicles()
    
    print("\nAlice consulta sobre el Honda Civic:")
    customer_1.inquire_vehicle(car_2)
    
    print("\nAlice intenta comprar el Honda Civic:")
    customer_1.buy_vehicle(car_2)
    
main()