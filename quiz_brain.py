class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

        
    def next_question(self):
        current_question =  self.question_list[self.question_number].text
        correct_answer = self.question_list[self.question_number].answer
        user_answer = input(f"Q{self.question_number+1}. {current_question} (True/False)? :")
        self.question_number += 1
        self.check_answer(user_answer,correct_answer)  
        print("\n")

    def still_has_question(self):
        return len(self.question_list) > self.question_number

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower()==correct_answer.lower():
            print(f"Thats Correct! The correct Answer is {correct_answer}")
            self.score += 1   
        else:
            print(f"Sorry That is Incorrect! The Correct Answer is {correct_answer}")     
        print(f"Your Current Score is :{self.score}/{self.question_number}")    