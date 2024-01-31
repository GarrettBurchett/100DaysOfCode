class QuizBrain:

    def __init__(self, questions: list):
        self.question_number = 0
        self.questions_list = questions
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)
    
    def next_question(self):
        question = self.questions_list[self.question_number]
        self.question_number += 1
        guess = input(f"Q.{self.question_number}: {question.text}. (True/False)?: ").title()
        self.check_answer(guess, question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}.\n")