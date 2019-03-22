---
layout: page
title:
---
***
## Relational Operators
***

&nbsp;
### Equal Operator
***

- The Python equal operator (`==`) is used to compare two values, variables or expressions to determine if they are the same.

- If the values being compared are the same, the operator returns `True`, otherwise it returns `False`.

- The operator takes the data type into account when making the comparison, so a string value of `"2"` is not considered the same as a numeric value of `2`.

- When the operands are expressions, they are evaluated first, before the comparison is made.

    ```python
        # Equal operator
        if 'Yes' == 'Yes':
            print('They are equal')

        if (2 > 1) == (5 < 10):
            print('Both expressions give the same result')

        if '2' == 2:
            print('They are equal')
        else:
            print('They are not equal')
    ```

&nbsp;
### Not Equals Operator
***

- The Python not equals operator (`!=`) is used to compare two values, variables or expressions to determine if they are NOT the same.

- If they are NOT the same, the operator returns `True`. If they are the same, then it returns `False`.

- The operator takes the data type into account when making the comparison so a value of `10` would NOT be equal to the string value `"10"` and the operator would return `True`.

- If expressions are used, then they are evaluated to a value of `True` or `False` before the comparison is made by the operator.

    ```python
        # Not Equals Operator
        if "Yes" != "No":
            print("They are NOT equal")

        if 10 != 20:
            print("They are NOT equal")

        if (10 > 1) != (10 > 1000):
            # True != False
            print("They are NOT equal")
    ```

&nbsp;
### Comparison Operators
***

- In Python, relational operators compare two values or expressions. The most common ones are less than (`<`), greater than (`>`), less than or equal to (`<=`), and greater than or equal to (`>=`).

- If the relation is sound, then the entire expression will evaluate to `True`. If not, the expression evaluates to `False`.

    ```python
        a = 2
        b = 3
        a < b #evaluates to True
        a > b #evaluates to False
        a >= b #evaluates to False
        a <= b #evaluates to True
        a <= a #evaluates to True
    ```