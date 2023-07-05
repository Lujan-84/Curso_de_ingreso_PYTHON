import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Lujan
apellido: Miguel
-----
Al presionar el botón Mostrar pedir un número. Informar si el número es PRIMO o no.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero = int(prompt(title="Prompt",prompt="Ingrese un numero"))
        if numero == 0:
            alert(title="Alert",message="No es PRIMO")
        elif numero < 3:
            alert(title="Alert",message="Es PRIMO")
        else:   
            for num in range(2,numero):
                flag = True
                if numero%num == 0:
                    alert(title="Alert",message="No es PRIMO")
                    flag = False
                    break
        if flag:
            alert(title="Alert",message="Es PRIMO")
            
if __name__ == "__main__":
    app = App()
    app.mainloop()