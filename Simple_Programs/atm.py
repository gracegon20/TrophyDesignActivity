import sys
#This is an ATM Machine
print("Welcome to this ATM Machine")
user_pin = 1234


#Function for Atm
def main_menu():
        global balance
        balance = 1500
        while True:
            user_pin = int(input("Please enter your PIN: "))
            if user_pin == 1234:
                def menu():
                    print("1. Check Balance")
                    print("2. Deposit Money")
                    print("3. Withdraw Money")
                    print("4. Exit")
            
                while True:
                    menu()
                    choice = int(input("Please select an option: "))

                    if choice == 1:
                            print(f"Your current balance is: ₱{balance:.2f}")
                    elif choice == 2:
                        print("Deposit Money")
                        amount = float(input("Enter amount to deposit: "))
                        balance += amount
                        print(f"Deposited ₱{amount:.2f}. New balance is: ₱{balance:.2f}")
                    elif choice == 3:
                        print("Withdraw Money")
                        amount = float(input("Enter amount to withdraw: "))
                        if amount > balance:
                            print("Insufficient funds.")
                        else:
                            balance -= amount
                            print(f"Withdrew ₱{amount:.2f}. New balance is: ₱{balance:.2f}")
                    elif choice == 4:
                        print("Thank you for using the ATM. Goodbye!")
                        sys.exit()
                    else:
                        print("Invalid option. Please try again.")
            else:
                print("Incorrect PIN. Please try again.")
main_menu()
