import random
from tkinter import *
from data import question_data

score = 0
new_question = random.choice(question_data)
numbers_of_question = len(question_data)
is_finished = False

# Creating main window
window = Tk()
window.title("Quizler App")
window.config(bg="#375362", padx=20, pady=20)

# Creating score label
score_label = Label(text=f"Score: {score}/{numbers_of_question}", font=("Ariel", 24, "normal"))
score_label.grid(row=0, column=1)

# Creating canvas
canvas = Canvas(width=340, height=335, highlightthickness=0)
correct_bg_img = PhotoImage(file="correct_bg.png")
wrong_bg_img = PhotoImage(file="wrong_bg.png")
question_bg_img = PhotoImage(file="question_bg.png")
background_img = canvas.create_image(170.5, 175, image=question_bg_img)
canvas.grid(row=2, column=0, columnspan=2)
question_text = canvas.create_text(170.5, 175, width=300, text=new_question["question"], font=("Ariel", 24, "normal"))


# Handling generate new question
def generate_new_question():
    global new_question
    canvas.itemconfig(background_img, image=question_bg_img)
    if len(question_data) > 0:
        new_question = random.choice(question_data)
        question_data.remove(new_question)
        canvas.itemconfig(question_text, text=new_question["question"])
    else:
        global is_finished
        is_finished = True
        canvas.itemconfig(question_text,
                          text=f"You have finished the question\n Your score: {score}/{numbers_of_question}")


# Handle true user answer
def is_true():
    if not is_finished:
        global score
        answer = new_question["correct_answers"]
        if answer == "True":
            score += 1
            score_label.config(text=f"Score: {score}/{numbers_of_question}")
            canvas.itemconfig(background_img, image=correct_bg_img)
        else:
            canvas.itemconfig(background_img, image=wrong_bg_img)
        window.after_cancel(question_timer)
        window.after(3000, func=generate_new_question)


# Handling false  user answer
def is_false():
    if not is_finished:
        global score
        answer = new_question["correct_answers"]
        if answer == "False":
            score += 1
            score_label.config(text=f"Score: {score}/{numbers_of_question}")
            canvas.itemconfig(background_img, image=correct_bg_img)
        else:
            canvas.itemconfig(background_img, image=wrong_bg_img)
        window.after_cancel(question_timer)
        window.after(3000, func=generate_new_question)


# Creating buttons
wrong_btn_img = PhotoImage(file="wrong.png")
wrong_btn = Button(image=wrong_btn_img, command=is_false, highlightthickness=0)
wrong_btn.grid(row=3, column=1)

correct_btn_img = PhotoImage(file="correct.png")
correct_btn = Button(image=correct_btn_img, command=is_true, highlightthickness=0)
correct_btn.grid(row=3, column=0)
window.rowconfigure(2, pad=20)
question_timer = window.after(1, func=generate_new_question)
window.mainloop()
