---
layout: page
title: 05 - Functions
---
***

You might have considered the situation where you would like to reuse a piece of code, just with a few different values. Instead of rewriting the whole code, it's much cleaner to define a __function__, which can then be used repeatedly.

&nbsp;

## Function Junction

***

- Functions are defined with three components:

  1. __header__, which includes the _def_ keyword, the name of the function, and any parameters the function requires.

        ```python
        # There are no parameters
        def hello_world():
        ```

  2. An optional __comment__ that explains what the function does.

        ```python
        """Prints 'Hello World!' to the console."""
        ```

  3. The __body__, which describes the procedures the function carries out. The body is indented, just like conditional statements.

        ```python
        print "Hello World!"
        ```

- Here's the full function pieced together:

    ```python
    def hello_world():
    """Prints 'Hello World!' to the console."""

        print "Hello World!"
    ```

- After defining a function, it must be called to be implemented.

&nbsp;

## Parameters and Arguments

***

- Let's take another look at the definition of the function `square`:

    ```python
    def square(n):
    ```

- Here, _n_ is a `parameter` of square. A parameter is a variable that is an input to a function.

- The values of the parameters passed into a function are known as the `arguments`.

    ```python
    square(10)
    ```

- Here, the function `square` was called with the parameter `n` set to the argument 10.

- Typically, when you call a function, you should pass in the same number of arguments as there are parameters.

&nbsp;

## Functions Calling Functions

***

- We've seen functions that can print text or do simple arithmetic, but functions can be much more powerful than that. For example, a function can call another function:

    ```python
    def fun_one(n):
        return n * 5

    def fun_two(m):
        return fun_one(m) + 7
    ```

&nbsp;

## Generic Imports

***

- There is a Python module named `math` that includes a number of useful variables and functions, and `sqrt()` is one of those functions.

- In order to access `math`, all you need is the import keyword. When you simply import a module this way, it's called a __generic import__.

    ```python
    import math
    print math.sqrt(25)
    ```

&nbsp;

## Function Imports

***

- However, we only really needed the sqrt function, and it can be frustrating to have to keep typing `math.sqrt()`.

- It's possible to import only certain variables or functions from a given _module_. Pulling in just a single function from a module is called a __function import__, and it's done with the from keyword:

    ```python
    from module import function
    ```

- Now you can just type `sqrt()` to get the square root of a number instead of _math.sqrt()!_.

&nbsp;

## Universal Imports

***

- What if we still want all of the variables and functions in a module but don't want to have to constantly type `math.name`

- __Universal import__ can handle this for you. The syntax for this is:

    ```python
    from module import *
    ```

&nbsp;

## Here Be Dragons

***

- Universal imports may look great on the surface, but they're not a good idea for one very important reason: they fill your program with a _ton_ of _variable_ and _function_ names without the safety of those names still being associated with the module(s) they came from.

- If you have a function of your very own named _sqrt_ and you import _math_, your function is safe:  there is your _sqrt_ and there is _math.sqrt_.

- If you do from math `import *`, however, you have a `problem`: namely, two different functions with the exact same name.

- Even if your own definitions don't directly conflict with names from imported modules, if you `import *` from several modules at once, you `won't` be able to `figure out` which variable or function came from where.

- For these reasons, it's best to stick with either _import module_ and type _module.name_ or just import specific variables and functions from various modules as needed.

- Below code will show you everything available in the math module.

    ```python
    import math # Imports the math module
    everything = dir(math) # Sets everything to a list of things from math
    print everything # Print all!
    ```

&nbsp;

## On Beyond Strings

***

- let's look at some of the functions that are built in to Python (no modules required!):

  - `max()` function takes any number of arguments and returns the largest one.

  - `min()` then returns the smallest of a given series of arguments.

  - `abs()` function returns the absolute value of the number it takes as an argument

    - For instance, `3` and `-3` both have the same absolute value: `3`. The _abs()_ function always returns a positive value, and unlike _max()_ and _min()_, it only takes a single number.

  - `type()` function returns the type of the data it receives as an argument.

    ```python
    print type(42)
    print type(4.2)
    print type('spam')
    ```