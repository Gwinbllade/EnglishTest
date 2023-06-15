from tkinter import *
from PIL import Image, ImageTk
import time

window = Tk()

def click():
    global smaller_image
    image_label.config(image=smaller_image)  # Restore original image

    # Enlarge the image for a second
    resized_image = image.resize((100, 100))  # Increase size to 100x100 pixels
    larger_image = ImageTk.PhotoImage(resized_image)
    image_label.config(image=larger_image)
    window.update()
    time.sleep(0.5)  # Pause for 1 second

    # Restore the image to the original size
    image_label.config(image=smaller_image)
    window.update()

button = Button(window, text='Click me!!')
button.config(command=click)
button.config(font=('Ink Free', 30, 'bold'))
button.configure(bg='#ca69fa')
button.configure(fg='#390354')
button.config(activebackground='#500d70')
button.config(activeforeground='#d79df2')

image = Image.open('Untitled8_20230614114511.png')
resized_image = image.resize((80, 80))
smaller_image = ImageTk.PhotoImage(resized_image)

image_label = Label(window, image=smaller_image)
image_label.pack(side='left')
button.pack(side='left')

window.mainloop()
