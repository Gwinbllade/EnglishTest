from tkinter import *
from tkinter import messagebox

# ---------------------------------------------------------------- Налаштування вікна
mainWindow=Tk()
mainWindow.geometry('600x600')
mainWindow.configure(bg="#eac1f5")#Колір головного вікна
# ----------------------------------------------------------------



#
createFileButton=Button(text='Створити файл', width=20, font="14px")
createFileButton.place(x='50', y='100')

EditFileButton=Button(text='Редагувати файл', width=20, font="14px")
EditFileButton.place(x='350', y='100')



mainWindow.mainloop()
