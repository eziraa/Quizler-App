from tkinter import *
from data import question_data

# Creating main window
window = Tk()
window.title("Quizler App")
window.config(bg="#276344", padx=20, pady=20)

# Creating canvas
canvas = Canvas(width=341, height=357)
question_bg_img = PhotoImage(file="question_bg.png")
canvas.create_image(170.5, 175, image=question_bg_img)
canvas.grid(row=0, column=0, columnspan=2)

# Creating buttons
wrong_btn_img = PhotoImage(file="wrong.png")
wrong_btn = Button(image=wrong_btn_img)
wrong_btn.grid(row=1, column=1)
correct_btn_img = PhotoImage(file="correct.png")
correct_btn = Button(pady=20, padx=20, image=correct_btn_img)
correct_btn.grid(row=1, column=0)
window.mainloop()
