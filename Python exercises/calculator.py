# simple calculator ->user input

a = int(input("Enter first numbers:"))
b = int(input("Enter second numbers:"))
operator = input("Enter an operator(+,-,*,/):")
match operator:
    case '+':
        sum = a+b
        print(f"Your sum is:{sum}")
    case '-':
        sub = a-b
        print(f"Your subtraction is:{sub}")
    case '*':
        mul = a*b
        print(f"Your multiplicaton is:{mul}")
    case '/':
        div = a/b
        print(f"Your division is:{div}")
    
    case '':
        print("Invalid input!! Please Try again")