# Program to calculate airfare:

Fullprice = int(5000)
FrequentFlyer = True

print(f"Flight Ticket Price of single person is:{Fullprice}")
number = int(input("Enter total numbers of ticket to book:"))
totalPrice = number*Fullprice
print(f"Your total is:{totalPrice}")

# promocode
PromoCode = input("Enter Promode:")
if(PromoCode == "first flight"):
    newPrice =totalPrice - totalPrice*(20/100)
    print(f"Your total is{newPrice}")
elif(PromoCode==""):
    print(f"Your total is{totalPrice}")
else:
    print("Invalid Promocode!!")
# luggage weight
luggageWeight = int(input("Enter your luggage weight(kg):"))
if(luggageWeight<=20):
    print("You are good to go!!")
elif(luggageWeight>20 and PromoCode=="first flight"):
    print("You have extra weight.Fine amount is Rs.100 per kg")
    fine = (luggageWeight-20)*100
    print(f"SO your fine amount is:{fine}")
    newPrice += fine
    print(f"Your total is:{newPrice}")
elif(luggageWeight>20 and PromoCode==""):
    print("You have extra weight.Fine amount is Rs.100 per kg")
    fine = (luggageWeight-20)*100
    print(f"SO your fine amount is:{fine}")
    totalPrice += fine
    print(f"Your total is:{totalPrice}")
else:
    print("Invalid number!!")

