from question import Question
from question_bank import QuestionBank
from data_manager import DataManager
from quiz import Quiz
from ui import UI


class App:
    def __init__(self):
        question_bank = QuestionBank(DataManager(10), Question).generate()
        quiz = Quiz(question_bank)

        self.ui = UI(quiz)

    # PUBLIC METHODS
    def start(self):
        self.ui.go_to_next_question()
        self.ui.mainloop()
