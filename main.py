import json
data = open('questions.json')
quiz = json.load(data)
# quiz from //https://gist.github.com/cmota/f7919cd962a061126effb2d7118bec72
def run_quiz(questions):
    score = 0
    for question in questions:
        print("Question", questions.index(question) + 1,": ", question['question'], "\n")
        print(f"A:{question['A']}, B:{question['B']}\nC:{question['C']}, D:{question['D']} \n" )
        answer = input('Enter your answer: A, B, C or D: ')
        if answer.upper() == question['answer']:
            score += 1
             
    print (f"You answered {score} out of {len(questions)} questions correctly")
run_quiz(quiz)
input("Press Enter to exit...")