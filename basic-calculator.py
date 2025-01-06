num1=int(input())
num2=int(input())
op=input()
if op=='+':
    print(num1+num2)
elif op=='-':
    print(num1-num2)
elif op=='*':
    print(num1*num2)
elif op=='/':
    print(num1/num2)
elif op=='%':
    print(num1%num2)
else:
    print("Enter valid operator!")
