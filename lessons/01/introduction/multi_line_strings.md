---
layout: page
title:
---
***

## Multi-line Strings

***

- We have seen how to define a string with single quotes and with double quotes. If we want a string to span multiple lines, we can also use triple quotes:

    ```python
        address_string = """District 1 1656
        Union Street Eureka
        707-445-6600"""
    ```

- When a string like this is not assigned to a variable, it works as a multi-line comment.

    ```python
        """The following piece of code does the following steps:
        takes in some input
        does An Important Calculation
        returns the modified input and a string that says "Success!" or "Failure..."
        """
        ... a complicated piece of code here...
    ```