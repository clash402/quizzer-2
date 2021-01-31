from tkinter import *


class UI(Tk):
    def __init__(self, quiz):
        super().__init__()

        self.quiz = quiz

        self.IMAGE_TRUE_BUTTON = "./images/true.png"
        self.IMAGE_FALSE_BUTTON = "./images/false.png"

        self.COLOR_PRIMARY = "#375362"
        self.COLOR_WHITE = "white"
        self.COLOR_GREEN = "green"
        self.COLOR_RED = "red"

        self.FONT_CANVAS = ("Arial", 20, "italic")
        self.FONT_SCORE_LABEL = ("Arial", 14)

        self._draw()

    # DRAW METHODS
    def _draw(self):
        self._draw_window()
        self._draw_score_label()
        self._draw_canvas()
        self._draw_true_button()
        self._draw_false_button()

    def _draw_window(self):
        self.title("Quizzer")
        self.config(padx=24, pady=24, bg=self.COLOR_PRIMARY)

    def _draw_score_label(self):
        self.score_label = Label(text="Score: 0", font=self.FONT_SCORE_LABEL, fg="white", bg=self.COLOR_PRIMARY)
        self.score_label.grid(column=1, row=0)

    def _draw_canvas(self):
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.canvas_text = self.canvas.create_text(
            150, 125,
            text="Trivia question",
            width=280,
            font=self.FONT_CANVAS
        )
        self.canvas.grid(column=0, columnspan=2, row=1, padx=8, pady=40)

    def _draw_true_button(self):
        self.true_button_image = PhotoImage(file=self.IMAGE_TRUE_BUTTON)
        self.true_button = Button(
            image=self.true_button_image,
            command=self._true_button_clicked,
            highlightthickness=0
        )
        self.true_button.grid(column=0, row=2)

    def _draw_false_button(self):
        self.false_button_image = PhotoImage(file=self.IMAGE_FALSE_BUTTON)
        self.false_button = Button(
            image=self.false_button_image,
            command=self._false_button_clicked,
            highlightthickness=0
        )
        self.false_button.grid(column=1, row=2)

    # UPDATE METHODS
    def update_canvas_with_answer(self, answer_is_correct):
        if answer_is_correct:
            self.canvas.config(bg=self.COLOR_GREEN)
        else:
            self.canvas.config(bg=self.COLOR_RED)

    def update_canvas_with_next_question(self, question):
        self.canvas.config(bg=self.COLOR_WHITE)
        self.canvas.itemconfig(self.canvas_text, text=question)

    def update_canvas_to_game_over(self):
        self.canvas.config(bg=self.COLOR_WHITE)
        self.canvas.itemconfig(self.canvas_text, text="Quiz over")

    def update_score_label(self):
        self.score_label.config(text=f"Score: {self.quiz.score}")

    # BUTTONS
    def enable_buttons(self):
        self.true_button.config(state="normal")
        self.false_button.config(state="normal")

    def disable_buttons(self):
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")

    # EVENTS
    def _true_button_clicked(self):
        self.update_canvas_with_answer(self.quiz.check_answer("True"))
        self.disable_buttons()
        self.after(1000, self.go_to_next_question)

    def _false_button_clicked(self):
        self.update_canvas_with_answer(self.quiz.check_answer("False"))
        self.disable_buttons()
        self.after(1000, self.go_to_next_question)

    # QUESTION METHODS
    def go_to_next_question(self):
        if self.quiz.still_has_questions():
            question = self.quiz.get_question()

            self.update_canvas_with_next_question(question)
            self.update_score_label()
            self.enable_buttons()
        else:
            self.update_canvas_to_game_over()
            self.disable_buttons()
