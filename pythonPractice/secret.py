text = input("tell me a secret: ")

with open("st.txt", "w") as f:
    f.write(text)

print("thanks! your privacy is my number one priority")
