---
layout: page
title: Control flow
---
***

- Just like in real life, sometimes we'd like our code to be able to make decisions.

- __Control flow__ gives us this ability to choose among outcomes based on what else is happening in the program.

&nbsp;

## Compare Closely

***

- Let's start with the simplest aspect of control flow: __comparators__. There are six:

  - Equal to (`==`)

    ```python
        >>> 2 == 2
        True
        >>> 2 == 5
        False
    ```

  - Not equal to (`!=`)

    ```python
        >>> 2 != 5
        True
        >>> 2 != 2
        False
    ```

  - Less than (`<`)

    ```python
        >>> 2 < 5
        True
        >>> 5 < 2
        False
    ```

  - Less than or equal to (`<=`)

    ```python
        >>> 2 <= 2
        True
        >>> 5 <= 2
        False
    ```

  - Greater than (`>`)

    ```python
        >>> 5 > 2
        True
        >>> 2 > 5
        False
    ```

  - Greater than or equal to (`>=`)

    ```python
        >>> 5 >= 5
        True
        >>> 2 >= 5
        False
    ```

&nbsp;

## To Be and/or Not to Be

***

- __Boolean operators__ compare statements and result in boolean values. There are three boolean operators:

  1. `and`, which checks if both the statements are `True`.

        ```python
            1 < 2 and 2 < 3 is True
            1 < 2 and 2 > 3 is False
        ```
  
  2. `or`, which checks if at least one of the statements is `True`.

        ```python
            1 < 2 or 2 > 3 is True
            1 > 2 or 2 > 3 is False
        ```

  3. `not`, which gives the opposite of the statement.

- Boolean operators aren't just evaluated from left to right. Just like with arithmetic operators, there's an order of operations for boolean operators:

  1. `not` is evaluated first
  2. `and` is evaluated next
  3. `or` is evaluated last

- Parentheses () ensure your expressions are evaluated in the order you want.

&nbsp;

## Conditional Statement Syntax

***

- `if` is a conditional statement that executes some specified code after checking if its expression is `True`.

  ```python
    if 8 < 9:
        print "Eight is less than nine!"
  ```

- Pay attention to the indentation before the `print` statement. This space, called `white space`, is how Python knows we are entering a new block of code.

- Python accepts many different kinds of indentation to indicate blocks. In this lesson, we use four spaces but elsewhere you might encounter two-space indentation or tabs (which Python will see as different from spaces).

- If the indentation from one line to the next is different and there is no command (like `if`) that indicates an incoming block then Python will raise an `IndentationError`.

- These errors could mean, for example, that one line had two spaces but the next one had three. Python tries to indicate where this error happened by printing the line of code it couldn't parse and using a `^` to point to where the indentation was different from what it expected.

- Also, make sure you notice the colons at the end of the `if` statement. It's also important.

&nbsp;

## Else Problems

***

- The `else` statement complements the `if` statement. An `if/else` pair says: If this expression is true, run this indented code block; otherwise, run this code after the else statement.

- Unlike `if`, `else` doesn't depend on an expression. For example:

    ```python
        if 8 > 9:
            print "I don't printed!"
        else:
            print "I get printed!"
    ```

&nbsp;

## I Got 99 Problems, But a Switch Ain't One

***

- `elif` is short for `else if.` It means exactly what it sounds like: "otherwise, if the following expression is true, do this!"

    ```python
        if 8 > 9:
            print "I don't get printed!"
        elif 8 < 9:
            print "I get printed!"
        else:
            print "I also don't get printed!"
    ```

- In the example above, the `elif` statement is only checked if the original `if` statement is `False`.