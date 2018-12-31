---
layout: page
title: 07 - Module
---
***

## Modules Python Introduction
***

- In the world of programming, a great deal of emphasis is placed on making code reusable. In most cases, we write code so that it can be reusable by ourselves.

- But sometimes we share code that's helpful across a broad range of situations. Python allows us to package code into _files_ or sets of files called _modules_.

- A module is a collection of Python declarations intended broadly to be used as a tool.

- Modules are also often referred to as "libraries" or "packages" — a package is really a directory that holds a _collection_ of modules.

- Usually, the basic syntax you need at the top of your file to use a module in that file is:

    ```python
        from module_name import object_name
    ```

- Often, a library will include a lot of code that you don't need that may slow down your program or conflict with existing code. Because of this, it makes sense to only import what you need.

&nbsp;
## Python Modules Examples
***

- One common library that comes as part of the Python Standard Library is `datetime`.`datetime` helps you work with dates and times in Python.

- Another one of the most commonly used is `random` which allows you to generate numbers or select items at random.

- With `random`, we'll be using more than one piece of the module's functionality, so the import syntax will look like:

    ```python
        import random
    ```

- We'll work with two common `random` functions:

  - `random.choice()` which takes a list as an argument and returns a number from the list.

  - `random.randint()` which takes two numbers as arguments and generates a random number between the two numbers you passed in.

&nbsp;
## Namespaces
***

- Notice that when we want to invoke the `randint()` function we call `random.randint()`. This is default behavior where Python offers a _namespace_ for the module.

- A namespace isolates the functions, classes, and variables defined in the module from the code in the file doing the importing. Your local namespace, meanwhile, is where your code is run.

- Python defaults to naming the namespace after the module being imported, but sometimes this name could be ambiguous or lengthy.

- Sometimes, the module's name could also conflict with an object you have defined within your local namespace.

- Fortunately, this name can be altered by aliasing using the `as` keyword:

    ```python
        import module_name as name_you_pick_for_the_module
    ```

- Aliasing is most often done if the name of the library is long and typing the full name every time you want to use one of its functions is laborious.

- You might also occasionally encounter `import *`. The `*` is known as a "wildcard" and matches anything and everything.

- This syntax is considered dangerous because it could pollute our local namespace. Pollution occurs when the same name could apply to two possible things.

- For example, if you happen to have a function `floor()` focused on floor tiles, using `from math import *` would also import a function `floor()` that rounds down floats.

&nbsp;
## Python Module Decimals
***

- Let's say you are writing software that handles monetary transactions.

- If you used Python's built-in floating-point arithmetic to calculate a sum, it would result in a weirdly formatted number.

    ```python
        cost_of_gum = 0.10
        cost_of_gumdrop = 0.35

        cost_of_transaction = cost_of_gum + cost_of_gumdrop
        # Returns 0.44999999999999996
    ```

- Being familiar with rounding errors in floating-point arithmetic you want to use a data type that performs decimal arithmetic more accurately. You could do the following:

    ```python
        from decimal import Decimal

        cost_of_gum = Decimal('0.10')
        cost_of_gumdrop = Decimal('0.35')

        cost_of_transaction = cost_of_gum + cost_of_gumdrop
        # Returns 0.45 instead of 0.44999999999999996
    ```

- Above, we use the `decimal` module's `Decimal` data type to add 0.10 with 0.35. Since we used the `Decimal` type the arithmetic acts much more as expected.

- Usually, modules will provide functions or data types that we can then use to solve a general problem, allowing us more time to focus on the software that we are building to solve a more specific problem.

&nbsp;
## Modules Python Files and Scope
***

- You may remember the concept of scope from when you were learning about functions in Python.

- If a variable is defined _inside_ of a function, it will not be accessible outside of the function.

- Scope also applies to classes and to the files you are working within.

- Files inside the same directory do not have access to each other's variables, functions, classes, or any other code.

- Files are actually _modules_, so you can give a file access to another file's content using that glorious `import` statement.

- With a single line of `from sandwiches import sandwiches` at the top of __hungry_people.py__, the hungry people will have all the sandwiches they could ever want.