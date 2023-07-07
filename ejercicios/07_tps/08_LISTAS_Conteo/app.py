import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el
usuario quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    a. La suma acumulada de los negativos
    b. La suma acumulada de los positivos
    c. Cantidad de números positivos ingresados
    d. Cantidad de números negativos ingresados
    e. Cantidad de ceros
    f. El minimo de los negativos
    g. El maximo de los positivos
    h. El promedio de los negativos

Informar los resultados mediante alert()

'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_cargar = customtkinter.CTkButton(
            master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_cargar.grid(row=2, padx=20, pady=20,
                             columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar Estadísticas", command=self.btn_mostrar_estadisticas_on_click)
        self.btn_mostrar.grid(row=3, padx=20, pady=20,
                              columnspan=2, sticky="nsew")

        self.lista = []

    def btn_comenzar_ingreso_on_click(self):
        while True:
            numero = prompt("Datos" , "Ingrese numero")
            if numero == None:
                break
            else:
                numero = float(numero)
                self.lista.append(numero)

    def btn_mostrar_estadisticas_on_click(self):
        suma_positivos = 0
        suma_negativos = 0
        contador_positivos = 0
        contador_negativos = 0
        contador_ceros = 0
        minimo_negativos = 0
        maximo_positivos = 0 
        for num in self.lista:
            if num > 0:
                contador_positivos += 1
                suma_positivos += num
                if num > maximo_positivos:
                    maximo_positivos = num
            elif num < 0:
                contador_negativos += 1
                suma_negativos += num
                if num < minimo_negativos:
                    minimo_negativos = num
            else:
                contador_ceros += 1
        if contador_negativos > 0:
            promedio_negativos = suma_negativos / contador_negativos
        
        mensaje = f"""La suma acumulada de los negativos es: {suma_negativos}
        La suma acumulada de los positivos es: {suma_positivos}
        Cantidad de numeros positivos ingresados: {contador_positivos}
        Cantidad de numeros negativos ingresados: {contador_negativos}
        Cantidad de ceros: {contador_ceros}
        El minimo de los negativos es: {minimo_negativos}
        El maximo de los positivos es: {maximo_positivos}
        El promedio de los negativos es: {promedio_negativos}"""
        alert("Mensaje" , mensaje)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
