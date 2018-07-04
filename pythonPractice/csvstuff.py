import csv

list1 = ["top gun", "risky business", "minority report"]
list2 = ["titanic", "the revenant", "inception"]
list3 = ["training day", "man on fire", "flight"]

allList = [list1, list2, list3]

print(allList)


listy = [['top gun', 'risky business', 'minority report'],
         ['titanic', 'the revenant', 'inception'],
         ['training day', 'man on fire', 'flight']]

with open("yo.csv", "w", newline='') as f:
          w = csv.writer(f, delimiter=",")
          w.writerow(listy[1])
          w.writerow(listy[2])
          w.writerow(listy[0])
