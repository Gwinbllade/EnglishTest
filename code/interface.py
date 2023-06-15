from tkinter import *
from tkinter import messagebox
import os
import tkinter as tk
from tkinter import simpledialog
import subprocess

class MainWindow:
    def __init__(self):
        self.main_window = Tk()
        self.main_window.geometry('600x600')
        self.main_window.configure(bg="#eac1f5")
        
        self.create_widgets()

    def create_widgets(self):
        self.titel = Label(self.main_window, text='Do you speak English?', fg='black', font='Times 30', bg="#eac1f5")
        self.titel.place(x='100', y='90')

        self.test_button = Button(self.main_window, text='Флеш картки', width=20, font="14px", command=self.open_flashCards)
        self.test_button.place(x='50', y='200')

        self.quiz_button = Button(self.main_window, text='Квіз', width=20, font="14px", command=self.open_quiz)
        self.quiz_button.place(x='350', y='200')

        self.edit_button = Button(self.main_window, text='Редагувати БД', width=20, font="14px", command=self.open_edit_dialog)
        self.edit_button.place(x='200', y='500')

    def open_edit_dialog(self):
        self.main_window.destroy()  # Закрити головне вікно
        file_browser = FileBrowser()  # Створити екземпляр FileBrowser
        file_browser.run()  # Запустити FileBrowser

    def open_quiz(self):
        self.main_window.destroy()  
        quizWindow = Quiz()  
        quizWindow.run()  


    def open_flashCards(self):
        self.main_window.destroy() 
        fleshCardsWindow = FlashCards()  
        fleshCardsWindow.run() 

    def run(self):
       
        self.main_window.mainloop()



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

        folder_path = "./BD" 
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


class Quiz:
    def __init__(self):
        self.file_list = self.get_file_list()
        self.selected_file = None

        self.window = tk.Tk()
        self.window.title("Вибір файлу")
        self.window.geometry('600x600')
        self.window.configure(bg="#eac1f5")

        self.file_label = tk.Label(self.window, text="Оберіть файл:", font="Times 20", bg="#eac1f5")
        self.file_label.pack(pady=50)

        self.file_listbox = tk.Listbox(self.window, font="Times 14")
        self.file_listbox.pack(pady=10)

        for file_name in self.file_list:
            self.file_listbox.insert(tk.END, file_name)

        self.file_listbox.bind("<<ListboxSelect>>", self.on_file_select)

        self.start_button = tk.Button(self.window, text="Почати", font="Times 20", width=10, height="1", command=self.start_quiz, bg="#eac1f5")
        self.start_button.pack()

        self.exit_button = tk.Button(self.window, text="Вийти в головне меню", font="Times 12", width=20, height="1", command=self.go_to_main_menu, bg="#eac1f5")
        self.exit_button.pack(side=tk.BOTTOM, padx=10, pady=10, anchor=tk.SW)

        self.window.mainloop()

    def get_file_list(self):
        folder_path = "./BD"
        file_list = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        return file_list

    def on_file_select(self, event):
        selected_index = self.file_listbox.curselection()
        if selected_index:
            self.selected_file = self.file_listbox.get(selected_index[0])

    def start_quiz(self):


        if self.selected_file:
            self.window.destroy()
            self.load_quiz()
        else:
            messagebox.showerror("Помилка", "Виберіть файл перед початком тесту")
 

    def load_quiz(self):
        path = "./BD/" + self.selected_file
        num_lines = sum(1 for line in open(path))
 
        self.questions = self.read_test_file("./BD_Test/test.txt")
        subprocess.call(['./m', path, str(num_lines)])
        self.current_question = 0
        self.score = 0

        self.window = tk.Tk()
        self.window.title("Вікторина")
        self.window.geometry('600x600')
        self.window.configure(bg="#eac1f5")

        self.question_label = tk.Label(self.window, text="", font="Times 20", bg="#eac1f5")
        self.question_label.pack(pady=50)

        self.answer_var = tk.StringVar()
        self.answer_var.set(None)

        self.radio_buttons = []
        for i in range(3):
            radio_button = tk.Radiobutton(self.window, variable=self.answer_var, value=i+1,  selectcolor="#eac1f5", activebackground="#eac1f5")
            radio_button.pack()
            self.radio_buttons.append(radio_button)

        self.next_button = tk.Button(self.window, text="Далі", font="Times 20", width=10, height="1", command=self.next_question, bg="#eac1f5")
        self.next_button.pack()

        self.exit_button = tk.Button(self.window, text="Вийти в головне меню", font="Times 12", width=20, height="1", bg="#eac1f5", command = self.go_to_main_menu)
        self.exit_button.pack(side=tk.BOTTOM, padx=10, pady=10, anchor=tk.SW)

        self.load_question()


    def load_question(self):
        question = self.questions[self.current_question]
        self.question_label.config(text="Який переклад слова: "+question["question"] + "?")

        for i in range(3):
            self.radio_buttons[i].config(text=question["answers"][i], font="Times 20", width=10, height=3, bg="#eac1f8")

    def next_question(self):
        if self.answer_var.get() is not None:
            selected_answer = self.answer_var.get()

            correct_answer = self.questions[self.current_question]["correct_answer"]
            if int(selected_answer) == int(correct_answer):
                self.score += 1

            self.current_question += 1
            self.answer_var.set(None)

            if self.current_question < len(self.questions):
                self.load_question()
            else:
                self.show_results()

    def show_results(self):
        result_message = f"Результат: {self.score}/{len(self.questions)}"
        messagebox.showinfo("Результати", result_message)
        self.window.destroy()
        Quiz()

    def go_to_main_menu(self):
        self.window.destroy()
        main_window = MainWindow()
        main_window.run()

    def read_test_file(self, file_path):
        questions = []
        with open(file_path, 'r', encoding="ANSI") as file:
            lines = file.readlines()

        for line in lines:
            line = line.strip()
            data = line.split()
            if len(data) > 1:
                questions.append({"question": data[0], "answers": [data[1],data[2],data[3]], "correct_answer": int(data[4])})
        return questions
    
    def run(self):
        self.window.mainloop()


