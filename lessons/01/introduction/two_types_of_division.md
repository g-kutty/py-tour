---
layout: page
title:
---
***

## Two Types of Division

***

- In Python 2, when we divide two integers, we get an integer as a result. When the quotient is a whole number, this works fine:

    ```python
        # The value of quotient is now 3, which makes sense
        quotient = 6/2
    ```

- However, if the numbers do not divide evenly, the result of the division is truncated into an integer. In other words, the quotient is rounded down to a whole number.

    ```python
        # The value of quotient is 3, even though the result of the division here is 3.5
        quotient = 7/2
    ```

- To yield a float as the result instead, programmers often change either the numerator or the denominator (or both) to be a float:

    ```python
        # The value of quotient1 is 3.5
        quotient1 = 7./2
        # The value of quotient2 is 3.5
        quotient2 = 7/2.
        # The value of quotient3 is 3.5
        quotient3 = 7./2.
    ```

- An alternative way is to use the float() method:

    ```python
        # The value of quotient1 is 3.5
        quotient1 = float(7)/2
    ```