---
layout: page
title:
---
***

&nbsp;
## Logical Operators
***

- ### The and Operator

  - The `and` operator is a logical operator that combines two boolean expressions.

  - If both boolean expressions are true, then the `and` operator will return `True`. However, even if one expression is false, the operator will return `False`.

    ```python
        print(1 > 5 and 2 < 5) # will output False even though (2 < 5) is true
        print(5 >= 5 and 4 < 16) # will output True
    ```

- ### The Python or Operator

  - The Python `or` operator combines two Boolean expressions and evaluates to `True` if at least one of the expressions returns `True`.

  - Otherwise, if both expressions are `False`, than the entire expression evaluates to `False`.

  - The code below gives examples on how this works.

    ```python
            True or True # Evaluates to True
            True or False # Evaluates to True
            False or False # Evaluates to False
            1 == 1 or 1 < 2 # Evaluates to True
            1 < 2 or 3<1 # Evaluates to True
            3<1 or 1>6 # Evaluates to False
    ```

- ### The Python not Operator

  - The Python Boolean `not` operator is used in a Boolean expression in order to evaluate the expression to its inverse value.

  - If the original expression was `True`, including the `not` operator would make the expression `False`, and vice versa.

  - For example, the statement `1>2` evaluates to `False` so adding the `not` operator will make not `1>2` evaluate to `True`.

    ```python
        not True # Evaluates to False
        not False # Evaluates to True
        1 > 2  # Evaluates to False
        not 1 > 2 # Evaluates to True
        1 == 1 # Evaluates to True
        not 1 == 1 # Evaluates to False
    ```
