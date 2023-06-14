import tkinter as tk
from tkinter import messagebox

class Quiz:
    def __init__(self):
        self.questions = self.readTest()
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

        self.load_question()

        self.window.mainloop()

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

    @staticmethod 
    def readTest():
        questions = []
        with open("./BD_Test/test.txt", 'r', encoding="UTF-8") as file:
            lines = file.readlines()

        for line in lines:
            line = line.strip()
            data = line.split()
            if len(data) > 1:
                questions.append({"question": data[0], "answers": [data[1],data[2],data[3]], "correct_answer": int(data[4])})
        return questions

quiz = Quiz()
