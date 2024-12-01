import math

def calculator():
    print("Welcome to the Python Calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square")
    print("6. Square Root")
    
    while True:
        # Take input from the user
        choice = input("\nEnter the number corresponding to your choice (1-6): ")

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                if choice == '1':
                    print(f"The result is: {num1 + num2}")
                elif choice == '2':
                    print(f"The result is: {num1 - num2}")
                elif choice == '3':
                    print(f"The result is: {num1 * num2}")
                elif choice == '4':
                    if num2 != 0:
                        print(f"The result is: {num1 / num2}")
                    else:
                        print("Error: Division by zero is not allowed.")
            except ValueError:
                print("Error: Invalid input. Please enter numeric values.")

        elif choice == '5':
            try:
                num = float(input("Enter the number to square: "))
                print(f"The square of {num} is {num ** 2}")
            except ValueError:
                print("Error: Invalid input. Please enter a numeric value.")

        elif choice == '6':
            try:
                num = float(input("Enter the number to find the square root of: "))
                if num >= 0:
                    print(f"The square root of {num} is {math.sqrt(num)}")
                else:
                    print("Error: Cannot calculate the square root of a negative number.")
            except ValueError:
                print("Error: Invalid input. Please enter a numeric value.")

        else:
            print("Invalid choice. Please select a valid operation (1-6).")

        # Check if the user wants to perform another calculation
        next_calculation = input("\nDo you want to perform another calculation? (yes/no): ").lower()
        if next_calculation != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    calculator()
