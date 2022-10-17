from data import question_data
from question_model import Ques
from quiz_brain import QuizBrain

ques_bank = []
for i in question_data:

    new_q = Ques(i["text"], i["answer"])
    ques_bank.append(new_q)


quiz = QuizBrain(ques_bank)
while quiz.still_q():
    quiz.next_q()
print(f"Your quiz has been ended,\n {quiz.score}/{quiz.q_no}")