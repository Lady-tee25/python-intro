from quiz_data import get_questions
import random, datetime

question_bank = get_questions()         # ensure the () is inputed to call out the value

print(question_bank)

random.shuffle(question_bank)
print("=" * 60)
print(" ")
print(question_bank)


questions_only = []
answers_only = []
for question in question_bank:
    print(question[0])

    questions_only.append(question[0])
    print(questions_only)
    answers_only.append(question[1])

print(questions_only)
print(answers_only)

def ask(question):
    response = input(f"{question}: ")
    return response

while True:
    for que in questions_only:
        ans = ask(que)
        

    break

