def check_password(text):
    c = 0  
    cd = 0  
    d = 0  
    
    if len(text) <= 5:
        print("Invalid")
        return
    
    for char in text:
        if 'a' <= char <= 'z':
            c += 1
        elif 'A' <= char <= 'Z':
            cd += 1
        elif char.isdigit():
            d += 1
    
    if c == len(text):
        print("Weak")
    elif cd > 0 and d > 0:
        print("Medium")
    else:
        print("Strong")

check_password(user_input)
