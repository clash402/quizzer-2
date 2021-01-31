class QuestionBank:
    def __init__(self, data_manager, question):
        self.data_manager = data_manager
        self.question = question

    # PUBLIC METHODS
    def generate(self):
        trivia = self.data_manager.get_trivia()
        question_bank = []

        for item in trivia:
            text = item["question"]
            answer = item["correct_answer"]
            question = self.question(text, answer)
            question_bank.append(question)

        return question_bank
