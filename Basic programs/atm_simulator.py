balance = 0

while True:
    print("-------ATM MENU--------")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Your balance is ₹", balance)

    elif choice == "2":
        amount = int(input("Enter the amount you want to deposit :- "))
        balance = balance + amount
        print("Your new balance is = ", balance)
    
    elif choice == "3":
        amount = int(input("Enter the amount you want to withdraw :- "))
        if amount > balance:
            print("Insufficient Balance")
        else:
            balance = balance - amount
            print("Your new balance is = ", balance)

    elif choice == "4":
        print("Thanks for using the ATM")
        break

    else:
        print("Invalid choice. Please try again.")