import tkinter as tk

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.current_question = 0
        self.score = 0

        self.window = tk.Tk()
        self.window.title("Вікторина")

        self.question_label = tk.Label(self.window, text="")
        self.question_label.pack()

        self.answer_var = tk.StringVar()
        self.answer_var.set(None)

        self.radio_buttons = []
        for i in range(3):
            radio_button = tk.Radiobutton(self.window, variable=self.answer_var, value=i)
            radio_button.pack()
            self.radio_buttons.append(radio_button)

        self.next_button = tk.Button(self.window, text="Далі", command=self.next_question)
        self.next_button.pack()

        self.load_question()

        self.window.mainloop()

    def load_question(self):
        question = self.questions[self.current_question]
        self.question_label.config(text=question["question"])

        for i in range(3):
            self.radio_buttons[i].config(text=question["answers"][i])

    def next_question(self):
        if self.answer_var.get() is not None:
            selected_answer = self.answer_var.get()
            correct_answer = self.questions[self.current_question]["correct_answer"]
            
            if selected_answer == correct_answer:
                self.score += 1

            self.current_question += 1
            self.answer_var.set(None)

            if self.current_question < len(self.questions):
                self.load_question()
            else:
                self.show_results()

    def show_results(self):
        self.window.destroy()
        print(f"Результат: {self.score}/{len(self.questions)}")

# Заповніть список питань у форматі: {"question": "Питання", "answers": ["Відповідь 1", "Відповідь 2", "Відповідь 3"], "correct_answer": індекс_правильної_відповіді}
questions = [
    {"question": "Скільки планет у Сонячній системі?", "answers": ["7", "8", "9"], "correct_answer": 1},
    {"question": "Яка столиця Франції?", "answers": ["Мадрид", "Париж", "Лондон"], "correct_answer": 1},
    {"question": "Яка найбільша планета у Сонячній системі?", "answers": ["Марс", "Юпітер", "Венера"], "correct_answer": 1},
    # Додайте інші питання за необхідності
]

quiz = Quiz(questions)
