---
layout: page
title:
---
***

## Calculations
***

- Computers absolutely excel at performing calculations. The "compute" in their name comes from their historical association with providing answers to mathematical questions.

- Python performs addition, subtraction, multiplication, and division with `+`, `-`, `*`, and `/`.

    ```python
        # Prints "500"
        print(573 - 74 + 1)

        # Prints "50"
        print(25 * 2)

        # Prints "2.0"
        print(10 / 5)
    ```

- Notice that when we perform division, the result has a decimal place. This is because Python converts all `int`s to `float`s before performing division.

- In older versions of Python (2.7 and earlier) this conversion did not happen, and integer division would always round down to the nearest integer.

- Division can throw its own special error: `ZeroDivisionError`. Python will raise this error when attempting to divide by 0.

- Mathematical operations in Python follow the standard mathematical [order of operations](https://en.wikipedia.org/wiki/Order_of_operations).

&nbsp;
## Exponents
***

- Python can also perform exponentiation. In written math, you might see an exponent as a superscript number, but typing superscript numbers isn't always easy on modern keyboards.

- Since this operation is so related to multiplication, we use the notation `**`.

    ```python
        # 2 to the 10th power, or 1024
        print(2 ** 10)

        # 8 squared, or 64
        print(8 ** 2)

        # 9 * 9 * 9, 9 cubed, or 729
        print(9 ** 3)

        # We can even perform fractional exponents
        # 4 to the half power, or 2
        print(4 ** 0.5)
    ```

- Here, we compute some simple exponents. We calculate 2 to the 10th power, 8 to the 2nd power, 9 to the 3rd power, and 4 to the 0.5th power.

&nbsp;
## Modulo
***

- Python offers a companion to the division operator called the modulo operator.

- The modulo operator is indicated by `%` and gives the remainder of a division calculation.

- If the number is divisible, then the result of the modulo operator will be 0.

    ```python
        # Prints 4 because 29 / 5 is 5 with a remainder of 4
        print(29 % 5)

        # Prints 2 because 32 / 3 is 10 with a remainder of 2
        print(32 % 3)

        # Modulo by 2 returns 0 for even numbers and 1 for odd numbers
        # Prints 0
        print(44 % 2)
    ```

- Here, we use the modulo operator to find the remainder of division operations. We see that `29 % 5` equals 4, `32 % 3` equals 2, and `44 % 2` equals 0.