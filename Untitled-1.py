# Simple Calculator in Python

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    try:
        choice = int(input("Enter your choice (1/2/3/4): "))
        if choice in [1, 2, 3, 4]:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            if choice == 1:
                print(f"The result is: {add(num1, num2)}")
            elif choice == 2:
                print(f"The result is: {subtract(num1, num2)}")
            elif choice == 3:
                print(f"The result is: {multiply(num1, num2)}")
            elif choice == 4:
                print(f"The result is: {divide(num1, num2)}")
        else:
            print("Invalid choice. Please choose a valid operation.")
    except ValueError:
        print("Invalid input. Please enter numbers only.")
    
    # Ask the user if they want to perform another calculation
    again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
    if again == 'yes':
        calculator()
    else:
        print("Goodbye!")

# Run the calculator
calculator()
