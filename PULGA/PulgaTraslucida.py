import random
from Pulga import Pulga

class PulgaTraslucida(Pulga):
    def __init__(self, ancho_panel, alto_panel, canvas):
        super().__init__(ancho_panel, alto_panel)
        self.visible = True
        self.canvas = canvas
        self.timer = self.canvas.after(500, self.toggle_visibility)
    
    def toggle_visibility(self):
        self.visible = not self.visible  # Alterna entre True y False
        self.timer = self.canvas.after(500, self.toggle_visibility)  # Programa siguiente cambio
    
    def paint(self, canvas):
        if self.visible:
            super().paint(canvas)
    
    def click(self):
        self.visible = False
        self.canvas.after_cancel(self.timer)  # Cancelar el temporizador para detener el parpadeo
        super().click()