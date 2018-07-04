import random
import statistics

listi = []
list2 = []
both = [listi, list2]

for i in range(10000):
    num = random.randint(0, 100)
    if num >= 51:
        list2.append(num)
    else:
        listi.append(num)
for i in both:
    x = statistics.mean(i)
    print(x)
