# ATM Vault Simulator

balance = 10000

while True:
    print("\n---- Welcome to Python ATM ----")
    print("1. Check Balance")
    print("2. Deposit Funds")
    print("3. Withdraw Funds")
    print("4. Exit")

    try:
        user_choice = int(input("Enter your choice (1-4): "))
    except ValueError:
        print("Please enter numbers only!")
        continue

    match user_choice:
        case 1:
            print(f"Current Balance: Rs.{balance:.2f}")

        case 2:
            deposit = float(input("Enter amount to deposit: "))
            balance += deposit
            print(f"New Balance: Rs.{balance:.2f}")

        case 3:
            withdraw = float(input("Enter amount to withdraw: "))
            if withdraw > balance:
                print("Insufficient Balance!")
            else:
                balance -= withdraw
                print(f"Remaining Balance: Rs.{balance:.2f}")

        case 4:
            print("Thank you for choosing us!")
            break

        case _:
            print("Invalid Choice!")