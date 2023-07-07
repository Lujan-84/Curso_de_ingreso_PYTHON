'''
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

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
        cantidad_genero_f = 0
        cantidad_genero_m = 0
        cantidad_genero_nb = 0
        edad_f = 0
        edad_m = 0
        edad_nb = 0
        contador_nb = 0
        contador_asp = 0
        contador_js = 0  
        contador_py = 0  
        edad_menor_jr = 99   
        for i in range(10):
            while True:
                nombre = prompt("Dato","Nombre del postulante")
                if (nombre.isalpha):
                    break
            while True:
                edad = prompt("Dato","Edad del postulante")
                if (edad.isnumeric()):
                    edad = int(edad)
                    if (edad > 17):
                        break
            while True:
                genero = prompt("Dato","Ingrese genero (F-M-NB)")
                genero.upper()
                if (genero == "F" or genero == "M" or genero == "NB"):
                    match genero:
                        case "F":
                            cantidad_genero_f += 1
                            edad_f += edad
                        case "M":
                            cantidad_genero_m += 1
                            edad_m += edad
                        case "NB":
                            cantidad_genero_nb +=1
                            edad_nb += edad
                    break
            while True:
                tecnologia = prompt("Dato","Ingrese Tecnologia")
                tecnologia.upper()
                if (tecnologia == "PYTHON" or tecnologia == "JS" or tecnologia == "ASP.NET"):
                    match tecnologia:
                        case "ASP.NET":
                            contador_asp +=1
                        case "JS":
                            contador_js += 1
                        case "PYTHON":
                            contador_py += 1
                    break
            while True:
                puesto = prompt("Dato","Ingrese el puesto (Jr-Ssr-Sr)")
                if (puesto == "Jr" or puesto == "Ssr" or puesto == "Sr"):
                    match puesto:
                        case "Jr":
                            if (edad < edad_menor_jr):
                                edad_menor_jr = edad
                                nombre_menor_jr = nombre
                    break
            if (puesto == "Ssr" and genero == "NB" and edad > 25 and edad < 40 and tecnologia == "JS" or tecnologia == "ASP.NET"):
                contador_nb +=1 
                    
                           
        promedio_edad_f= edad_f / cantidad_genero_f
        promedio_edad_m = edad_m / cantidad_genero_m
        promedio_edad_nb = edad_nb / cantidad_genero_nb
                    
        if(contador_asp > contador_js and contador_asp > contador_py):
            tecnologia_mas_postulantes = "ASP.NET"
        elif(contador_js > contador_py):
            tecnologia_mas_postulantes = "JS"
        else:
            tecnologia_mas_postulantes = "PYTHON"
            
        porcentaje_f = cantidad_genero_f * 10
        porcentaje_m = cantidad_genero_m * 10
        porcentaje_nb = cantidad_genero_nb * 10
        
        print("La cantidad de postulantes no binarios que programan en ASP.NET o JS cuya edad esta entre 25 y 40, que se postularon para un puesto Ssr es: " + str(contador_nb))
        print("El postulante Jr con menor edad es: " + nombre_menor_jr) 
        print("El promedio de edad de postulantes femeninos es: " + str(promedio_edad_f))  
        print("El promedio de edad de postulantes masculinos es: " + str(promedio_edad_m))
        print("El promedio de edad de postulantes no binarios es: " + str(promedio_edad_nb))
        print("La tecnologia con mas postulantes fue: " + tecnologia_mas_postulantes)
        print("El porcentaje de postulantes femeninos es: " + str(porcentaje_f) + " %")
        print("El porcentaje de postulantes masculinos es: " + str(porcentaje_m) + " %")
        print("El porcentaje de postulantes no binarios es: " + str(porcentaje_nb) + " %")
        
         
                


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
