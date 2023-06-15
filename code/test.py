import os
import tkinter as tk
from tkinter import messagebox, simpledialog


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
        self.file_label.pack_forget()
        self.file_listbox.pack(pady=10)
        self.select_button.pack(pady=5)
        self.current_file = None
        self.current_lines.clear()
        self.current_line_index = 0


if __name__ == "__main__":
    flashcards = FlashCards()
    flashcards.run()
