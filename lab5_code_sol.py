# Programmers:  [your name here]
# Course:  CS151, [Instructors name here]
# Due Date: [date assignment is due]
# Programming Assignment:  [number of assignment]
# Problem Statement:  [what problem does your code solve; i.e., calculating inches from centimeters]
# Data In: [what information do you request from the user?]
# Data Out:  [What information do you display for the user?]
# Credits: [Is your code based of an example in the book, in class, or something else?  Reminder: you should never take code from the Internet or another person.]
# Display the purpose of the program

print("Welcome to the ATM program! This program allows you to interact with your account balance.")

# Initialize variables
INITIAL_BALANCE = 1000
current_balance = INITIAL_BALANCE
SENTINEL = 'E'
choice = ''

# Start the loop until the user decides to exit
while choice.upper() != SENTINEL:
    # Display the menu
    print("\nPlease select an option:"
          "\n\t D - Deposit"
          "\n\t W - Withdraw"
          "\n\t V - View Balance"
          "\n\t E - Exit")

    choice = input("Your choice: ").strip().upper()

    # Process the choice
    if choice == 'D':
        deposit_amount = input("Enter the amount to deposit: ").strip()

        if deposit_amount.isdigit():
            deposit_amount = int(deposit_amount)

            if deposit_amount < 0:
                print("Error: Please enter a positive number.")
            else:
                current_balance += deposit_amount
                print(f"Deposit successful! Your new balance is ${current_balance:.2f}.")
        else:
            print("Error: Please enter a valid number.")

    elif choice == 'V':
        # Clear the screen and show the balance
        print(f"Your current balance is ${current_balance:.2f}.")

    elif choice == 'W':
        withdraw_amount = input("Enter the amount to withdraw: ").strip()

        if withdraw_amount.isdigit():
            withdraw_amount = int(withdraw_amount)

            if withdraw_amount < 0:
                print("Error: Please enter a positive number.")
            else:
                current_balance -= withdraw_amount
                print(f"Withdrawal successful! Your new balance is ${current_balance:.2f}.")

                # Warning if the balance is negative
                if current_balance < 0:
                    print("❕ Warning: You have a negative balance. You will be charged 5% interest.")
        else:
            print("Error: Please enter a valid number.")

    elif choice == 'E':
        print("Thank you for using the ATM program. Goodbye!")
    else:
        print("Error: Invalid choice. Please enter D, W, V, or E.")

print("ATM program has ended.")