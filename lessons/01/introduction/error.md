---
layout: page
title:
---
***

## Errors
***

- Humans are prone to making mistakes. Humans are also typically in charge of creating computer programs. To compensate, programming languages attempt to understand and explain mistakes made in their programs.

- Python refers to these mistakes as _errors_ and will point to the location where an error occurred with a `^` character.

- When programs throw errors that we didn't expect to encounter we call those errors _bugs_.

- Programmers call the process of updating the program so that it no longer produces unexpected errors _debugging_.

- Two common errors that we encounter while writing Python are `SyntaxError` and `NameError`.

&nbsp;
## SyntaxError
***

- `SyntaxError` means there is something wrong with the way your program is written — punctuation that does not belong, a command where it is not expected, or a missing parenthesis can all trigger a `SyntaxError`.

- Example:

    ```python
        print "Mismatched quotes will cause a SyntaxError'
    ```
- The program will abruptly stop running with the following message:

    ```txt
        SyntaxError: EOL while scanning a string literal
    ```

&nbsp;
## NameError
***

- A `NameError` occurs when the Python interpreter sees a word it does not recognize. Code that contains something that looks like a variable but was never defined will throw a `NameError`.

- Example:

    ```python
        print Without quotes will cause a NameError
    ```