---
layout: page
title:
---
***

## Variables
***

- Programming languages offer a method of storing data for reuse.

- If there is a greeting we want to present, a date we need to reuse, or a user ID we need to remember we can create a _variable_ which can store a value.

- In Python, we assign variables by using the equals sign (`=`).

    ```python
        message_string = "Hello there"
        # Prints "Hello there"
        print(message_string)
    ```

- In the above example, we store the message "Hello there" in a variable called `message_string`.

- Variables can't have spaces or symbols in their names other than an underscore (`_`). They can't begin with numbers but they can have numbers after the first letter

- It's no coincidence we call these creatures "variables". If the context of a program changes, we can update a variable but perform the same logical process on it.

    ```python
        # Greeting
        message_string = "Hello there"
        print(message_string)

        # Farewell
        message_string = "Hasta la vista"
        print(message_string)
    ```

- Above, we create the variable `message_string`, assign a welcome message, and print the greeting. After we greet the user, we want to wish them goodbye. We then update `message_string` to a departure message and print that out.

&nbsp;
## Numbers
***

- Computers can understand much more than just strings of text. Python has a few numeric _data types_.

- It has multiple ways of storing numbers. Which one you use depends on your intended purpose for the number you are saving.

- An _integer_, or `int`, is a whole number. It has no decimal point and contains all counting numbers as well as their negative counterparts and the number 0.

- If you were counting the number of people in a room, the number of jellybeans in a jar, or the number of keys on a keyboard you would likely use an integer.

- A _floating-point_ number, or a `float`, is a decimal number. It can be used to represent fractional quantities as well as precise measurements.

- If you were measuring the length of your bedroom wall, calculating the average test score of a seventh-grade class, or storing a baseball player's batting average for the 1998 season you would likely use a `float`.

- Numbers can be assigned to variables or used literally in a program:

    ```python
        an_int = 2
        a_float = 2.1

        print(an_int + 3)
        # prints 5
    ```

- Above we defined an integer and a float as the variables `an_int` and `a_float`. We printed out the sum of the variable `an_int` with the number 3.

- We call the number 3 here a _literal_, meaning it's actually the number `3` and not a variable with the number 3 assigned to it.

- Floating-point numbers can behave in some unexpected ways due to how computers store them. For more information on floating-point numbers and Python, review [Python's documentation on floating-point limitations](https://docs.python.org/3/tutorial/floatingpoint.html).

&nbsp;
## Changing Numbers
***

- Variables that are assigned numeric values can be treated the same as the numbers themselves.

- Two variables can be added together, divided by 2, and multiplied by a third variable without Python distinguishing between the variables and _literals_.

- Performing arithmetic on variables does not change the variable — you can only update a variable using the `=` sign.

    ```python
        coffee_price = 1.50
        number_of_coffees = 4

        # Prints "6.0"
        print(coffee_price * number_of_coffees)
        # Prints "1.5"
        print(coffee_price)
        # Prints "4"
        print(number_of_coffees)

        # Updating the price
        coffee_price = 2.00

        # Prints "8.0"
        print(coffee_price * number_of_coffees)
        # Prints "2.0"
        print(coffee_price)
        # Prints "4"
        print(number_of_coffees)
    ```

- We create two variables and assign numeric values to them. Then we perform a calculation on them. This doesn't update the variables! When we update the `coffee_price` variable and perform the calculations again, they use the updated values for the variable!

&nbsp;
## Plus Equals
***

- Python offers a shorthand for updating variables.

- When you have a number saved in a variable and want to add to the current value of the variable, you can use the `+=` (plus-equals) operator.

    ```python
        # First we have a variable with a number saved
        number_of_miles_hiked = 12

        # Then we need to update that variable
        # Let's say we hike another two miles today
        number_of_miles_hiked += 2

        # The new value is the old value
        # Plus the number after the plus-equals
        print(number_of_miles_hiked)
        # Prints 14
    ```

- Above, we keep a running count of the number of miles a person has gone hiking over time.

- Instead of recalculating from the start, we keep a grand total and update it when we've gone hiking further.

- The plus-equals operator also can be used for string concatenation, like so:

    ```python
        hike_caption = "What an amazing time to walk through nature!"

        # Almost forgot the hashtags!
        hike_caption += " #nofilter"
        hike_caption += " #blessed"
    ```

- We create the social media caption for the photograph of nature we took on our hike, but then update the caption to include important social media tags we almost forgot.

&nbsp;
## Booleans
***

- Sometimes we have a need for variables that are either `true` or `false`. This datatype, which can only ever take one of two values, is called a __boolean__.

- In Python, we define booleans using the keywords `True` and `False`:

    ```python
        a = True
        b = False
    ```

- A boolean is actually a special case of an integer. A value of `True` corresponds to an integer value of `1`, and will behave the same. A value of `False` corresponds to an integer value of `0`.