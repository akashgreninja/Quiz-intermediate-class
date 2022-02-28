from data import question_data
from  question_model import Quiz
from quiz_brain import QuizBrain





question_bank=[]




for n in question_data:
    question_this=n["text"]
    answer_this=n["answer"]

    wadu=Quiz(question_this,answer_this)
    question_bank.append(wadu)

quiz=QuizBrain(question_bank)

end=False
while end==False:
    quiz.next_question()


