from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    # new_question = Question(q_text=question_text, q_answer=question_answer)
    # or do a positional parameter
    # Initialize an object after getting data from a question_data file
    new_question = Question(question_text, question_answer)
    # Insert each object into a list called question_bank.
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
