# Write a Python program that reads a floating-point number and then display the right-most digit of the integral part of the number.

# Output:
# Enter a Floating-point Number: 1423.569
# Right-most Number is 3





num=float(input())
num = num//1
print(int(num%10))
