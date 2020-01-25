from  Tkinter import*

raiz=Tk()#Crear instancia 
raiz.title("Primer programa en GUI")#titulo formulario 
raiz.config(bg="lightyellow")#Color de fondo de formulario
raiz.resizable(True,True)#Si se puede redimensionar 
raiz.geometry("500x300")

raiz.minsize(200,200)
raiz.maxsize(1200, 900)
raiz.mainloop()

