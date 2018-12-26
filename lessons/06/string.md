---
layout: page
title: 06 - Strings
---
***

## Lower
***

- In Python, the string method `.lower()` returns a string with all uppercase characters converted into lowercase. `.lower()` does not take any input arguments.

    ```python
        greeting = "Welcome To Chili's"
        print(greeting.lower())

        # welcome to chili's
    ```

&nbsp;
## Python string method `.upper()`
***

- The Python string method `.upper()` returns the string with all lowercase characters converted to uppercase.

    ```python
        dinosaur = "T-Rex"
        print(dinosaur.upper())
        # Prints T-REX in the console.
    ```

&nbsp;
## Python string method `.title()`
***

- The Python string method `.title()` returns the string in title case.

- With title case, the first character of each word is capitalized while the rest of the characters are lowercase.

    ```python
        my_var = "dark knight"
        print(my_var.title()) # "Dark Knight"
    ```

&nbsp;
## Python string `.split()` method
***

- The Python string method `.split()` will split a string into a list of items.

- If an argument is passed to the method, that value is used as the delimiter on which to split the string.

- If no argument is passed, the default behavior is to split on _whitespace_.

    ```python
        text = "Silicon Valley"
        print(text.split())     # ['Silicon', 'Valley']
        print(text.split('i'))  # ['S', 'l', 'con Valley']
        print(text.split('l'))  # ['Si', 'icon Va', '', 'ey']
    ```

&nbsp;
## Join strings
***

- In Python, the `.join()` method takes an array of strings and joins them together with a separator, or delimiter.

- It is a way to concatenate string array elements into one string.

    ```python
        colors = ['red', 'orange', 'yellow']
        print(' '.join(colors))

        # Red orange yellow
    ```

&nbsp;
## Strip method
***

- In Python, strings can be edited with the `.strip()` method. `.strip()` removes a given character or substring from the left and right of a string.

- It takes a character or substring as an argument, and returns a copy of the given string with that argument removed.

- If no argument is provided, whitespace is stripped from either side of the string.

- `.strip()` will remove all of the given argument from the left and right of the string, until there is a mismatch.

    ```python
        ex = "******hello**"
        print(ex.strip("*"))

        # hello
    ```

&nbsp;
## String replace
***

- The `.replace()` method is used to replace the occurrence of the first argument with the second argument within the string.

- The first argument is the old substring to be replaced, and the second argument is the new substring that will replace every occurrence of the first one within the string.

    ```python
        fruit = "Strawberry"
        print(fruit.replace('r', 'R'))

        # StRawbeRRy
    ```

&nbsp;
## Python string method `.find()`
***

- The Python string method `.find()` returns the index of the first occurrence of the string passed as the argument. It returns `-1` if no occurrence is found.

    ```python
        mountain_name = "Mount Kilimanjaro"
        print(mountain_name.find("o")) # Prints 1 in the console.
    ```

&nbsp;
## Python String `.format()`
***

- The Python string method `.format()` replaces empty brace (`{}`) placeholders in the string with its arguments.

- If keywords are specified within the placeholders, they are replaced with the corresponding named arguments to the method.

    ```python
        msg1 = 'Fred scored {} out of {} points.'
        msg1.format(3, 10)
        # => 'Fred scored 3 out of 10 points.'

        msg2 = 'Fred {verb} a {adjective} {noun}.'
        msg2.format(adjective='fluffy', verb='tickled', noun='hamster')
        # => 'Fred tickled a fluffy hamster.'
    ```

&nbsp;
## Indexing and Slicing Strings
***

- Python strings can be indexed using the same notation as lists, since strings are lists of characters.

- A single character can be accessed with bracket notation (`[index]`), or a substring can be accessed using slicing (`[start:end]`).

- Indexing with negative numbers counts from the end of the string.

    ```python
        str = 'yellow'
        str[1]     # => 'e'
        str[-1]    # => 'w'
        str[4:6]   # => 'ow'
        str[:4]    # => 'yell'
        str[-3:]   # => 'low'
    ```

&nbsp;
## String concatenation
***

- To combine the content of two strings into a single string, Python provides the `+` operator. This process of joining strings is called concatenation.

    ```python
        x = 'One fish, '
        y = 'two fish.'
        z = x + y
        print(z)
        # 'One fish, two fish.'
    ```

&nbsp;
## String lengths
***

- In Python, the built in function `len()` calculates the length of objects. It can be used to compute the length of strings, lists, sets, and other countable objects!

    ```python
        length = len("Hello")
        print(length)
        # output: 5

        colors = ['red', 'yellow', 'green']
        print(len(colors))
        # output: 3
        print(len(colors[1]))
        # output: 6
    ```

&nbsp;
## IndexError
***

- When indexing into a string in Python, if you try to access an index that doesn't exist, an `IndexError` is generated. For example, the following code would create an `IndexError`:

    ```python
        fruit = "Berry"
        index = fruit[6]
    ```

&nbsp;
## Immutable strings
***

- Strings are immutable in Python. This means that once a string has been defined, it can't be changed.

- There are no mutating methods for strings. This is unlike data types like lists, which can be modified once they are created.

&nbsp;
## Escaping characters in a string
***

- Backslashes (`\`) are used to escape characters in a Python string.

- For instance, to print a string with quotation marks, the given code snippet can be used.

    ```python
        txt = "She said \"Never let go\"."
        print(txt) # She said "Never let go".
    ```

&nbsp;
## Iterate String
***

- To iterate through a string in Python, "for...in" notation is used.

    ```python
        str = "hello"
        for c in str:
        print(c)

        # h
        # e
        # l
        # l
        # o
    ```

&nbsp;
## The Python in syntax
***

- In Python, the `in` syntax is used to determine if a letter or a substring exists in a string.

- It returns `True` if a match is found, otherwise `False` is returned.

    ```python
        game = "Popular Nintendo Game: Mario Kart"
        print("l" in game) # Prints True in the console.
        print("x" in game) # Prints False in the console.
    ```