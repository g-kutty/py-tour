---
layout: page
title: 03 - Date and Time
---
***

## The datetime Library

***

- A lot of times you want to keep track of when something happened. We can do so in Python using `datetime`.

&nbsp;

## Getting the Current Date and Time

***

- We can use a function called `datetime.now()` to retrieve the current date and time.

    ```Python
        from datetime import datetime
        print datetime.now()
    ```

- The first line imports the datetime library so that we can use it.

- The second line will print out the current date and time.

&nbsp;

## Extracting Information

***

- Notice how the output looks like `2013-11-25 23:45:14.317454`.

    ```python
        from datetime import datetime
        now = datetime.now()

        current_year = now.year
        current_month = now.month
        current_day = now.day
    ```

- In the third line, we take the year from the variable `now` and store it in `current_year`.

- In the fourth and fifth lines, we store the `month` and `day` from now.

&nbsp;

## Hot Date

***

- What if we want to print today's date in the following format? `mm/dd/yyyy`. Let's use string substitution again!

    ```Python
        from datetime import datetime
        now = datetime.now()

        print '%02d-%02d-%04d' % (now.month, now.day, now.year)
    ```
- Remember that the standalone `%` operator after the string will fill the `%02d` and `%04d` placeholders in the string on the left with the numbers and strings in the parentheses on the right.

- `%02d` pads the month and day numbers with zeros to two places, and `%04d` pads the year to four places. This is one way dates are commonly displayed.

&nbsp;

## Pretty Time

***

- Let's do the same for the hour, minute, and second.

    ```Python
        from datetime import datetime
        now = datetime.now()

        print now.hour
        print now.minute
        print now.second
    ```

- In the above example, we just printed the current hour, then the current minute, then the current second.

- We can again use the variable `now` to print the time.