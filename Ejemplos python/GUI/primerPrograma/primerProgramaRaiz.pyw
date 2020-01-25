from tkinter import *

#Crear variable para la raiz 
raiz=Tk()
#Poner titulo 
raiz.title("Ventana de prueba")
#Metodo para no poder redimensionar el formulario 
#raiz.resizable(False,False)#los parametros son booleanos primero width y el segundo heigth 
#cambiar icono 
raiz.iconbitmap("persona.ico")
#cambiar el tamaño por defecto 
#raiz.geometry("650x350")#los parametros van entre comillas
#Cambiar color 
raiz.config(bg="lightblue")#Sirve para muchas cosa bg es background color de fondo y entre comillas el color

#Crear frame 
miFrame=Frame()
#Importante poner el frame dentro de la raiz 
#miFrame.pack(fill="both", expand=True)#Se espande el frame a nivel de la raíz 
miFrame.pack()
#Cambiar el color del frame 
miFrame.config(bg="green")
#Cambiar el tamaño del frame y la raiz de inicio se acopla  a este tamaño 
miFrame.config(width="650",height="350")
#Cambiar el borde del frame 
miFrame.config(bd=35)
#Cambiar el tipo de borde 
miFrame.config(relief="groove")
#Cambiar el cursor del frame 
miFrame.config(cursor="hand2")
#Crear ventana principal 
raiz.mainloop()