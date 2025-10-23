# src/calculator.py
from src.utils import add, subtract, multiply, divide

def get_input(prompt, is_number=True):
    """Helper to get and validate user input."""
    while True:
        try:
            value = input(prompt).strip()
            if not is_number:
                return value.lower()
            return float(value)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def run_calculator():
    """Main function to run the command-line calculator."""
    operations = {
        '1': ("Add", add),
        '2': ("Subtract", subtract),
        '3': ("Multiply", multiply),
        '4': ("Divide", divide)
    }

    print("--- Simple Python Calculator ---")

    while True:
        print("\nChoose an operation:")
        print("1: Add (+)")
        print("2: Subtract (-)")
        print("3: Multiply (*)")
        print("4: Divide (/)")

        choice = input("Enter choice (1-4): ").strip()
        
        if choice not in operations:
            print("Invalid choice. Please select 1, 2, 3, or 4.")
            continue

        operation_name, func = operations[choice]
        
        try:
            # Use two numbers for simplicity in the main script
            num1 = get_input(f"Enter the first number for {operation_name}: ")
            num2 = get_input(f"Enter the second number for {operation_name}: ")

            if choice in ('1', '2', '3'):
                # For add/subtract/multiply with two numbers
                result = func(num1, num2)
            elif choice == '4':
                # Division handling, which already raises ZeroDivisionError in utils.py
                result = func(num1, num2)
            
            print(f"\nResult: {num1} {choice_to_symbol(choice)} {num2} = {result}")

        except ZeroDivisionError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            
        # Ask for another calculation
        another = get_input("Perform another calculation? (y/n): ", is_number=False)
        if another != 'y':
            print("Thank you for using the calculator. Goodbye!")
            break

def choice_to_symbol(choice):
    """Maps choice to operation symbol."""
    symbols = {'1': '+', '2': '-', '3': '*', '4': '/'}
    return symbols.get(choice, '?')

if __name__ == "__main__":
    # This block allows the script to be run directly: `python src/calculator.py`
    run_calculator()


