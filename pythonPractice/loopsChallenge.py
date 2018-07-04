list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


print("enter q to quit")
while True:
    resp = input("guess a number between 1 and 10: ")
    try:
        resp = int(resp)
        if resp in list:
            print("correct")
        else:
            print("try again")
            
    except(ValueError):
        if resp == "q":
            break
        else:
            print("try again")
