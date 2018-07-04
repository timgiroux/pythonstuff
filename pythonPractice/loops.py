questions = ["Whats your name?",
             "Favorite Color?",
             "whats your quest?",
             "press q to quit"]
sent = ["Your name is {}.", "Your favorite color is {}.", "Your quest is {}."]
answers = []
n = 0

while True:
    a = input(questions[n])
    if a == "q":
        break
    else:
        answers.append(a)
    n = (n+1) % 4


for i in range(0, 3):
    x = sent[i].format(answers[i])
    print(x)

