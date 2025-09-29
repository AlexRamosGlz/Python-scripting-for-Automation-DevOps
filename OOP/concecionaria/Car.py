
class Car:
    color: str
    brand: str
    model: str
    is_available: bool = True

    def __init__(self, color: str, brand: str, model: str):
        self.brand = brand
        self.color = color
        self.model = model

    def get_model(self) -> str:
        return self.model

    def get_brand(self) -> str:
        return self.brand

    def get_color(self) -> str:
        return self.color
    
    def get_is_available(self) -> str:
        return self.is_available

    def set_is_available(self) -> None:
        self.is_available = not self.is_available