class FlashCards:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Карточки")
        self.window.geometry("600x600")
        self.window.configure(bg="#eac1f5")  # Колір  вікна

        self.file_listbox = tk.Listbox(self.window)
        self.file_listbox.pack(pady=10)

        self.load_files("./BD")

        self.select_button = tk.Button(self.window, text="Вибрати", width=20, font="14px", command=self.select_file)
        self.select_button.place(x='200', y='500')

        self.back_button = tk.Button(self.window, text="Назад", command=self.show_previous_line)
        self.back_button.pack_forget()

        self.forward_button = tk.Button(self.window, text="Вперед", state=tk.DISABLED, command=self.show_next_line)

        self.show_translation_button = tk.Button(self.window, text="Показати переклад", command=self.show_translation)
        self.back_to_list_button = tk.Button(self.window, text="Назад до списку", command=self.go_back_to_list)

        self.exit_button = tk.Button(self.window, text="Вийти в головне меню", font="Times 12", width=20, height="1", command=self.go_to_main_menu, bg="#eac1f5")
        self.exit_button.pack(side=tk.BOTTOM, padx=10, pady=10, anchor=tk.SW)

        self.word_label = tk.Label(self.window, font="Times 25")
        self.translation_label = tk.Label(self.window, font="Times 25")
        self.current_file = None
        self.current_lines = []
        self.current_line_index = 0


    def run(self):
        self.window.mainloop()


    def load_files(self, folder_path):
        files = os.listdir(folder_path)
        self.file_listbox.delete(0, tk.END)
        for file_name in files:
            self.file_listbox.insert(tk.END, file_name)


    def go_to_main_menu(self):
        self.window.destroy()
        main_window = MainWindow()
        main_window.run()


    def select_file(self):
        selected_file = self.file_listbox.get(tk.ACTIVE)
        if selected_file:
            self.file_listbox.pack_forget()
            self.select_button.pack_forget()
            self.back_button.pack(pady=5)
            self.forward_button.pack(pady=5)
            self.show_translation_button.pack(pady=5)
            self.back_to_list_button.pack(pady=5)
            self.current_file = selected_file
            self.load_lines(selected_file)
            self.show_line(0)

    def load_lines(self, file_name):
        self.current_lines.clear()
        with open(f"./BD/{file_name}", "r") as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                self.current_lines.append(line)

    def show_line(self, line_index):
        line = self.current_lines[line_index]
        line_parts = line.split('-')
        word = line_parts[1]  # Друга частина рядка (слово)
        self.word_label.config(text=f"Слово: {word}")
        self.word_label.pack(pady=10)
        self.current_line_index = line_index
        self.update_navigation_buttons()

    def show_previous_line(self):
        if self.current_line_index > 0:
            self.hide_translation()
            self.show_line(self.current_line_index - 1)

    def show_next_line(self):
        if self.current_line_index < len(self.current_lines) - 1:
            self.hide_translation()
            self.show_line(self.current_line_index + 1)

    def update_navigation_buttons(self):
        if self.current_line_index == 0:
            self.back_button.config(state=tk.DISABLED)
        else:
            self.back_button.config(state=tk.NORMAL)

        if self.current_line_index == len(self.current_lines) - 1:
            self.forward_button.config(state=tk.DISABLED)
        else:
            self.forward_button.config(state=tk.NORMAL)

    def show_translation(self):
        line = self.current_lines[self.current_line_index]
        line_parts = line.split('-')
        translation = line_parts[0]  # Перша частина рядка (переклад)
        word = line_parts[1]  # Друга частина рядка (слово)
        self.translation_label.config(text=f"Переклад: {translation}")
        self.translation_label.pack(pady=10)

    def hide_translation(self):
        self.translation_label.pack_forget()

    def go_back_to_list(self):
        self.word_label.pack_forget()
        self.translation_label.pack_forget()
        self.back_button.pack_forget()
        self.forward_button.pack_forget()
        self.show_translation_button.pack_forget()
        self.back_to_list_button.pack_forget()
        self.file_listbox.pack(pady=10)
        self.select_button.pack(pady=5)
        self.current_file = None
        self.current_lines.clear()
        self.current_line_index = 0

        

if __name__ == "__main__":
    subprocess.call(['g++', './Source.cpp', '-o', 'm'])
    window = MainWindow()
    window.run()