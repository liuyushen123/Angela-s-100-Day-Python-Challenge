from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# "question data" is a list of dictionaries
# Each dictionary contain key of q_text and q_answer


def get_questions(a_list):
    for i in question_data:
        a_list.append(Question(i["text"], i["answer"]))
    return a_list


quizBrainObj = QuizBrain(get_questions([]))

while quizBrainObj.still_has_question():
    user_choice = input(
        f"Q.{quizBrainObj.question_number + 1} {quizBrainObj.get_question().question_text} (True/False): "
    )
    quizBrainObj.check_answer(user_choice)
    print("\n" * 2)
