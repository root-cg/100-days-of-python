class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        if self.question_number == 12:
            return False
        return True
    
    def check_answer(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            print("You are right")
            self.score += 1
        else:
            print("You are wrong!!")
        print(f"The correct ans is: {correct_ans}")
        print(f"Your current score is: {self.score}/{self.question_number}")


        
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q.{self.question_number }:  {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)