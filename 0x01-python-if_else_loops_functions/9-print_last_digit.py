#!/usr/bin/python3
def print_last_digit(number):
    # Get the last digit using modulus
    last_digit = number % 10
    print("The last digit of", number, "is", last_digit)

# Example usage:
print_last_digit(123)  # Output: The last digit of 123 is 3
print_last_digit(9876)  # Output: The last digit of 9876 is 6 
