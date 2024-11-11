import random

class LogicaBase:
    def __init__(self, interfaz):
        self.interfaz = interfaz
        self.intentos = 6
        self.palabra_secreta = ""
        self.palabra_visualizada = []
        self.vidas = self.intentos
        self.tema = "Base" 
        self.palabras = []  

    def elegir_palabra(self):
        return random.choice(self.palabras)

    def iniciar_juego(self):
        self.vidas = self.intentos
        self.palabra_secreta = self.elegir_palabra()
        self.palabra_visualizada = ["_"] * len(self.palabra_secreta)
        self.interfaz.actualizar_interfaz(self.palabra_visualizada, self.vidas)

    def adivinar_letra(self, letra):
        if letra and letra not in self.palabra_visualizada:
            if letra in self.palabra_secreta:
                for i, l in enumerate(self.palabra_secreta):
                    if l == letra:
                        self.palabra_visualizada[i] = letra
            else:
                self.vidas -= 1
            
            self.interfaz.actualizar_interfaz(self.palabra_visualizada, self.vidas)

        if "_" not in self.palabra_visualizada:
            return "ganaste"
        elif self.vidas <= 0:
            return "perdiste"
        return "continua"