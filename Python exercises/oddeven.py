# Program to check if the number is even or odd and within the range or not

num = int(input("Enter a number(0-100):"))

if(num % 2 == 0 and 0<num<=100):
    print(f"{num} is even number and within the range")
elif(num % 2 == 0 and num>100):
    print(f"{num} is even number but out of the required range")
elif(num % 2 != 0 and 0<num<=100):
    print(f"{num} is odd and wihtin the range")
elif(num % 2 != 0 and num>100):
    print(f"{num} is odd and out of the required range")
else:
    print("Invalid input!!!")