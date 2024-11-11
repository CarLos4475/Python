import random
import tkinter as tk
from PIL import Image, ImageTk
import os

class Pulga:
    def __init__(self, ancho_panel, alto_panel):
        self.x = random.randint(0, ancho_panel - 100)
        self.y = random.randint(0, alto_panel - 100)
        self.ancho_panel = ancho_panel
        self.alto_panel = alto_panel
        self.pulga = None
        self.visible = True
        
        self.cargar_imagen()
        
    def cargar_imagen(self):
        ruta_pulga = os.path.join(os.path.dirname(__file__), "PULGUITA.png")
        imagen_pulga = Image.open(ruta_pulga)
        imagen_pulga = imagen_pulga.resize((90, 90))
        self.pulga = ImageTk.PhotoImage(imagen_pulga)
        
    def mover_aleatoriamente(self):
        if self.visible:
            deltaX = random.randint(-20, 20)
            deltaY = random.randint(-20, 20)
            self.mover(deltaX, deltaY)
        
    def mover(self, deltaX, deltaY):
        self.x = max(0, min(self.ancho_panel - self.pulga.width(), self.x + deltaX))
        self.y = max(0, min(self.alto_panel - self.pulga.height(), self.y + deltaY))
        
    def paint(self, canvas):
        if self.visible:
            canvas.create_image(self.x, self.y, image=self.pulga, anchor=tk.NW)
        
    def click(self):
        self.visible = False

    def is_visible(self):
        return self.visible
