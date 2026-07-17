# Program to find sum of all numbers between 1-100 that are divisible by 3 and 5 both
num = 0


for i in range(0, 100):
    if(i % 3 == 0 and i % 5 == 0):
        print(i)
        num = num+i


print(f"The sum of numbers is:{num}")
    