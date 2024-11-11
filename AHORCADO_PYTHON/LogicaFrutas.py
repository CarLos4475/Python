import random
from LogicaBase import LogicaBase

class LogicaFrutas(LogicaBase):
    def __init__(self, interfaz):
        super().__init__(interfaz)
        self.tema = "Frutas"
        self.palabras = ["manzana", "banana", "platano", "uva", "naranja", "sandia", "melon", "fresa"]

    def elegir_palabra(self):
        return random.choice(self.palabras)