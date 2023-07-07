'''
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print)

'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        flag = True
        contador = 0
        suma_edades = 0
        contador_votos = 0
        maximo = 0
        minimo = 1000000
        while flag:
            while flag:
                nombre = prompt("Datos","Ingrese el nombre")
                if (nombre == None):
                    flag = False
                    break
                elif (nombre.isalpha()):
                    break
            while flag:
                edad = prompt("Dato","Ingrese la edad")
                if (edad.isnumeric()):
                    edad = int(edad)
                    if (edad > 25):
                        contador += 1
                        suma_edades += edad
                        break
            while flag:
                cantidad_votos = prompt("Dato","Ingrese cantidad de votos")
                cantidad_votos = int(cantidad_votos)
                if (cantidad_votos > 0):
                    contador_votos += cantidad_votos
                    if (cantidad_votos > maximo):
                        maximo = cantidad_votos
                        mas_votado = nombre
                    if (cantidad_votos < minimo):
                        minimo = cantidad_votos
                        menos_votado = nombre
                        edad_menos_votado = edad
                    break
        
        promedio_edades = suma_edades / contador    
        print("El candidato mas votado fue " + mas_votado)
        print("El candidato con menos votos fue " + menos_votado + " y tiene " + str(edad_menos_votado) + " años")    
        print("El promedio de edades de los candidatos es: " + str(promedio_edades))
        print("El total de votos emitidos fue: " + str(contador_votos))
                


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
