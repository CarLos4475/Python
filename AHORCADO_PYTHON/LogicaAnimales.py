from LogicaBase import LogicaBase
import random

class LogicaAnimales(LogicaBase):
    def __init__(self, interfaz):
        super().__init__(interfaz)
        self.tema = "Animales"
        self.palabras = ["perro", "gato", "leon", "tigre", "elefante", "jirafa", "mono", "cebra"]

    def elegir_palabra(self):
        return random.choice(self.palabras)