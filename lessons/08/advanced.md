---
layout: page
title: 08 - Advanced Topics
---
***

## Iterators for Dictionaries
***

- Let's start with iterating over a dictionary. Recall that a dictionary is just a collection of keys and values.

    ```python
        d = {
        "Name": "George",
        "Age": 56,
        "Major": True
        }
        print d.items()
        # => [('Major', True), ('Age', 56), ('Name', 'George')]
    ```

- Note that the `.items()` method doesn't return key/value pairs in any specific order.

&nbsp;
## keys() and values()
***

- While `.items()` returns an array of tuples with each tuple consisting of a key/value pair from the dictionary:

- The `.keys()` method returns a list of the dictionary's keys, and

- The `.values()` method returns a list of the dictionary's values.

- Again, these methods will not return the `keys` or `values` from the dictionary in any specific `order`.

- You can think of a tuple as an immutable list. Tuples are surrounded by `()` and can contain any data type.

&nbsp;
## Building Lists
***

- If we wanted to generate a list according to some logic — for example, a list of all the even numbers from 0 to 50?

- Python's answer to this is the `list comprehension`. List comprehensions are a powerful way to generate lists using the _for/in_ and _if_ keywords we've learned.

- Here's a simple example of list comprehension syntax:

    ```python
        new_list = [x for x in range(1, 6)]
        # => [1, 2, 3, 4, 5]
    ```

- This will create a new_list populated by the numbers one to five. If you want those numbers doubled, you could use:

    ```python
        doubles = [x * 2 for x in range(1, 6)]
        # => [2, 4, 6, 8, 10]
    ```

- And if you only wanted the doubled numbers that are evenly divisible by three:

    ```python
        doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]
        # => [6]
    ```

&nbsp;
## List Slicing Syntax
***

- Sometimes we only want part of a Python list. List slicing allows us to access elements of a list in a concise manner. The syntax looks like this:

    ```python
        [start:end:stride]
    ```

- Where `start` describes where the slice _starts_ (inclusive), `end` is where it _ends_ (exclusive), and `stride` describes the space between items in the sliced list.

- For example, a `stride` of 2 would select every other item from the original list to place in the sliced list.

    ```python
        l = [i ** 2 for i in range(1, 11)]
        # Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

        print l[2:9:2]
        # [9, 25, 49, 81]
    ```

- If you don't pass a particular index to the list slice, Python will pick a default.

    ```python
        to_five = ['A', 'B', 'C', 'D', 'E']

        print to_five[3:]
        # prints ['D', 'E']

        print to_five[:2]
        # prints ['A', 'B']

        print to_five[::2]
        # print ['A', 'C', 'E']
    ```

    1. The default `starting` index is _0_.

    2. The default `ending` index is the _end_ of the list.

    3. The default `stride` is _1_.

&nbsp;
## Reversing a List
***

- We have seen that a positive _stride_ progresses through the list from left to right.

- A `negative` stride progresses through the list from right to left.

    ```python
        letters = ['A', 'B', 'C', 'D', 'E']
        print letters[::-1]
    ```

- In the example above, we print out _['E', 'D', 'C', 'B', 'A']`_

&nbsp;
## Anonymous Functions
***

- One of the more powerful aspects of Python is that it allows for a style of programming called `functional programming`.

- which means that you're allowed to pass functions around just as if they were variables or values.

    ```python
        lambda x: x % 3 == 0
    ```

- Is the same as:

    ```python
        def by_three(x):
            return x % 3 == 0
    ```

- Only we don't need to actually give the function a name; it does its work and returns a value without one. That's why the function the lambda creates is an anonymous function.

- Lambda functions are defined using the following syntax:

    ```python
        my_list = range(16)
        res = filter(lambda x: x % 3 == 0, my_list)
        # [0, 3, 6, 9, 12, 15]
    ```

- Lambdas are useful when you need a quick function to do some work for you.

- If you plan on creating a function you'll use over and over, you're better off using `def` and giving that function a name.