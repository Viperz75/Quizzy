from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#1677c5"
GREEN_COLOR = "#57C84D"
RED_COLOR = "#FF0000"


class QuizzUi:
    import pygame
    pygame.mixer.init()

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzy")
        self.window.iconbitmap("quizzy.ico")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.resizable(0, 0)
        self.score_label = Label(text="Score: 0", font=("Unispace", 14, "normal"), bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280,
                                                     text="Question Text",
                                                     font=("Times New Roman", 20, "normal"),
                                                     fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Buttons
        self.true_button_img = PhotoImage(file="true.png")
        self.true_button = Button(image=self.true_button_img, highlightthickness=0, border=0, command=self.true)
        self.false_button_img = PhotoImage(file="false.png")
        self.false_button = Button(image=self.false_button_img, highlightthickness=0, border=0, command=self.false)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    #Proceeding to the next question
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="Congratulations! You've Reached The End of the Quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    #Commands of True & Buttons
    def true(self):
        self.feedback(self.quiz.check_answer("True"))

    def false(self):
        right = self.quiz.check_answer("False")
        self.feedback(right)

    #Music and Letting The User Know if he is Right or Wrong
    def feedback(self, right):
        if right:
            self.canvas.config(bg=GREEN_COLOR)
            self.pygame.mixer_music.load("right.mp3")
            self.pygame.mixer_music.play(loops=0)
        else:
            self.canvas.config(bg=RED_COLOR)
            self.pygame.mixer_music.load("wrong.mp3")
            self.pygame.mixer_music.play(loops=0)
        self.window.after(1000, self.get_next_question)
