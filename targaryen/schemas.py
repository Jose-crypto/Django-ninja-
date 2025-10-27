## Se creo este esquema para realizar aqui la serializacion, mantiene el codigo mas limpio
# Si se intenta poonerlo dentro del archivo de modelo puede hacer referencia a lso modelos y puede generar problemas de dependencia cilcila

from ninja import Schema

class DragonOut(Schema):
    name: str
    birth_year: int