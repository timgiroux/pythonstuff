import random
sent = ["Fuck {}.", "Marry {}.", "Kill {}."]
answers = []
ques = ["Enter your hottest teacher: ",
        "Enter an ex girlfriend: ",
        "Enter another ex girlfriend: "]

        
for i in range(3):
    ans = input(ques[i])
    answers.append(ans)

for i in range(0, 3):
    if i == 0:
        global randy
        randy = random.randint(1, 3)
    x = sent[i].format(answers[randy - i])
    print(x)
