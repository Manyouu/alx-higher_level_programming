#!/usr/bin/python3
def print_last_digit(number):
    last_digit = abs(number) % 10
    print('{:d}'.format(last_digit), end='')
    return last_digit

# Example usage:
number_to_check = -12345
print_last_digit(number_to_check) 
