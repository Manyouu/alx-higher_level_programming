0x09. Python - Everything is object

General
Why Python programming is awesome
What is an object
What is the difference between a class and an object or instance
What is the difference between immutable object and mutable object
What is a reference
What is an assignment
What is an alias
How to know if two variables are identical
How to know if two variables are linked to the same object
How to display the variable identifier (which is the memory address in the CPython implementation)
What is mutable and immutable
What are the built-in mutable types
What are the built-in immutable types
How does Python pass variables to functions

Python Scripts
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a newline character
The first line of all your script files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle (version 2.8.*)
All your files must be executable
The length of your files will be tested using wc

.txt Answer Files
Only one line
No Shebang
All your files should end with a new line

Tasks

0. Who am I?

What function would you use to get the type of an object?

Write the name of the function in the file, without ()

1. Where are you?

How do you get the variable identifier (which is the memory address in the CPython implementation)?

Write the name of the function in the file, without ().

2. Right count

In the following code, do a and b point to the same object? Answer with Yes or No

3. Right count =

In the following code, do a and b point to the same object? Answer with Yes or No.

4. Right count =

In the following code, do a and b point to the same object? Answer with Yes or No.

5. Right count =+

In the following code, do a and b point to the same object? Answer with Yes or No.

6. Is equal

What do these 3 lines print?

7. Is the same

What do these 3 lines print?

8. Is really equal

What do these 3 lines print?

9. Is really the same

What do these 3 lines print?

10. And with a list, is it equal

What do these 3 lines print?

11. And with a list, is it the same

What do these 3 lines print?

12. And with a list, is it really equal

What do these 3 lines print?

13. And with a list, is it really the same

What do these 3 lines print?

14. List append

What does this script print?

15. List add

What does this script print?

16. Integer incrementation

What does this script print?

17. List incrementation

What does this script print?

18. List assignation

What does this script print?

19. Copy a list object

Write a function def copy_list(l): that returns a copy of a list.

The input list can contain any type of objects
Your file should be maximum 3-line long (no documentation needed)
You are not allowed to import any module

20. Tuple or not?

Is a a tuple? Answer with Yes or No

21. Tuple or not?

Is a a tuple? Answer with Yes or No.

22. Tuple or not?

Is a a tuple? Answer with Yes or No.

23. Tuple or not?

Is a a tuple? Answer with Yes or No

24. Who I am?

What does this script print?

25. Tuple or not

What does this script print?

26. Empty is not empty

What does this script print?

27. Still the same?

Will the last line of this script print 139926795932424? Answer with Yes or No.

28. Same or not?

Will the last line of this script print 139926795932424? Answer with Yes or No

29. #pythonic

Write a function magic_string() that returns a string “BestSchool” n times the number of the iteration (see code):

Format: see example
Your file should be maximum 4-line long (no documentation needed)
You are not allowed to import any module

30. Low memory cost

Write a class LockedClass with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called first_name.

You are not allowed to import any module

31. int 1/3

Assuming we are using a CPython implementation of Python3 with default options/configuration:

How many int objects are created by the execution of the first line of the script? (103-line1.txt)
How many int objects are created by the execution of the second line of the script (103-line2.txt)

32. int 2/3

Assuming we are using a CPython implementation of Python3 with default options/configuration:

How many int objects are created by the execution of the first line of the script? (104-line1.txt)
How many int objects are created by the execution of the second line of the script (104-line2.txt)
After the execution of line 3, is the int object pointed by a deleted? Answer with Yes or No (104-line3.txt)
After the execution of line 4, is the int object pointed by b deleted? Answer with Yes or No (104-line4.txt)
How many int objects are created by the execution of the last line of the script (104-line5.txt)

33. int 3/3

Assuming we are using a CPython implementation of Python3 with default options/configuration:

Before the execution of line 2 (print("Love")), how many int objects have been created and are still in memory? (105-line1.txt)
Why? (optional blog post :))

34. Clear strings

Assuming we are using a CPython implementation of Python3 with default options/configuration (For answers with numbers use integers, don’t spell out the word):

How many string objects are created by the execution of the first line of the script? (106-line1.txt)
How many string objects are created by the execution of the second line of the script (106-line2.txt)
After the execution of line 3, is the string object pointed by a deleted? Answer with Yes or No (106-line3.txt)
After the execution of line 4, is the string object pointed by b deleted? Answer with Yes or No (106-line4.txt)
How many string objects are created by the execution of the last line of the script (106-line5.txt)
