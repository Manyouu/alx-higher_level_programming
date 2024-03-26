#!/usr/bin/python3
def islower(c):
    # Check if the character is within the lowercase ASCII range
    return ord('a') <= ord(c) <= ord('z')

# Example usage:
print(islower('a'))  # True
print(islower('A'))  # False
print(islower('z'))  # True
print(islower('Z'))  # False
