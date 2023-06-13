from createFileWindow import *



from tkinter import *

def openCreateFileWindow():
    mainWindow.withdraw()
    createFileWindow.deiconify()

def openMainWindow():
    mainWindow.deiconify()
    createFileWindow.withdraw()

def saveWord():
    ukrWord = ukrWordEntry.get()
    engWord = engWordEntry.get()
    print(f"{ukrWord} - {engWord}")

# Налаштування вікна створення файлу
createFileWindow = Tk()
createFileWindow.geometry('600x600')
createFileWindow.configure(bg="#eac1f5")
createFileWindow.withdraw()



engWordLabel = Label(createFileWindow, text='Введіть слово англійською', fg='black', font='Times', bg="#eac1f5")
engWordLabel.place(x='1', y='40')

engWordEntry = Entry(createFileWindow, width=30, bg='light blue', font='14')
engWordEntry.place(x='240', y='40')

ukrWordLabel = Label(text='Введіть слово державною', fg='black', font='Times', bg="#eac1f5")
ukrWordLabel.place(x='1', y='100')

ukrWordEntry = Entry(width=30, bg='light blue', font='14')
ukrWordEntry.place(x='240', y='100')

saveWordButton = Button(text='Зберегти слово', width=20, font="14px", command=saveWord)
saveWordButton.place(x='195', y='400')

switchMainWindowButton = Button(text='Головне меню', width=20, font="14px", command=openMainWindow)
switchMainWindowButton.place(x='195', y='500')

# createFileWindow.mainloop()

#------------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------- Налаштування головного вікна
mainWindow=Tk()
mainWindow.geometry('600x600')
mainWindow.configure(bg="#eac1f5")#Колір головного вікна
# ----------------------------------------------------------------


createFileButton=Button(mainWindow, text='Створити файл', width=20, font="14px", command=openCreateFileWindow)
createFileButton.place(x='50', y='100')

EditFileButton=Button(mainWindow, text='Редагувати файл', width=20, font="14px")
EditFileButton.place(x='350', y='100')



mainWindow.mainloop()
