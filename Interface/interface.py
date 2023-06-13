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
        self.main_window.destroy()  # Закрити головне вікно
        file_browser = FileBrowser()  # Створити екземпляр FileBrowser
        file_browser.run()  # Запустити FileBrowser

    def run(self):
        self.main_window.mainloop()

if __name__ == "__main__":
    window = MainWindow()
    window.run()


import os
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class FileBrowser:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Редагування БД")
        self.window.geometry('600x600')
        self.window.configure(bg="#eac1f5")  # Колір головного вікна

        self.file_listbox = tk.Listbox(self.window)
        self.file_listbox.pack(side=tk.LEFT, fill=tk.BOTH, padx=10)  # Added padx and pady for spacing

        self.line_listbox = tk.Listbox(self.window)
        self.line_listbox.pack(side=tk.LEFT, fill=tk.BOTH, padx=10)  # Added padx and pady for spacing

        self.labal1 = tk.Label(text="Слово українською", bg="#eac1f5", font="Times 14")
        self.labal1.pack()
        self.text_entry_1 = tk.Entry(self.window, font="Times 14")
        self.text_entry_1.pack(fill=tk.BOTH)

        self.labal2 = tk.Label(text="Слово англійською", bg="#eac1f5", font="Times 14")
        self.labal2.pack()
        self.text_entry_2 = tk.Entry(self.window, font="Times 14")
        self.text_entry_2.pack(fill=tk.BOTH)

        self.update_line_button = tk.Button(self.window, text="Оновити слово", font="Times", width="15", height="1",
                                            command=self.update_line)
        self.update_line_button.pack(pady=10)

        self.delete_file_button = tk.Button(self.window, text="Видалити файл", font="Times", width="15", height="1",
                                            command=self.delete_file)
        self.delete_file_button.pack(pady=10)

        self.delete_line_button = tk.Button(self.window, text="Видалити слово", font="Times", width="15", height="1",
                                            command=self.delete_line)
        self.delete_line_button.pack(pady=10)

        self.add_file_button = tk.Button(self.window, text="Додати файл", font="Times", width="15", height="1",
                                         command=self.add_file)
        self.add_file_button.pack(pady=10)

        self.add_line_button = tk.Button(self.window, text="Додати слово", font="Times", width="15", height="1",
                                         command=self.show_add_line_dialog)
        self.add_line_button.pack(pady=10)

        self.selected_file = ""
        self.selected_line_index = -1

        self.exit_main_menu_button = tk.Button(self.window, text='Головне меню', width=20, font="14px",
                                               command=self.exit_main_menu)
        self.exit_main_menu_button.place(x='400', y='550')

        folder_path = "./BD"  # Задайте шлях до папки тут
        self.load_files(folder_path)

        self.file_listbox.bind("<<ListboxSelect>>", self.file_selected)
        self.line_listbox.bind("<<ListboxSelect>>", self.line_selected)

        self.window.mainloop()

    def load_files(self, folder_path):
        self.file_listbox.delete(0, tk.END)  # Очищаємо список файлів

        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        text_files = [f for f in files if f.endswith(".txt")]

        for file_name in text_files:
            self.file_listbox.insert(tk.END, file_name)

    def file_selected(self, event):
        self.selected_file = self.file_listbox.get(self.file_listbox.curselection())
        file_path = os.path.join("./BD", self.selected_file)  # Задайте шлях до папки тут
        self.display_file_content(file_path)

    def line_selected(self, event):
        self.selected_line_index = self.line_listbox.curselection()[0]
        line_text = self.line_listbox.get(self.selected_line_index)
        parts = line_text.split(" - ")
        if len(parts) == 2:
            self.text_entry_1.delete(0, tk.END)
            self.text_entry_2.delete(0, tk.END)
            self.text_entry_1.insert(tk.END, parts[0])
            self.text_entry_2.insert(tk.END, parts[1])

    def display_file_content(self, file_path):
        self.line_listbox.delete(0, tk.END)  # Очищаємо список рядків

        with open(file_path, "r") as file:
            lines = file.readlines()

        for line in lines:
            self.line_listbox.insert(tk.END, line.rstrip("\n"))

    def update_line(self):
        new_line_text_1 = self.text_entry_1.get()
        new_line_text_2 = self.text_entry_2.get()

        if self.selected_file and self.selected_line_index >= 0:
            file_path = os.path.join("./BD", self.selected_file)  # Задайте шлях до папки тут

            with open(file_path, "r") as file:
                lines = file.readlines()

            updated_line = f"{new_line_text_1} - {new_line_text_2}\n"
            lines[self.selected_line_index] = updated_line

            with open(file_path, "w") as file:
                file.writelines(lines)

            self.display_file_content(file_path)

    def delete_file(self):
        if self.selected_file:
            file_path = os.path.join("./BD", self.selected_file)  # Задайте шлях до папки тут
            os.remove(file_path)
            self.selected_file = ""
            self.line_listbox.delete(0, tk.END)
            self.load_files("./BD")  # Задайте шлях до папки тут

    def delete_line(self):
        if self.selected_file and self.selected_line_index >= 0:
            file_path = os.path.join("./BD", self.selected_file)  # Задайте шлях до папки тут

            with open(file_path, "r") as file:
                lines = file.readlines()

            del lines[self.selected_line_index]

            with open(file_path, "w") as file:
                file.writelines(lines)

            self.selected_line_index = -1
            self.display_file_content(file_path)

            # Очищаємо поля введення
            self.text_entry_1.delete(0, tk.END)
            self.text_entry_2.delete(0, tk.END)

    def add_file(self):
        file_name = simpledialog.askstring("Додати файл", "Введіть назву файлу:")
        if file_name:
            if not file_name.endswith(".txt"):
                file_name += ".txt"

            folder_path = "./BD"  # Задайте шлях до папки тут
            file_path = os.path.join(folder_path, file_name)
            if os.path.exists(file_path):
                messagebox.showerror("Помилка", "Файл вже існує")
            else:
                with open(file_path, "w"):
                    pass  # Створюємо порожній файл
                self.load_files("./BD")  # Задайте шлях до папки тут

    def show_add_line_dialog(self):
        if self.selected_file:
            dialog = tk.Toplevel(self.window)
            dialog.title("Додати рядок")

            label_1 = tk.Label(dialog, text="Укр:")
            label_1.pack()
            entry_1 = tk.Entry(dialog)
            entry_1.pack()

            label_2 = tk.Label(dialog, text="Анг:")
            label_2.pack()
            entry_2 = tk.Entry(dialog)
            entry_2.pack()

            save_button = tk.Button(dialog, text="Зберегти",
                                    command=lambda: self.add_line(entry_1.get(), entry_2.get(), dialog))
            save_button.pack()

    def add_line(self, line_text_1, line_text_2, dialog):
        if line_text_1 and line_text_2:
            file_path = os.path.join("./BD", self.selected_file)  # Задайте шлях до папки тут
            new_line = f"{line_text_1} - {line_text_2}\n"

            with open(file_path, "a") as file:
                file.write(new_line)

            self.display_file_content(file_path)
            dialog.destroy()

    def exit_main_menu(self):
        self.window.destroy()
        main_window = MainWindow()
        main_window.run()

if __name__ == "__main__":
    window = FileBrowser()
    window.mainloop()
