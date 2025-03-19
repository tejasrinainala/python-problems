n = input("Enter a string: ")
m = ""

for i in range(len(n)):
    if n[i].isnumeric():
        m += n[i]
        # If it's the last character or the next character is not a digit, print `m`
        if i == len(n) - 1 or not n[i + 1].isnumeric():
            print(m)
            m = ""
