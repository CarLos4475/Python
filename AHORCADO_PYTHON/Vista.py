import tkinter as tk
from tkinter import messagebox
import random
from LogicaFrutas import LogicaFrutas
from LogicaAnimales import LogicaAnimales 
from LogicaProgramacion import LogicaProgramacion


class Vista:
    def __init__(self):
        # Seleccionar lógica de juego
        self.logicas = [LogicaFrutas, LogicaAnimales, LogicaProgramacion]
        self.indice_tematica = 0
        self.logica_juego = self.logicas[self.indice_tematica](self)
        self.puntuacion = 0
        

        self.root = tk.Tk()
        self.root.title("Ahorcado")
        self.root.configure(background="#FFC0CB")
        self.root.geometry("900x850")

        # COMPONENTES
        self.marco_juego = tk.Frame(self.root, bg="#FFC0CB")
        
        self.etiqueta_puntuacion = tk.Label(
            self.marco_juego,
            text=f"Puntuación: {self.puntuacion}",
            font=("Arial", 16, "bold"),
            bg="#FFC0CB"
        )
        
        self.etiqueta_bienvenida = tk.Label(
            self.root,
            text="BIENVENIDO AL JUEGO",
            font=("Arial", 36, "bold"),
            bg="#FFC0CB",
            fg="#FF1493"
        )
        self.canvas_bienvenida = tk.Canvas(self.root, width=300, height=200, bg="#FFC0CB", highlightthickness=0)
        self.boton_iniciar = tk.Button(
            self.root,
            text="Jugar",
            command=self.seleccionar_tematica,
            bg="#FF69B4",
            fg="white",
            font=("Arial", 18),
            padx=20,
            pady=10
        )

        self.etiqueta_palabra = tk.Label(self.marco_juego, text="", font=("Arial", 24), bg="#FFC0CB")
        self.canvas_juego = tk.Canvas(self.marco_juego, width=400, height=400, bg="#FFC0CB")
        self.canvas_vidas = tk.Canvas(self.marco_juego, width=300, height=50, bg="#FFC0CB", highlightthickness=0)
        
        self.marco_entrada = tk.Frame(self.marco_juego, bg="#FFC0CB")
        self.entrada_letra = tk.Entry(self.marco_entrada, font=("Arial", 18), width=5)
        self.boton_adivinar = tk.Button(
            self.marco_entrada,
            text="Adivinar letra",
            command=lambda: self.adivinar_letra(self.entrada_letra.get()),
            bg="#FF69B4",
            fg="white",
            font=("Arial", 14)
        )

        self.canvas_feedback = tk.Canvas(self.marco_juego, width=50, height=50, bg="#FFC0CB", highlightthickness=0)
        
        self.mostrar_pantalla_bienvenida()
        
    def mostrar_pantalla_bienvenida(self):
        self.etiqueta_bienvenida.pack(pady=(30, 20))
        self.canvas_bienvenida.configure(width=400, height=300)
        self.canvas_bienvenida.pack(pady=(0, 20))
        self.boton_iniciar.pack(pady=20)
        self.paso_animacion = 0
        self.animar_ahorcado()

    def animar_ahorcado(self):
        self.canvas_bienvenida.delete("all")
        
        # DIBUJA AL AHORCADO CON UN CONTADOR
        if self.paso_animacion >= 0:
            self.canvas_bienvenida.create_line(100, 250, 300, 250, width=3)
        if self.paso_animacion >= 1:
            self.canvas_bienvenida.create_line(200, 250, 200, 50, width=3)
        if self.paso_animacion >= 2:
            self.canvas_bienvenida.create_line(200, 50, 300, 50, width=3)
        if self.paso_animacion >= 3:
            self.canvas_bienvenida.create_line(300, 50, 300, 100, width=3)
        if self.paso_animacion >= 4:
            self.canvas_bienvenida.create_oval(275, 100, 325, 150, width=3)
        if self.paso_animacion >= 5:
            self.canvas_bienvenida.create_line(300, 150, 300, 220, width=3)
        if self.paso_animacion >= 6:
            self.canvas_bienvenida.create_line(300, 180, 250, 200, width=3)
        if self.paso_animacion >= 7:
            self.canvas_bienvenida.create_line(300, 180, 350, 200, width=3)
        if self.paso_animacion >= 8:
            self.canvas_bienvenida.create_line(300, 220, 250, 270, width=3)
        if self.paso_animacion >= 9:
            self.canvas_bienvenida.create_line(300, 220, 350, 270, width=3)
        
        # Incrementar paso y reiniciar
        self.paso_animacion = (self.paso_animacion + 1) % 10
        self.root.after(1000, self.animar_ahorcado)

    def seleccionar_tematica(self):
        ventana_carga = tk.Toplevel(self.root)
        ventana_carga.title("Cargando Juego")
        ventana_carga.geometry("400x200")
        ventana_carga.configure(bg="#FFC0CB")
        
        x = self.root.winfo_x() + (self.root.winfo_width() // 2) - 200
        y = self.root.winfo_y() + (self.root.winfo_height() // 2) - 100
        ventana_carga.geometry(f"400x200+{x}+{y}")
        
        mensaje = tk.Label(
            ventana_carga,
            text=f"Preparando juego ...",
            font=("Arial", 14, "bold"),
            bg="#FFC0CB"
        )
        mensaje.pack(pady=50)
        
        def iniciar_despues_de_carga():
            ventana_carga.destroy()
            self.iniciar_juego()
            
        self.root.after(2000, iniciar_despues_de_carga)
        
    def iniciar_juego(self):
        self.etiqueta_bienvenida.pack_forget()
        self.canvas_bienvenida.pack_forget()
        self.boton_iniciar.pack_forget()
        self.mostrar_interfaz_juego()
        self.logica_juego.iniciar_juego()
        
        
    def mostrar_interfaz_juego(self):
        self.marco_juego.pack(expand=True, fill=tk.BOTH)
        self.etiqueta_palabra.pack(pady=(20, 10))
        self.canvas_juego.pack(pady=10)
        self.canvas_vidas.pack(pady=(10, 0))  
        self.marco_entrada.grid_columnconfigure(0, weight=1)
        self.marco_entrada.grid_columnconfigure(1, weight=1)
        self.marco_entrada.pack(pady=10)
        self.entrada_letra.grid(row=0, column=0, padx=10, pady=10)
        self.boton_adivinar.grid(row=0, column=1, padx=10, pady=10)
        self.canvas_feedback.pack(pady=10)  

        self.etiqueta_tematica = tk.Label(
            self.marco_juego, 
            text=f"TEMATICA: {self.logica_juego.tema}", 
            font=("Arial", 18, "bold"), 
            bg="#FFC0CB"
        )
        self.etiqueta_puntuacion.pack(anchor='ne', padx=10, pady=5)
        self.etiqueta_tematica.pack(pady=(0, 10))

    def actualizar_interfaz(self, palabra_visualizada, intentos):
        self.etiqueta_palabra.config(text=" ".join(palabra_visualizada))
        self.actualizar_vidas()
        self.actualizar_ahorcado(intentos)

    def adivinar_letra(self, letra):
        resultado = self.logica_juego.adivinar_letra(letra)
        self.entrada_letra.delete(0, tk.END)

        if letra in self.logica_juego.palabra_secreta:
            self.mostrar_simbolo("checkmark")
        else:
            self.mostrar_simbolo("cross")

        if resultado == "ganaste":
            self.puntuacion += 1
            self.etiqueta_puntuacion.config(text=f"Puntuación: {self.puntuacion}")
            self.mostrar_sprite_feliz()
            messagebox.showinfo("¡Felicitaciones!", "¡Has adivinado la palabra!")
            self.nueva_palabra()
        elif resultado == "perdiste":
            self.mostrar_sprite_triste()
            messagebox.showinfo("Game Over", f"La palabra era: {self.logica_juego.palabra_secreta}")
            self.nueva_palabra()
            
    def cambiar_tematica(self):
        self.indice_tematica = (self.indice_tematica + 1) % len(self.logicas)
        self.logica_juego = self.logicas[self.indice_tematica](self)
    
    def nueva_palabra(self):
        self.canvas_juego.delete("sprite")
        self.cambiar_tematica() 
        self.logica_juego.iniciar_juego()
        self.etiqueta_tematica.config(text=f"TEMATICA: {self.logica_juego.tema}")
        self.entrada_letra.focus()

    def mostrar_simbolo(self, simbolo):
        self.canvas_feedback.delete("all")
        if simbolo == "checkmark":
            self.canvas_feedback.create_oval(5, 5, 45, 45, outline="green", width=3)
            self.canvas_feedback.create_line(10, 25, 20, 35, fill="green", width=3)
            self.canvas_feedback.create_line(20, 35, 40, 15, fill="green", width=3)
        elif simbolo == "cross":
            self.canvas_feedback.create_line(10, 10, 40, 40, fill="red", width=3)
            self.canvas_feedback.create_line(40, 10, 10, 40, fill="red", width=3)
        self.root.after(1000, lambda: self.canvas_feedback.delete("all"))

    def finalizar_juego(self, mensaje):
        messagebox.showinfo("Fin del juego", mensaje)
        self.reiniciar_juego()

    def mostrar_sprite_feliz(self):
        self.canvas_juego.delete("sprite")
        self.canvas_juego.create_oval(150, 150, 250, 250, fill="yellow", tags="sprite")
        self.canvas_juego.create_arc(175, 175, 225, 225, start=0, extent=-180, fill="black", tags="sprite")
        self.canvas_juego.create_oval(180, 180, 190, 190, fill="black", tags="sprite")
        self.canvas_juego.create_oval(210, 180, 220, 190, fill="black", tags="sprite")

    def mostrar_sprite_triste(self):
        self.canvas_juego.delete("sprite")
        self.canvas_juego.create_oval(150, 150, 250, 250, fill="yellow", tags="sprite")
        self.canvas_juego.create_arc(175, 200, 225, 250, start=0, extent=180, fill="black", tags="sprite")
        self.canvas_juego.create_oval(180, 180, 190, 190, fill="black", tags="sprite")
        self.canvas_juego.create_oval(210, 180, 220, 190, fill="black", tags="sprite")

    def reiniciar_juego(self):
        self.canvas_juego.delete("sprite")
        self.logica_juego.iniciar_juego()  # Reinicia la lógica del juego
        self.marco_juego.pack_forget()
        self.mostrar_pantalla_bienvenida()

    def actualizar_ahorcado(self, intentos):
        self.canvas_juego.delete("all")
        # Dibujar la base
        self.canvas_juego.create_line(100, 350, 300, 350, width=5)  # Base 
        self.canvas_juego.create_line(200, 350, 200, 50, width=5)   # Palo 
        self.canvas_juego.create_line(200, 50, 300, 50, width=5)    # Techo 
        self.canvas_juego.create_line(300, 50, 300, 100, width=5)   # Cuerda

        # Dibujar el ahorcado conforme los intentos restantes
        if intentos <= 5:
            self.canvas_juego.create_oval(275, 100, 325, 150, width=3)  # Cabeza
        if intentos <= 4:
            self.canvas_juego.create_line(300, 150, 300, 250, width=3)  # Cuerpo
        if intentos <= 3:
            self.canvas_juego.create_line(300, 180, 250, 220, width=3)  # Brazo izquierdo
        if intentos <= 2:
            self.canvas_juego.create_line(300, 180, 350, 220, width=3)  # Brazo derecho
        if intentos <= 1:
            self.canvas_juego.create_line(300, 250, 250, 300, width=3)  # Pierna izquierda
        if intentos <= 0:
            self.canvas_juego.create_line(300, 250, 350, 300, width=3)  # Pierna derecha

    def actualizar_vidas(self):
     self.canvas_vidas.delete("all")
     # Dibujar corazones según las vidas restantes
     vidas_restantes = self.logica_juego.vidas 
     for i in range(vidas_restantes):
         x = 10 + (i * 40)  
         self.canvas_vidas.create_oval(x, 10, x + 30, 40, fill="red")
         self.canvas_vidas.create_text(x + 15, 25, text="♥", font=("Arial", 18), fill="white")

    def iniciar(self):
        self.root.mainloop()
