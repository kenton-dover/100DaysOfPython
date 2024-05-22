class QuizBrain:
    def __init__(self, questions: list):
        self.question_number = 0
        self.questions = questions
        self.score = 0
        
    def next_question(self):
        current_question = self.questions[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number} : {current_question.text} (True/False)")
        if answer == current_question.answer:
            self.score += 1