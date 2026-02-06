a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
def greatest(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c


print("Greatest number =", greatest(a, b, c))
