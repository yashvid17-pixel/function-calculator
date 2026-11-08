def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

# This starts the program automatically when you run the file
print("=== Function Calculator ===")
print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")

while True:
    try:
        choice = input("\nChoose an operation (1-5): ").strip()
        
        if choice == '5':
            print("Exiting calculator.")
            break
            
        if choice not in ['1', '2', '3', '4']:
            print("Invalid selection. Please choose 1-5.")
            continue

        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))

        if choice == '1':
            print(f"Result: {add(first_number, second_number)}")
        elif choice == '2':
            print(f"Result: {subtract(first_number, second_number)}")
        elif choice == '3':
            print(f"Result: {multiply(first_number, second_number)}")
        elif choice == '4':
            try:
                print(f"Result: {divide(first_number, second_number)}")
            except ZeroDivisionError:
                print("Error: Cannot divide by zero.")

    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
