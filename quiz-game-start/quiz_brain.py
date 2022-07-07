# TODO: asking the questions
# TODO: checking if the answer was correct
# TODO: checking if we're the end of the quiz


# Create a QuizBrain class
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.current_score = 0

    # This will show the next question on the list.
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)")
        self.check_answer(user_answer, current_question.answer)

    # Create method called still_has_questions()
    # Purpose: to create awhile loop to keep showing the questions until the end.
    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            print("You've completed the quiz")
            print(f"Your final score was: {self.current_score }/{self.question_number}")
            return False

    def check_answer(self, user_ans, curr_question_ans):
        if user_ans.lower() == curr_question_ans.lower():
            print("You got it right!")
            self.current_score += 1
        else:
            print("You got it wrong.")
        print(f"The correct answer was: {curr_question_ans}")
        print(f"Your current score is: {self.current_score }/{self.question_number}")


