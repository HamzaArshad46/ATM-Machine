correct_pin = 1234
balance = 5000.00

print("=" * 30)
print("Welcome to Python ATM Machine")
print("=" * 30)

attempts = 3

while attempts > 0:
    pin = int(input("Enter your pin: "))
    if pin == correct_pin:
        print("\n Login Successful")
        break 
    else: 
        attempts -= 1
        print ("Incorrect Pin...")

        if attempts > 0:
            print(f"\nYou have {attempts} attempts left ")

        else:
            print("Too many incorrect pins!")
            print("Your account is locked....")
            exit()

#ATM Menu

while True:
    print("=" * 30)
    print("ATM MENU")
    print("=" * 30)
    print("1. Show Balance.")
    print("2. Desposit Money.")
    print("3. WithDraw Money.")
    print("4. Exit.")
    print("=" * 30)

    choice = input("Enter your choice: (1,2,3,4): ")

    if choice == "1":
        print(f"Your current balance is {balance:.2f}")

    elif choice == "2":
        try:
            amount = float(input("Enter your amount you want to deposit.."))
            if amount <= 0:
                print("Please enter a positive amount....")
            else: 
                balance += amount
                print(f"{amount:.2f} deposit successfully!")
                print(f"New balance Rs.{balance:.2f}")
        except ValueError:
            print("Please enter a valid number...")

    elif choice == "3":
        try:
            amount = float(input("Enter WithDrawl Amount.."))
            if amount <= 0:
                print("Please Enter a positive amount number...")
            elif amount > balance:
                print("Insufficient Balance!")
            else:
                balance -= amount
                print(f"Please collect your withdrawl amount Rs.{amount:.2f}")
                print(f"Your remaining balance is Rs.{balance:.2f}")
        except ValueError:
            print("Please enter a valid amount number...")

    elif choice == "4":
        print("\n Thank you for using Python ATM Machine.")
        print("Have a great day!")
        break

    else:
        print("Invalid choice. Please enter 1-4")



