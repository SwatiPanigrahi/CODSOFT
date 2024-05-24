def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
def main():
    print('Simple Calculator')
    print('Select Operation')
    print('1. Add')
    print('2. Subtract')
    print('3. Multiply')
    print('4. Divide')
    print('5. Exit')
choice = int(input("Enter your choice"))
if choice == 1:
    print('Sum =',num1+num2)
elif choice == 2:
    print('Difference=',num1-num2)
elif choice == 3:
    print('Product=',num1*num2)
elif choice == 4:
    print('Quotient=',num1/num2)
elif choice == 5:
        print('Exit')
else:
    print('Invalid choice! Please select a valid operation')
