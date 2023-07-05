import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Lujan
apellido: Miguel
---
Ejercicio: entrada_salida_02
---
Enunciado:
Al presionar el botón  'Mostrar', se deberá obtener un dato utilizando el Dialog Prompt
y luego mostrarlo utilizando el Dialog Alert
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        #Asigno a la variable nombre lo que retorna la funcion prompt
        nombre = prompt("Pregunta", "Ingrese su nombre")
        
        #Proceso: creo el mensaje
        mensaje = "El nombre ingresado es: " + nombre
        
        #Muestro utilizando el Dialogo Alert
        alert("Mensaje",mensaje)
        
    
if __name__ == "__main__":
    app = App()
    app.mainloop()