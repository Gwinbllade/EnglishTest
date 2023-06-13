from tkinter import *
# Налаштування меню тестування
testMenu=Tk()
testMenu.geometry('600x600')
testMenu.configure(bg="#eac1f5")#Колір  вікна

quizButton = Button(testMenu, text='Квіз', width=20, font="14px")
quizButton.place(x='350', y='100')


testButton = Button(testMenu, text='Тест', width=20, font="14px")
testButton.place(x='50', y='100')

editButton = Button(testMenu, text='Редагувати', width=20, font="14px")
editButton.place(x='200', y='500')

testMenu.mainloop()