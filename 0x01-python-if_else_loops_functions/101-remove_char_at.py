#!/usr/bin/python3
def remove_char_at(s, n):
    # Check if the index is within valid bounds
    if 0 <= n < len(s):
        # Create a new string by excluding the character at position n
        return s[:n] + s[n+1:]
    else:
        # Invalid index, return the original string
        return s

# Example usage:
original_string = "Hello, World!"
position_to_remove = 5
new_string = remove_char_at(original_string, position_to_remove)
print("Original string:", original_string)
print("New string after removing character at position", position_to_remove, ":", new_string) 
