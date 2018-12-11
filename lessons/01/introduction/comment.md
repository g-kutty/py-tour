---
layout: page
title:
---
***

## Comments
***

- Ironically, the first thing we're going to do is show how to tell a computer to ignore a part of a program.

- Text written in a program but not run by the computer is called a _comment_. Python interprets anything after a `#` as a comment.

- Comments can:

  - Provide context for why something is written the way it is:

    ```python
        # This variable will be used to count the number of times anyone tweets the word persnickety
        persnickety_count = 0
    ```

  - Help other people reading the code understand it faster:

    ```python
        # This code will calculate the likelihood that it will rain tomorrow
        complicated_rain_calculation_for_tomorrow()
    ```

  - Ignore a line of code and see how a program will run without it:

    ```python
        # useful_value = old_sloppy_code()
        useful_value = new_clean_code()
    ```