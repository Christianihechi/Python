from bank_account_class import BankAccount


def main():
    account_holder = input("Enter account holder name: ")
    account_number = input("Enter account number: ")
    account_balance = int(input("Enter initial balance: "))

    bank_account = BankAccount(account_holder, account_number, account_balance)

    while True:
        print("1. Account Information")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            bank_account.account_info()
        elif choice == "2":
            amount = int(input("Enter deposit amount: "))
            bank_account.deposit(amount)
            print(f"Hi {bank_account.account_holder}! Your account has been credited successfully with: "
                  f"{amount} Naira.\nCurrent Balance: {bank_account.account_balance} Naira")
        elif choice == "3":
            amount = int(input("Enter withdrawal amount: "))
            success = bank_account.withdraw(amount)
            if success:
                bank_name = input("Enter recipient's bank name: ")
                account_no = input("Enter recipient's account number: ")
                print()
                print(f"Your account has been debited with {amount} Naira.\n---Recipients Information---"
                      f"\nBank name: {bank_name.upper()}.\nAccount No: {account_no}."
                      f"\nCurrent Balance: {bank_account.account_balance} Naira")
            else:
                print("Your account balance is insufficient for this transaction, please try again!")
        elif choice == "4":
            print("Exiting program")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
