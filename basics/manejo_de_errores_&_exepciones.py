from dataclasses import dataclass, field
import json

@dataclass
class ErrorDto:

    error: Exception
    message: str
    
    def __post_init__(self):
        print(json.dumps({
            "error": str(self.error),
            "message": self.message
        }, ensure_ascii=False))
        
try:
    divisor = int(input("Ingrese el divisor: "))
    result = 100/divisor
    print(result)
except ZeroDivisionError as error:
    erro = ErrorDto(error, "No puedes dividr entre 0")
except ValueError as error:
    error = ErrorDto(error, "El divison no puede ser un string")

