# import random

# print("Welcome to the rock paper scissor game!!!")
 
# option = ["rock", "paper","scissor"]

# user = input("Choose rock, paper or scissor:").lower()
# computer = random.choice(option)

# print("Computer: ",computer)
# print("User: ",user)

# # user winning case:
# if(user == "paper" and computer == "rock"):
#     print("User win!!")
# elif(user == "scissor" and computer == "paper"):
#     print("User win!!")
# elif(user == "rock" and computer == "scissor"):
#     print("User win!!")

# # computer winning case:
# elif(user == "paper" and computer == "scissor" ):
#     print("Computer win!!")
# elif(user == "scissor" and computer == "rock" ):
#     print("Computer win!!")
# elif(user == "rock" and computer == "paper" ):
#     print("Computer win!!")

# # draw case:
# elif(user == computer):
#     print("Draw!!")

# else:
#     print("Invalid input!!")

# rock-paper-scissor game using while loop
choices = ["rock","paper","scissor"]
count = 0

while True:
    player = input("Enter you choice(rock,paper or scissor):").lower()

    if player not in choices:
        print("Invalid choice")
        continue
    computer =  choices[count%3]
    count += 1

    print("Computer chose:",computer)

    if(player==computer):
        print("Its a tie.")
    elif(player=="rock" and computer=="scissor") or\
        (player=="paper" and computer=="rock") or\
        (player=="scissor" and computer=="paper"):
        print("You win!!")
    else:
        print("Computer win!!")

    again = input("Do you want to play again>(y/n):").lower()
    if(again !="y"):
        print("Game Over mate!!")
        break
