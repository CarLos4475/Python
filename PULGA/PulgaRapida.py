import random
from Pulga import Pulga

class PulgaRapida(Pulga):
    def __init__(self, ancho_panel, alto_panel):
        super().__init__(ancho_panel, alto_panel)
    
    def mover_aleatoriamente(self):
        if self.visible:
            deltaX = random.randint(-150, 150)
            deltaY = random.randint(-150, 150)
            self.mover(deltaX, deltaY)
            
