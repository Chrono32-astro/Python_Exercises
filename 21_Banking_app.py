# Python banking program

# show balance
# deposit
#withdrawal

def show_balance(balance):
    print(f"\nYour balance is: ${balance:.2f}\n")


def deposit_money():
    try:
        amount = float(input("Enter an amount to deposit: $"))
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return 0
        return amount
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return 0


def withdraw_money(balance):
    try:
        amount = float(input("Enter an amount to withdraw: $"))
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return 0
        if amount > balance:
            print("Insufficient balance.")
            return 0
        return amount
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return 0


def main():
    balance = 0.0
    is_running = True

    while is_running:
        print("\n====== Banking Program ======")
        print("1. Show Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit_money()
        elif choice == "3":
            balance -= withdraw_money(balance)
        elif choice == "4":
            is_running = False
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

    print("\nThank you for using the Banking Program!")
    print("Have a nice day!\n")


if __name__ == "__main__":
    main()