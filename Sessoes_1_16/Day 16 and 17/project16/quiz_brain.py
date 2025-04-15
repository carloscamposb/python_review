class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list) #return true

    def next_question(self):
        current_question = self.question_list[self.question_number]
        answer_user = input(f"Q.{self.question_number + 1}: {current_question.text_q} (True/False)? ")
        self.question_number += 1
        self.check_answer(answer_user, current_question.answer_q)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right! ✅")
            
        else:
            print("That's wrong. ❌")
        print(f"The correct answer is: {correct_answer}")
        print(f"Your current score is: {self.score} | Question Number: {self.question_number+1}\n")
        print(f"\n")
