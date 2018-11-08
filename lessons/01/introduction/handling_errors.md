---
layout: page
title:
---
***

## Handling Errors

***

- These are complaints that Python makes when it doesn't understand what you want it to do.

- Here are some common errors that we might run into when printing strings:

- __SyntaxError__

  - If the quotes are mismatched Python will notice this and inform you that your code has an error in its syntax because the line ended before the double-quote that was supposed to close the string appeared.

    ```python
        print "Mismatched quotes will cause a SyntaxError'
    ```

  - The program will abruptly stop running with the following message:

    ```python
        SyntaxError: EOL while scanning a string literal
    ```

- __NameError__

  - Another issue you might run into is attempting to create a string without quotes at all. Python treats words not in quotes as commands, like the `print` statement.

  - If it fails to recognize these words as defined, Python will complain the code has a `NameError`.

    ```python
        print Without quotes will cause a NameError
    ```