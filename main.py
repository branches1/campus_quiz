from question_model import Question
from data import question_data, passionate_question_data
from quiz_brain import QuizBrain

question_bank = []  # A list of question objects.
for question in passionate_question_data:  # CHANGE QUESTION SOURCE HERE

    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(q_text=question_text, answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You have finished the quiz. Woop.")
print(f"You final score was: {quiz.score}/{quiz.question_number}")
