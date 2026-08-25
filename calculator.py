#!/usr/bin/env python3
"""
A simple command-line calculator written in Python.
Supports basic arithmetic operations: addition, subtraction,
multiplication, and division.
"""


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return the quotient of a divided by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def main():
    print("===== Python Calculator =====")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter your choice (1/2/3/4): ").strip()

    if choice not in ("1", "2", "3", "4"):
        print("Invalid choice. Please run again and select 1-4.")
        return

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    if choice == "1":
        result = add(num1, num2)
        op = "+"
    elif choice == "2":
        result = subtract(num1, num2)
        op = "-"
    elif choice == "3":
        result = multiply(num1, num2)
        op = "*"
    elif choice == "4":
        try:
            result = divide(num1, num2)
        except ValueError as err:
            print(f"Error: {err}")
            return
        op = "/"

    print(f"\nResult: {num1} {op} {num2} = {result}")
    print("============================")


if __name__ == "__main__":
    main()
