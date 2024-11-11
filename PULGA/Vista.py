import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

class Vista:
    def __init__(self, controlador):
        self.controlador = controlador
        self.root = tk.Tk()
        self.root.withdraw()
        self.crear_ventana_bienvenida()
        
    def crear_ventana_bienvenida(self):
        self.ventana_bienvenida = tk.Toplevel(self.root)
        self.ventana_bienvenida.title("Bienvenida")
        self.ventana_bienvenida.geometry("700x700")
        self.ventana_bienvenida.configure(bg="dark turquoise")
        
        etiqueta_bienvenida = tk.Label(
            self.ventana_bienvenida,
            text="BIENVENIDO A LA PULGA",    
            font=("Arial", 24, "bold"),
            bg="dark turquoise"
        )
        etiqueta_bienvenida.pack(pady=20)
        
        instrucciones = tk.Label(
            self.ventana_bienvenida,
            text="PRESIONA LAS PULGAS PARA GANAR",
            font=("Arial", 12, "bold"),
            fg="black",
            bg="dark turquoise"
        )
        instrucciones.pack(pady=10)
        
        ruta_pulga = os.path.join(os.path.dirname(__file__), "PULGUITA.png")
        imagen_pulga = Image.open(ruta_pulga)
        pulga = ImageTk.PhotoImage(imagen_pulga)
        
        etiqueta_imagen = tk.Label(self.ventana_bienvenida, image=pulga, bg="dark turquoise")
        etiqueta_imagen.image = pulga
        etiqueta_imagen.pack(pady=10)
        
        boton_jugar = tk.Button(
            self.ventana_bienvenida,
            text="Jugar",
            font=("Arial", 14),
            command=self.controlador.iniciar_juego
        )
        boton_jugar.pack(pady=10)

    def crear_ventana_principal(self):
        self.root.deiconify()
        self.root.title("PULGA")
        
        ruta_imagen = os.path.join(os.path.dirname(__file__), "CASA.png")
        self.background_image = tk.PhotoImage(file=ruta_imagen)
        
        self.canvas = tk.Canvas(self.root, width=1200, height=800)
        self.canvas.pack()
        
        self.canvas.bind("<Button-1>", self.controlador.mouse_clicked)

    def actualizar_canvas(self, pulgas):
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, image=self.background_image, anchor="nw")
        for pulga in pulgas:
            pulga.paint(self.canvas)

    def mostrar_mensaje_victoria(self):
        messagebox.showinfo("¡Felicitaciones!", "¡Has ganado el juego!")
        self.root.destroy()
        