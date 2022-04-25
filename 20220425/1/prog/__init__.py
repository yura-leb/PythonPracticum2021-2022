import tkinter
import os
from PIL import Image, ImageTk


def main():

    root = tkinter.Tk()

    # создаем рабочую область
    frame = tkinter.Frame(root)
    frame.grid()

    # Добавим метку
    label = tkinter.Label(frame, text="Hello, World!").grid(row=1, column=1)

    # вставляем кнопку
    but = tkinter.Button(frame, text="Кнопка").grid(row=1, column=2)
    
    # Добавим изображение
    canvas = tkinter.Canvas(root, height=400, width=700)
    imgpath = os.path.join(os.path.dirname(__file__), "icon.png")
    image = Image.open(imgpath)
    photo = ImageTk.PhotoImage(image)
    image = canvas.create_image(0, 0, anchor="nw", image=photo)
    canvas.grid(row=2, column=1)
    root.mainloop()
