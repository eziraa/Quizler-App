import random
from data import question_data
from Quiz_Ui import QuizUi

score = 0
new_question = random.choice(question_data)
numbers_of_question = len(question_data)
is_finished = False
quiz_ui = QuizUi(score=score, new_question=new_question, numbers_of_question=numbers_of_question)


# Handling generate new question
def generate_new_question():
    global new_question
    quiz_ui.canvas.itemconfig(quiz_ui.background_img, image=quiz_ui.question_bg_img)
    if len(question_data) > 0:
        new_question = random.choice(question_data)
        question_data.remove(new_question)
        quiz_ui.canvas.itemconfig(quiz_ui.question_text, text=new_question["question"])
    else:
        global is_finished
        is_finished = True
        quiz_ui.canvas.itemconfig(quiz_ui.question_text,
                                  text=f"You have finished the question\n Your score: {score}/{numbers_of_question}\n Your lost: {numbers_of_question - score} questions")


quiz_ui.question_timer = quiz_ui.window.after(3, generate_new_question)


# Handle true user answer
def is_true():
    if not is_finished:
        global score
        answer = new_question["correct_answers"]
        if answer == "True":
            score += 1
            quiz_ui.score_label.config(text=f"Score: {score}/{numbers_of_question}")
            quiz_ui.canvas.itemconfig(quiz_ui.background_img, image=quiz_ui.correct_bg_img)
        else:
            quiz_ui.canvas.itemconfig(quiz_ui.background_img, image=quiz_ui.wrong_bg_img)
        quiz_ui.window.after_cancel(quiz_ui.question_timer)
        quiz_ui.window.after(3000, func=generate_new_question)


# Handling false  user answer
def is_false():
    if not is_finished:
        global score
        answer = new_question["correct_answers"]
        if answer == "False":
            score += 1
            quiz_ui.score_label.config(text=f"Score: {score}/{numbers_of_question}")
            quiz_ui.canvas.itemconfig(quiz_ui.background_img, image=quiz_ui.correct_bg_img)
        else:
            quiz_ui.canvas.itemconfig(quiz_ui.background_img, image=quiz_ui.wrong_bg_img)
        quiz_ui.window.after_cancel(quiz_ui.question_timer)
        quiz_ui.window.after(3000, func=generate_new_question)


quiz_ui.wrong_btn.config(command=is_false)
quiz_ui.correct_btn.config(command=is_true)
quiz_ui.window.mainloop()

# Creating buttons
