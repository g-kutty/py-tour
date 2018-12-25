---
layout: page
title: 02 - Functions
---

## Python Functions
***

- In Python, some tasks need to be done multiple times within a program. Rather than rewrite code, a function can be defined using the keyword `def` with parameters, which are inputs into the function.

- The function can return some value as an output with the keyword return and be implemented throughout the code.

    ```python
        def my_function (x):
            return x+1

        print(my_function(2))
    ```

- In the example, a function `my_function` is defined with the parameter `x`. The function returns a value that takes the parameter and adds 1 to it. It is then implemented multiple times with different input values.

&nbsp;
## Calling Functions
***

- Python uses simple syntax to use or _call_ a preexisting function. A function can be called by writing the name of it, followed by parentheses.

    ```python
        doHomework()
    ```

- For example, the code above would call the `doHomework()` method.

&nbsp;
## Defining Functions
***

- A developer can create or define his or her own function in Python. To do so, the keyword `def` is followed by the name of the function, parentheses, and a colon.

- The body of the function, or the code for what the function will actually do, comes after the colon on an indented line.

    ```python
        def doHomework():
            ...
    ```

&nbsp;
## Function Indentation
***

- Python uses indentation to identify blocks of code. Code within the same block should be indented at the same level.

- A Python function is one type of code block. All code under a function declaration should be indented to identify it as part of the function.

- There can be additional indentation within a function to handle other statements such as `for` and `if` so long as the lines are not indented less than the first line of the function code.

    ```python
        # Indentation is used to identify code blocks
        def test_function(number):
            # This code is part of test function
            print("Inside the test_function")
            sum = 0
            for x in range(number):
                # More indentation because 'for' has a code block
                # but still part of he function
                sum += x
            return sum
        print("This is not part of test_function")
    ```

&nbsp;
## Function Parameters
***

- Sometimes functions need inputs to fill in the blanks within their code. Python functions have _parameters_ that do just that.

- _Parameters_ are variables that are first defined in the function definition and hold values which are necessary for a function's operations.

- For example, the code below uses a _character_, _setting_, and _skill_ as inputs to write the first sentence of a book.

    ```python
        def writeABook(character, setting, special_skill):
            print(character+" is in "+setting+" practicing her "+special_skill)
    ```

&nbsp;
## Multiple Parameters
***

- Python functions can have multiple _parameters_.

- Just like how you wouldn’t go to school without both a backpack and a pencil case, functions may also need more than one input to carry out their operations.

- To define functions with multiple _parameters_, the necessary inputs are placed in a comma-separated list within the parentheses of the function definition.

&nbsp;
## Function Arguments
***

- _Parameters_ in python are variables— placeholders for the actual values the function needs.

- When the function is called, these values are passed in as _arguments_.

    ```python
        def sales(grocery_store, item_on_sale, cost):
            print(grocery_store+" is selling "+item_on_sale+" for "+cost)

        sales("The Farmer’s Market", "toothpaste", "$1")
    ```

- For example, the arguments passed into the function `.sales()` are the Farmer’s Market, toothpaste, and $1 which correspond to the parameters _grocery_store_, _item_on_sale_, and _cost_.

&nbsp;
## Function Keyword Arguments
***

- Python functions can be defined with named arguments which may have default values provided.

- The arguments of a Python function are available inside the function as variables. They are also available when the function is called elsewhere in a program.

- When function arguments are passed using their names, they are referred to as keyword arguments.

- The use of keyword arguments when calling a function allows the arguments to be passed in any order - NOT just the order that they were defined in the function.

    ```python
        def find_volume(length=1, width=1, depth=1):
            print("Length = " + str(length))
            print("Width = " + str(width))
            print("Depth = " + str(depth))
            return length * width * depth;

        find_volume(1, 2, 3)
        find_volume(length=5, depth=2, width=4)
        find_volume(2, depth=3, width=4)
    ```

&nbsp;
## Returning value from Python function
***

- A `return` keyword is used to return a value from a Python function.

- The value returned from a function can be assigned to a variable which can then be used in the program.

- In the example, the function `check_leap_year` returns a string which indicates if the passed parameter is a leap year or not.

    ```python
        def check_leap_year(year):
            if year % 4 == 0:
                return str(year) + " is a leap year."
            else:
                return str(year) + " is not a leap year."

            year_to_check = 2018
            returned_value = check_leap_year(year_to_check)
            print(returned_value) #2018 is not a leap year.
    ```

&nbsp;
## Returning Multiple Values
***

- Python functions are able to return multiple values using one `return` statement.

- All values that should be returned are listed after the `return` keyword and are separated by commas.

    ```python
        def square_point(x, y, z):
            x_squared = x * x
            y_squared = y * y
            z_squared = z * z
            # Return all three values:
            return x_squared, y_squared, z_squared
    ```

- In the example, the function `square_point` returns `x_squared`, `y_squared`, and `z_squared` by listing them after the `return` statement and separating them by commas.

&nbsp;
## Parameters As Local Variables
***

- Parameters are found inside the definition of a function and behave identically to local variables.

- However, they contain the values passed into the function when the function is called.

- Like local variables, they cannot be called outside of the scope of the function, or the program will throw an error.

    ```python
        def my_function(c):
            print(c)
            my_function(7) # Pass the value 7 into the function
            print(c) # Will cause an error as c no longer exists
    ```

- In the example, the parameter `c` is defined as a part of the definition of `my_function` and therefore can only be accessed within `my_function`. Attempting to print the value of `c` outside of the function causes an error.

&nbsp;
## Global Variables
***

- A variable that is defined outside of a function is called a global variable. It can usually be accessed inside a function.

- While a global variable can be modified on the outside of a function, it cannot be modified within a function.

    ```python
        a = 1
        def f1():
            print (a) # will print 1
        f1()
    ```

- In the example, the variable `a` is a global variable because it is defined outside of the function `f1`. It is therefore accessible to `f1`, which will print the value of `a`.

&nbsp;
## Python Variable Scope
***

- Not all the variables used by a function need to be included in the function definition.

- For instance, this function uses a variable defined on a previous line to create a greeting customized with a name.

    ```python
        greeting = "Hello there, "

        def greet_someone(name):
            print(greeting + name + " !")
    ```

&nbsp;
## The Scope of Variables
***

- In Python, a variable defined inside a function is called a local variable. It cannot be used outside of the scope of the function, and attempting to do so without defining the variable outside of the function will cause an error.

    ```python
        a = 5
        def f1():
            a = 2
            print(a)

        print(a) # Will print 5
        f1() # Will print 2
    ```

- In the example, the variable `a` is defined both inside and outside of the function. When the function `f1` is implemented, `a` is printed as `2` because it is locally defined to be so.

- However, when printing `a` outside of the function, `a` is printed as `5` because it is implemented outside of the scope of the function.