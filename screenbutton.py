
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os


# def openfn():
#     filename = filedialog.askopenfilename(title='open')
#     return filename
# def open_img():
#     # x = openfn()
#     img = Image.open('planta.jpg')
#     img = img.resize((250, 250), Image.ANTIALIAS)
#     img = ImageTk.PhotoImage(img)
#     panel = Label(root, image=img)
#     panel.image = img
#     panel.pack()


def clickedcam():
    root = Tk()
    root.title("Alerta de Incendio")
    root.geometry('600x300')
    root.resizable(width=True, height=True)

    lab = Label(root, text="Alerta de Incendio", font=("Arial Bold", 35), padx=10, pady=10)
    lab.grid(column=2, row=5, sticky=W)

    img = Image.open("planta.jpg")

    photo =ImageTk.PhotoImage(img)
    lab =Label(image=photo).place(x=50,y=50)
    panel = Label(root, image=img).grid(row=1, column=1)
    panel.pack(side="bottom", fill="both", expand="yes")
    root.mainloop()



def clickedlock():
    lbl.configure(text="Button was clicked Locks !!")


def clickedBack():
    lbl.configure(text="Button was clicked Back !!", padx = 20, pady = 20 )




window = Tk()
window.title("HomeSafe")
window.geometry('600x300')
window.resizable(width=True, height=True)




lbl = Label(window, text="HomeSafe", font=("Arial Bold", 35), padx = 10, pady = 10)
lbl.grid(column=0, row=0, sticky=W)

btncamera = Button(window, text="Feed Cameras", command = clickedcam)
btncamera.grid(column=4, row=20, padx = 10, pady = 10)

btnlocks = Button(window, text="Locks", command = clickedlock)
btnlocks.grid(column=8, row=20, padx = 10, pady = 10)

btnback = Button(window, text="Voltar", command = clickedBack)
btnback.grid(column=6, row=25, pady = 10)



window.mainloop()
