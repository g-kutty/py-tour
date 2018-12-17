---
layout: page
title: 13 - Strings
---
***

- Another useful data type is the __string__. A string can contain letters, numbers, and symbols.

    ```python
        name = "Ryan"
        age = "19"
        food = "cheese"
    ```

- In the above example, we create a variable `name` and set it to the string value _"Ryan"_.

- We also set `age` to _"19"_ and `food` to _"cheese"_.

- Strings need to be within quotes.

&nbsp;

## Escaping characters

***

- There are some characters that cause problems. For example:

    ```python
        'There's a snake in my boot'
    ```

- This code breaks because Python thinks the apostrophe in _'There`'`s'_ ends the string. We can use the backslash to fix the problem, like this:

    ```python
        'There\'s a snake in my boot!'
    ```

&nbsp;

## Access by Index

***

- Each character in a string is assigned a number. This number is called the `index`.

    ```python
        c = "cats"[0]
        n = "Ryan"[3]
    ```

- In the above example, we create a new variable called `c` and set it to _"c"_, the character at index zero of the string _"cats"_.

- Next, we create a new variable called `n` and set it to _"n"_, the character at index three of the string _"Ryan"_.

- Notice that in the first _"cat"_ example we are calling the 0th letter of _"cat"_ and getting _"c"_ in return. This is because in Python indices begin counting at 0.

&nbsp;

## String methods

***

- String methods let you perform specific tasks for strings. We'll focus on four string methods:

  1.`len()`- gets the length of a string.

    ```Python
        len("Norwegian Blue")
    ```

  2.`lower()` - gets the lowercase string from the given string.

    ```python
        "Ryan".lower()
    ```

  3.`upper()` - gets the uppercase string from the given string.

    ```Python
        "Ryan".upper()
    ```

  4.`str()` - method turns non-strings into strings.

    ```python
        str(2)
    ```

&nbsp;

## Dot Notation

***

- Let's take a closer look at why you use _len`(`string`)`_ and _str`(`object`)`_, but dot notation such as _"String".upper()_ for the rest.

- Methods that use dot notation only work with strings.

- On the other hand, `len()` and `str()` can work on other data types.

&nbsp;

## String Concatenation

***

- The `+` operator between strings will _'add'_ them together, one after the other. Notice that there are spaces inside the quotation marks after _Life_ and _of_ so that we can make the combined string look like 3 words.

    ```python
        print "Life " + "of " + "Brian"
    ```

&nbsp;

## Explicit String Conversion

***

- Sometimes you need to combine a string with something that isn't a string. In order to do that, you have to convert the non-string into a string.

    ```python
        print "I have " + str(2) + " coconuts!"
    ```

- The `str()` method converts non-strings into strings.

&nbsp;

## String Formatting with %

***

- When you want to print a variable with a string, there is a better method than concatenating strings together.

    ```python
        name = "George"
        print "Hello %s" % (name)
    ```

- The `%`operator after the string is used to combine a string with variables. The `%` operator will replace the `%s` in the string with the string variable that comes after it.

- You need the same number of `%s` terms in a string as the number of variables in parentheses:

    ```Python
        print "The %s who %s %s!" % ("Tony", "Cyril", "George")
    ```