import random
from LogicaBase import LogicaBase

class LogicaProgramacion(LogicaBase):
    def __init__(self, interfaz):
        super().__init__(interfaz)
        self.intentos = 4  # Menos intentoss
        self.vidas = self.intentos
        self.tema = "Programacion"
        self.palabras = ["javascript", "python", "java", "ruby", "php", "swift", "kotlin"]

    def elegir_palabra(self):
        return random.choice(self.palabras)