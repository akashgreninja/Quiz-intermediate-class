class QuizBrain:





    def __init__(self,q_list):
        self.question_number=0
        self.question_list=q_list
        self.score=0

    def end_of_quiz(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number += 1
        user_answer=input(f"{self.question_number} {current_question.text}")
        self.check_answer(user_answer,current_question)


    def check_answer(self,user_answer,current_question):
        if user_answer.lower() == current_question.answer.lower():
            self.score += 1
            print("correct")

        else:
            print("wrong")
        print(f"the correct answer is {current_question.answer}")
        print(f"your score is {self.score}/{self.question_number}")





