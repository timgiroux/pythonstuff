string = ""
list = []


for i in range(30):
    s = str(i)
    list.append(s)
    for x in ["a", "b", "c"]:
        list.append(x)

for d in range (24):
    string = string + list[d]

print(string)

