---
layout: page
title: 03 - Control flow
---
***

&nbsp;
## if Statements
***

- The Python `if` statement is used to determine the execution of code based on the evaluation of a Boolean expression.

- If the `if` statement expression evaluates to `True`, then the indented code following the statement is executed.

- If the expression evaluates to `False` then the indented code following the `if` statement is skipped and the program executes the next line of code which is indented at the same level as the `if` statement.

    ```python
        # if Statement
        test_value = 100

        if test_value > 1:
            # Expression evaluates to True
            print("This code is executed!")

        if test_value > 1000:
            # Expression evaluates to False
            print("This code is NOT executed!")

        print("Program continues at this point.")
    ```

&nbsp;
## else Statement
***

- The Python `else` statement provides alternate code to execute if the expression in an `if` statement evaluates to `False`.

- The indented code for the `if` statement is executed if the expression evaluates to `True`. The indented code immediately following the `else` is executed only if the expression evaluates to `False`.

- To mark the end of the `else` block, the code must be unindented to the same level as the starting `if` line.

    ```python
        # else Statement

        test_value = 50

        if test_value < 1:
            print("Value is < 1")
        else:
            print("Value is >= 1")

        test_string = "VALID"

        if test_string == "NOT_VALID":
            print("String equals NOT_VALID")
        else:
            print("String equals something else!")
    ```

&nbsp;
## Boolean Values
***

- _Booleans_ are a data type in Python, much like integers, floats, and strings.

- However, booleans only have two values: `True` of `False`. Specifically, these two values are of the `bool` type.

- Since booleans are a data type, creating a variable that holds a boolean value is the same for other data types.

    ```python
        is_true = True
        is_false = False

        print(type(is_true)) #will output: <class 'bool'>
    ```

&nbsp;
## elif Statement
***

- The Python `elif` statement allows for continued checks to be performed after an initial `if` statement.

- An `elif` statement differs from the `else` statement because another expression is provided to be checked just as with the initial `if` statement.

- If the expression is `True` the indented code following the `elif` is executed. If the expression evaluates to `False` the code can continue to an optional `else` statement.

- Multiple `elif` statements can be used following an initial `if` to perform a series of checks. Once an `elif` expression evaluates to `True` no further `elif` statements are executed.

    ```python
        # elif Statement
        pet_type = "fish"

        if pet_type == "dog":
            print("You have a dog.")
        elif pet_type == "cat":
            print("You have a cat.")
        elif pet_type == "fish":
            print("You have a fish")
        else:
            print("Not sure!")
    ```

&nbsp;
## Handling exceptions in Python
***

- A `try` and `except` block can be used to handle error in code block. Code which may raise an error can be written in the `try` block .

- During execution, if that code block raises an error, the rest of the `try` block will cease executing and the `except` block code will execute.

    ```python
        def check_leap_year(year):
            is_leap_year = False
            if year%4 == 0:
                is_leap_year = True

        try:
            check_leap_year(2018)
            print(is_leap_year) #The variable is_leap_year is declared inside the function.
        except:
            print('Your code raised an error!')
    ```