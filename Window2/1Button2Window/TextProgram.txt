from tkinter import *
from PIL import Image, ImageTk

window = Tk()
rotation_angle = 0

def click():
    global smaller_image, rotation_angle
    rotation_angle += 190
    rotated_image = image.rotate(rotation_angle)
    smaller_image = ImageTk.PhotoImage(rotated_image.resize((50,50)))
    image_label.config(image=smaller_image)

button = Button(window, text='Click me!!')
button.config(command=click)
button.config(font=('Ink Free', 30, 'bold'))
button.configure(bg='#ca69fa')
button.configure(fg='#390354')
button.config(activebackground='#500d70')
button.config(activeforeground='#d79df2')

image = Image.open('Untitled8_20230614114503.png')
resized_image = image.resize((50, 50))
smaller_image = ImageTk.PhotoImage(resized_image)

image_label = Label(window, image=smaller_image)
image_label.pack(side='left')
button.pack(side='left')

window.mainloop()
