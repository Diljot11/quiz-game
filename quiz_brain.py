class QuizBrain:

    def __init__(self, q_list):
        self.q_no=0
        self.ques_list=q_list
        self.score=0
    # def quiz1(self):
    #     while self.still_q():
    #         ans=self.next_q()
    #         if ans==(self.ques_list[self.q_no]).ans:
    #             print('yeahhh right')


    def still_q(self):
        return self.q_no<len(self.ques_list)
# return True

    def next_q(self):
        q = self.ques_list[self.q_no]
        self.q_no+=1
        ans=input(f"Q.{self.q_no}: {q.text}. (True/False)? :")
        cor_ans=q.ans
        self.check_ans(ans, cor_ans)

        # return ans
    def check_ans(self, ans, cor_ans):

        if ans.lower()==cor_ans.lower():
            self.score+=1
            print("you are right!!")
        else:
            print("that's wrong")

        print(f"the correct ans is {cor_ans}.\n Your score is:  {self.score}/{self.q_no}\n")






















