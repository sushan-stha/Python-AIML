# Program to calculate airfare:

Fullprice = int(5000)


print(f"Flight Ticket Price of single person is:{Fullprice}")
number = int(input("Enter total numbers of ticket to book:"))
totalPrice = number*Fullprice
print(f"Your total is:{totalPrice}")

# frequent flyer club
FrequentFlyer = input("Are you a frequent flyer?").lower()
if(FrequentFlyer=="yes"):
    discount = totalPrice-totalPrice*(20/100)
    print(f"You've got 20percent off!.Your new total is:{discount}")
else:
    print(f"Your total is:{totalPrice}")

# promocode
PromoCode = input("Enter Promode:")
if(PromoCode == "first flight" and FrequentFlyer=="yes"):
    newPrice =discount - discount*(20/100)
    print(f"Your total is{newPrice}")
elif(PromoCode=="" and FrequentFlyer=="yes"):
    print(f"Your total is{discount}")
if(PromoCode == "first flight" and FrequentFlyer=="no"):
    newPrice = totalPrice - totalPrice*(20/100)
    print(f"Your total is{newPrice}")
elif(PromoCode=="" and FrequentFlyer=="no"):
    print(f"Your total is{totalPrice}")

# luggage weight
luggageWeight = int(input("Enter your luggage weight(kg):"))
if(luggageWeight<=20):
    print("You are good to go!!")
elif(luggageWeight>20 and PromoCode=="first flight"):
    extraWeight = luggageWeight-20
    print(f"You have {extraWeight}kg more weight.So, fine amount is Rs.100 per kg")
    fine = (luggageWeight-20)*100
    print(f"SO your fine amount is:{fine}")
elif(luggageWeight>20 and PromoCode==""):
    extraWeight = luggageWeight-20
    print(f"You have {extraWeight}kg more weight.So, fine amount is Rs.100 per kg")
    fine = (luggageWeight-20)*100
    print(f"SO your fine amount is:{fine}")
else:
    print("Invalid number!!")

