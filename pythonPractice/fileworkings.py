import csv

with open("st.csv", "r") as f:
    w = csv.reader(f, delimiter=",")
    for row in w:
        print(",".join(row))
