from tkinter import *
root =Tk()
root.title("Programación O.O")
root.iconbitmap("LOGO.ico")
root.geometry("480x480")
root.config(bg="red")
label=Label(root,text="Bienvenidos a P.O.O")
label.pack(anchor=NW)
label.config(fg="blue",bg="green",font=("Verdana",20))
label1=Label(root,text="Saludos")
label1.pack(anchor=CENTER)
label1.config(fg="black",bg="gray",font=("Comic Sans",18))
label2=Label(root,text="Gracias")
label2.pack(anchor=SE)
label2.config(fg="cyan",bg="white",font=("Times New Roman",16))

root.mainloop()