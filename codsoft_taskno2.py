#Task 2 calculate codsoft 

def display_menu():
    print("\nPlease choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    

def get_operation_choice():
    while True:
        choice = input("\nEnter your choice (1-5): ").strip()
        if choice in ['1', '2', '3', '4', '5']:
            return choice
        else:
            print("❌ Invalid choice! Please enter a number between 1 and 5.")

def get_number(prompt):
    while True:
        try:
            number = float(input(prompt).strip())
            return number
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

def main():
    print("Welcome to the Simple Calculator!")
    
    while True:
        display_menu()
        choice = get_operation_choice()

        if choice == '5':
            print("Thank you for using the Simple Calculator! Goodbye!")
            break

        print("Enter the two numbers\n")
        
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        if choice == '1':
            result = num1 + num2
            print(f"The result of {num1} + {num2} is {result}")
        elif choice == '2':
            result = num1 - num2
            print(f"The result of {num1} - {num2} is {result}")
        elif choice == '3':
            result = num1 * num2
            print(f"The result of {num1} * {num2} is {result}")
        elif choice == '4':
            if num2 == 0:
                print("❌ Error! Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"The result of {num1} / {num2} is {result}")

if __name__ == "__main__":
    main()
