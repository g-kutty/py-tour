---
layout: page
title:
---
***
## Logical Operators
***

&nbsp;
### The and Operator
***
  
- The `and` operator is a logical operator that combines two boolean expressions.

- If both boolean expressions are true, then the `and` operator will return `True`. However, even if one expression is false, the operator will return `False`.

    ```python
        # will output False even though (2 < 5) is true
        print(1 > 5 and 2 < 5)
        # will output True
        print(5 >= 5 and 4 < 16)
    ```

&nbsp;
### The Python or Operator
***

- The Python `or` operator combines two Boolean expressions and evaluates to `True` if at least one of the expressions returns `True`.

- Otherwise, if both expressions are `False`, than the entire expression evaluates to `False`.

- The code below gives examples on how this works.

    ```python
        # Evaluates to True
        True or False
        # Evaluates to True
        1 == 1 or 1 < 2
    ```

&nbsp;
### The Python not Operator
***

- The Python `not` operator is used in a Boolean expression in order to evaluate the expression to its inverse value.

- If the original expression was `True`, including the `not` operator would make the expression `False`, and vice versa.

- For example, the statement `1>2` evaluates to `False` so adding the `not` operator will make not `1>2` evaluate to `True`.

    ```python
        # Evaluates to False
        not True
        # Evaluates to True
        not 1 > 2
    ```
