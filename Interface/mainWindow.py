from tkinter import *
from tkinter import messagebox

class MainWindow:
    def __init__(self):
        self.main_window = Tk()
        self.main_window.geometry('600x600')
        self.main_window.configure(bg="#eac1f5")
        
        self.create_widgets()

    def create_widgets(self):
        self.titel = Label(self.main_window, text='Do you speak English?', fg='black', font='Times 30', bg="#eac1f5")
        self.titel.place(x='100', y='90')

        self.test_button = Button(self.main_window, text='Тест', width=20, font="14px")
        self.test_button.place(x='50', y='200')

        self.quiz_button = Button(self.main_window, text='Квіз', width=20, font="14px")
        self.quiz_button.place(x='350', y='200')

        self.edit_button = Button(self.main_window, text='Редагувати БД', width=20, font="14px", command=self.open_edit_dialog)
        self.edit_button.place(x='200', y='500')

    def open_edit_dialog(self):
        messagebox.showinfo("Увага", "Функціонал редагування БД ще не реалізований")

    def run(self):
        self.main_window.mainloop()

if __name__ == "__main__":
    window = MainWindow()
    window.run()
