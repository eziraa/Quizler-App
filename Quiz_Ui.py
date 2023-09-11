from tkinter import *


class QuizUi:
    def __init__(self, score, numbers_of_question, new_question):
        self.window = Tk()
        self.window.title("Quizler App")
        self.window.config(bg="#375362", padx=20, pady=20)

        self.score_label = Label(text=f"Score: {score}/{numbers_of_question}", font=("Ariel", 24, "normal"), fg="white", bg="#375362")
        self.score_label.grid(row=0, column=0)

        self.canvas = Canvas(width=340, height=335, highlightthickness=0)
        self.correct_bg_img = PhotoImage(file="correct_bg.png")
        self.wrong_bg_img = PhotoImage(file="wrong_bg.png")
        self.question_bg_img = PhotoImage(file="question_bg.png")
        self.background_img = self.canvas.create_image(170.5, 175, image=self.question_bg_img)
        self.canvas.grid(row=2, column=0, columnspan=2)
        self.question_text = self.canvas.create_text(170.5, 175, width=300, text=new_question["question"], font=("Ariel", 24, "normal"))

        self.correct_btn_img = PhotoImage(file="correct.png")
        self.correct_btn = Button(image=self.correct_btn_img, highlightthickness=0)
        self.correct_btn.grid(row=3, column=0)

        self.wrong_btn_img = PhotoImage(file="wrong.png")
        self.wrong_btn = Button(image=self.wrong_btn_img, highlightthickness=0)
        self.wrong_btn.grid(row=3, column=1)

        self.window.rowconfigure(2, pad=20)
        self.question_timer = ""
