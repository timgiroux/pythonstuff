f = input("Enter first number: ")
operation = input("Enter operation: ")
s = input("Enter second number: ")

fnum = int(f)
snum = int(s)

if operation == "plus":
    print(fnum + snum)
elif operation == "minus":
    print(fnum - snum)
elif operation == "times":
    print(fnum * snum)
else:
    print("INVALID OPERATION")
