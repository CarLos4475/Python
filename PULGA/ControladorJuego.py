import tkinter as tk
from tkinter import messagebox
from Pulga import Pulga
from PulgaLenta import PulgaLenta
from PulgaRapida import PulgaRapida
from PulgaTraslucida import PulgaTraslucida
from Vista import Vista

class ControladorJuego:
    def __init__(self):
        self.pulgas = []
        self.vista = Vista(self)
        self.timer = None
        
    def iniciar_juego(self):
        self.vista.ventana_bienvenida.destroy()
        self.vista.crear_ventana_principal()
        self.crear_pulgas()
        self.iniciar_actualizacion()
        
    def crear_pulgas(self):
        pulga1 = Pulga(1200, 800)
        pulga2 = PulgaLenta(1200, 800)
        pulga3 = PulgaRapida(1200, 800)
        pulga4 = PulgaTraslucida(1200, 800, self.vista.canvas)
        self.pulgas.extend([pulga1, pulga2, pulga3, pulga4])
        
    def __init__(self):
        self.pulgas = []
        self.vista = Vista(self)
        self.timer = None
        
    def mouse_clicked(self, event):
        for pulga in self.pulgas:
            if pulga.is_visible() and pulga.x <= event.x <= pulga.x + pulga.pulga.width() and pulga.y <= event.y <= pulga.y + pulga.pulga.height():
                pulga.click()
                pulga.visible = False
            
                pulgas_invisibles = sum(1 for p in self.pulgas if not p.is_visible())
            
                if pulgas_invisibles >= 4:
                    print("¡Juego terminado!")
                    self.vista.canvas.after_cancel(self.timer)
                    self.vista.mostrar_mensaje_victoria()
                break
                
    def actualizar_juego(self):
        for pulga in self.pulgas:
            pulga.mover_aleatoriamente()
        self.vista.actualizar_canvas(self.pulgas)
        self.timer = self.vista.canvas.after(100, self.actualizar_juego)
        
    def iniciar_actualizacion(self):
        self.timer = self.vista.canvas.after(100, self.actualizar_juego)
