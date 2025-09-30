"""Interactive demo CLI (not graded)."""
from calculator import add, subtract, multiply, divide

def main():
    """Run the interactive command-line calculator."""
    print("TinyTools Calculator (add/subtract/multiply/divide)")
    op = input("Operation: ").strip().lower()
    a = float(input("First number: "))
    b = float(input("Second number: "))

    if op == "add":
        print(add(a, b))
    elif op == "subtract":
        print(subtract(a, b))
    elif op == "multiply":
        print(multiply(a, b))
    elif op == "divide":
        try:
            print(divide(a, b))
        except ZeroDivisionError as e:
            print(f"Error: {e}")
    else:
        print("Unknown op")

if __name__ == "__main__":
    main()
