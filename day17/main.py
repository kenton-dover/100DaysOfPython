
from question_model import QuestionModel
from quiz_brain import QuizBrain



def load_questions():
    question_bank = []
    from data import question_data
    for question in question_data:
        question_bank.append(QuestionModel(question["text"], question["answer"]))
    return question_bank

question_bank = load_questions()
        
quiz = QuizBrain(question_bank)


for i in range(len(question_bank)):
    quiz.next_question()

print(f"You got {quiz.score} out of {len(question_bank)}")