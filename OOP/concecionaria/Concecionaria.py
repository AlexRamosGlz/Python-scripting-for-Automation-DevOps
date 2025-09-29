from Car import Car
from FIlterDto import FilterDto


class Concecionaria:
    # list<Car>
    cars: list

    def __init__(self, cars: list):
        self.cars = cars

    def get_cars(self) -> list:
        return self.cars

    def get_cars_by_filter(self, filter) -> list:
        filtered_cars: list = []

        for car in self.get_cars():
            if(car.get_is_available is False):
                continue
            
            if filter.key == "model":
                if car.get_model() == filter.value:
                    filtered_cars.append(car)
                    break

            if filter.key == "brand":
                if car.get_brand() == filter.value:
                    filtered_cars.append(car)

            if filter.key == "color":
                if car.get_color() == filter.value:
                    filtered_cars.append(car)

        return filtered_cars
    
    def sell_car(self, model: str):
    
        car_to_sell = self.get_cars_by_filter(FilterDto("model", model))
        
        if(car_to_sell[0].get_is_available() is False):
            print("El coche no esta disponible")
            return
        
        car_to_sell[0].set_is_available()
        print(f"El coche {model} ha sido vendido")


cars: list = []
          
cars.append(Car("Negr", "Honda", "Civic 2023"))
cars.append(Car("Blanco", "Toyota", "Corolla 2024"))
cars.append(Car("Rojo", "Mazda", "CX-5 2022"))
cars.append(Car("Azul", "Nissan", "Sentra 2021"))
cars.append(Car("Gris", "Ford", "Focus 2020"))
cars.append(Car("Verde", "Chevrolet", "Cruze 2023"))
cars.append(Car("Amarillo", "Kia", "Rio 2024"))
cars.append(Car("Plateado", "Hyundai", "Tucson 2022"))
cars.append(Car("Naranja", "Volkswagen", "Jetta 2023"))
cars.append(Car("Dorado", "BMW", "Serie 3 2024"))

cars.append(Car("Negro", "Audi", "A4 2022"))
cars.append(Car("Blanco", "Mercedes-Benz", "Clase C 2023"))
cars.append(Car("Rojo", "Tesla", "Model 3 2024"))
cars.append(Car("Azul", "Honda", "HR-V 2021"))
cars.append(Car("Gris", "Toyota", "Yaris 2020"))
cars.append(Car("Verde", "Mazda", "Mazda 3 2023"))
cars.append(Car("Amarillo", "Nissan", "Versa 2022"))
cars.append(Car("Plateado", "Ford", "Escape 2024"))
cars.append(Car("Naranja", "Chevrolet", "Tracker 2021"))
cars.append(Car("Dorado", "Kia", "Sportage 2023"))

cars.append(Car("Negro", "Hyundai", "Elantra 2022"))
cars.append(Car("Blanco", "Volkswagen", "Golf 2024"))
cars.append(Car("Rojo", "BMW", "X1 2023"))
cars.append(Car("Azul", "Audi", "Q3 2021"))
cars.append(Car("Gris", "Mercedes-Benz", "GLA 2020"))
cars.append(Car("Verde", "Tesla", "Model Y 2023"))
cars.append(Car("Amarillo", "Honda", "CR-V 2024"))
cars.append(Car("Plateado", "Toyota", "RAV4 2022"))
cars.append(Car("Naranja", "Mazda", "CX-30 2021"))
cars.append(Car("Dorado", "Nissan", "Kicks 2023"))

cars.append(Car("Negro", "Ford", "Explorer 2024"))
cars.append(Car("Blanco", "Chevrolet", "Trax 2023"))
cars.append(Car("Rojo", "Kia", "Seltos 2022"))
cars.append(Car("Azul", "Hyundai", "Santa Fe 2021"))
cars.append(Car("Gris", "Volkswagen", "Tiguan 2020"))
cars.append(Car("Verde", "BMW", "X3 2024"))
cars.append(Car("Amarillo", "Audi", "A3 2023"))
cars.append(Car("Plateado", "Mercedes-Benz", "Clase A 2022"))
cars.append(Car("Naranja", "Tesla", "Model S 2021"))
cars.append(Car("Dorado", "Honda", "Accord 2020"))

cars.append(Car("Negro", "Toyota", "Camry 2023"))
cars.append(Car("Blanco", "Mazda", "MX-5 2024"))
cars.append(Car("Rojo", "Nissan", "Altima 2022"))
cars.append(Car("Azul", "Ford", "Mustang 2021"))
cars.append(Car("Gris", "Chevrolet", "Malibu 2020"))
cars.append(Car("Verde", "Kia", "Forte 2023"))
cars.append(Car("Amarillo", "Hyundai", "Sonata 2024"))
cars.append(Car("Plateado", "Volkswagen", "Passat 2022"))
cars.append(Car("Naranja", "BMW", "Serie 5 2021"))
cars.append(Car("Dorado", "Audi", "A6 2020")) 
cars.append(Car("Negr", "Honda", "Civic 2023"))
cars.append(Car("Blanco", "Toyota", "Corolla 2024"))
cars.append(Car("Rojo", "Mazda", "CX-5 2022"))

concecionaria = Concecionaria(cars)

for index in range(2):
    concecionaria.sell_car("Civic 2023")