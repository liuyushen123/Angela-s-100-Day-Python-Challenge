class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list
    
    def get_question(self):
        return self.question_list[self.question_number]
    
    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer):
        if (self.get_question().answer == user_answer):
            self.score += 1
            print("That is correct!")
        else:
            print("Bitch you got it wrong!")
        print("The correct answer was: " + self.get_question().answer)
        print(f"Your current score is {self.score}/{self.question_number+1}")
        self.question_number += 1