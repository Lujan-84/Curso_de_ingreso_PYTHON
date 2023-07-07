import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Lujan
apellido: Miguel
---
Ejercicio: entrada_salida_09
---
Enunciado:
Al presionar el botón  'Calcular', se deberán obtener los valores contenidos en las cajas de texto (txtSueldo y txtIncremento), 
transformarlos en números y mostrar el importe de sueldo actualizado con el incremento porcentual utilizando el Dialog Alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Sueldo")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_sueldo = customtkinter.CTkEntry(master=self)
        self.txt_sueldo.grid(row=0, column=1)
        
        self.label2 = customtkinter.CTkLabel(master=self, text="% de Incremento")
        self.label2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_incremento = customtkinter.CTkEntry(master=self)
        self.txt_incremento.grid(row=1, column=1)
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        #Asigno a una variable el dato obtenido de la caja de texto
        sueldo_ingresado = self.txt_sueldo.get()
        incremento_ingresado = self.txt_incremento.get()
        #Convierto los datos a numeros
        sueldo_ingresado = float(sueldo_ingresado)
        incremento_ingresado = float(incremento_ingresado)
        #Calculo el sueldo actualizado con incremento
        sueldo_con_incremento = sueldo_ingresado*(1 + incremento_ingresado/100)
        #Creo mensaje
        mensaje = "El sueldo actualizado con el incremento porcentual del " + str(incremento_ingresado) + " % es de: " + str(sueldo_con_incremento)
        #Muestro mensaje
        alert("Mensaje",mensaje)
        
        
    
if __name__ == "__main__":
    app = App()
    app.mainloop()