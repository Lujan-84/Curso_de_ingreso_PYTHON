import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Lujan
aperllido: Miguel
-----
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        suma_positivos = 0
        suma_negativos = 0
        contador_positivos = 0
        contador_negativos = 0
        contador_ceros = 0
        while True:
            numero = prompt(title="Prompt",prompt="Ingrese un numero:")
            if numero == None:
                break
            else:
                numero = int(numero)
                if numero == 0:
                    contador_ceros +=1
                elif numero > 0:
                    suma_positivos += numero
                    contador_positivos +=1
                else:
                    suma_negativos += numero
                    contador_negativos += 1
        
        if contador_negativos>contador_positivos:
            diferencia = contador_negativos -contador_positivos
        else:
            diferencia = contador_positivos - contador_negativos

        alert(title="Alert",message=f"La suma acumulada de los negativos es: {suma_negativos}.\nLa suma acumulada de los positivos es: {suma_positivos}.\nLa cantidad de numeros positivos ingresados: {contador_positivos}.\nLa cantidad de numeros negativos ingresados es: {contador_negativos}.\nLa cantidad de ceros ingresada es: {contador_ceros}.\nLa diferencia entre la cantidad de los numeros positivos ingresados y los negativos es: {diferencia}")

    
if __name__ == "__main__":
    app = App()
    app.mainloop()
