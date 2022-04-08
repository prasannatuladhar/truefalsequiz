from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question['question']
    question_answer = question['correct_answer']
    question = Question(question_text,question_answer)
    question_bank.append(question)

quiz_brain = QuizBrain(question_bank)
while quiz_brain.still_has_question():
    quiz_brain.next_question()

print(f"Your Final Score is : {quiz_brain.score}/{quiz_brain.question_number}")    