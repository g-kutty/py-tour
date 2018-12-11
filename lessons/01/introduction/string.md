---
layout: page
title:
---
***

## Strings
***

- Computer programmers refer to blocks of text as strings.

- In Python a string is either surrounded by double quotes (`"Hello world"`) or single quotes (`'Hello world'`). It doesn't matter which kind you use, just be consistent.

&nbsp;
## Concatenation
***

- The `+` operator doesn't just add two numbers, it can also "add" two strings! The process of combining two strings is called _string concatenation_.

- Performing string concatenation creates a brand new string comprised of the first string's contents followed by the second string's contents (without any added space in-between).

    ```python
        greeting_text = "Hey there!"
        question_text = "How are you doing?"
        full_text = greeting_text + question_text

        # Prints "Hey there!How are you doing?"
        print(full_text)
    ```

- In this sample of code, we create two variables that hold strings and then concatenate them.

- But we notice that the result was missing a space between the two, let's add the space in-between using the same concatenation operator!

    ```python
        full_text = greeting_text + " " + question_text

        # Prints "Hey there! How are you doing?"
        print(full_text)
    ```

- Now the code prints the message we expected.

- If you want to concatenate a string with a number you will need to make the number a string first, using the `str()` function.

- If you're trying to `print()` a numeric variable you can use commas to pass it as a different argument rather than converting it to a string.

    ```python
        birthday_string = "I am "
        age = 10
        birthday_string_2 = " years old today!"

        # Concatenating an integer with strings is possible if we turn the integer into a string first
        full_birthday_string = birthday_string + str(age) + birthday_string_2

        # Prints "I am 10 years old today!"
        print(full_birthday_string)
    ```

- Using `str()` we can convert variables that are not strings to strings and then concatenate them.

- But we don't need to convert a number to a string for it to be an argument to a print statement.

&nbsp;
## Multi-line Strings
***

- Python strings are very flexible, but if we try to create a string that occupies multiple lines we find ourselves face-to-face with a `SyntaxError`.

- Python offers a solution: _multi-line strings_. By using three quote-marks (`"""` or `'''`) instead of one, we tell the program that the string doesn't end until the next triple-quote.

- This method is useful if the string being defined contains a lot of quotation marks and we want to be sure we don't close it prematurely.

    ```python
        leaves_of_grass = """
        Poets to come! orators, singers, musicians to come!
        Not to-day is to justify me and answer what I am for,
        But you, a new brood, native, athletic, continental, greater than
        before known,
        Arouse! for you must justify me.
        """
    ```

- In the above example, we assign a famous poet's words to a variable. Even though the quote contains multiple linebreaks, the code works!

- If a multi-line string isn't assigned a variable or used in an expression it is treated as a comment.