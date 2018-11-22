---
layout: page
title: 07 - Loops
---
***

## While Loop
***

- The __while__ loop is similar to an _if statement_: it executes the code inside of it if some condition is _true_.

- The difference is that the _while loop_ will continue to execute as long as the condition is true. In other words, instead of executing if something is true, it executes while that thing is true.

&nbsp;
## Condition
***

- The __condition__ is the expression that decides whether the loop is going to continue being executed or not.

    ```python
        loop_condition = True

        while loop_condition:
            print "I am a loop"
            loop_condition = False
    ```

- Inside a while loop, you can do anything you could do elsewhere, including arithmetic operations.

&nbsp;
## Simple errors
***

- A common application of a while loop is to check user input to see if it is valid.

- For example, if you ask the user to enter _y_ or _n_ and they instead enter _7_, then you should re-prompt them for input.

    ```python
        choice = raw_input('Did you like python? (y/n)')

        while choice != 'y' and choice != 'n':
            choice = raw_input("Sorry, I didn't catch that. Enter again: ")
    ```

&nbsp;
## Infinite loops
***

- An __infinite loop__ is a loop that never exits. This can happen for a few reasons:

  1. The loop condition cannot possibly be false (e.g. while 1 != 2)

  2. The logic of the loop prevents the loop condition from becoming false.

        ```python
            count = 10
            while count > 0:
                count += 1 # Instead of count -= 1
        ```

&nbsp;
## Break
***

- The __break__ is a one line statement that means _"exit the current loop."_ An alternate way to make our counting loop exit and stop executing is with the break statement.

    ```python
        count = 0

        while True:
            print count
            count += 1
            if count >= 10:
                break
    ```

- The difference here is that this loop is guaranteed to run at least once.

&nbsp;
## While / else
***

- Something completely different about Python is the __while/else__ construction.

- `while/else` is similar to `if/else`, but there is a difference: the `else` block will execute anytime the loop condition is evaluated to `False`.

- This means that it will execute if the loop is never entered or if the loop exits normally. If the loop exits as the result of a break, the else will not be executed.

    ```python
        import random

        count = 0
        while count < 3:
            num = random.randint(1, 6)
            print num
            if num == 5:
                print "Sorry, you lose!"
                break
            count += 1
        else:
            print "You win!"
    ```

&nbsp;
## For your strings
***

- Using a for loop, you can print out each individual character in a string.

    ```python
        thing = "spam!"

        for c in thing:
            print c
    ```

- String manipulation is useful in for loops if you want to modify some content in a string.

    ```python
        word = "Marble"
        for char in word:
            print char,
    ```

- The example above iterates through each character in word and `,` in the end, prints out _M a r b l e_.

- The `,` character after our print statement means that our next print statement keeps printing on the same line.

&nbsp;
## Looping over a dictionary
***

- You may be wondering how looping over a dictionary would work. Would you get the key or the value?

- The short answer is: you get the key which you can use to get the value.

    ```python
        d = {'x': 9, 'y': 10, 'z': 20}
        for key in d:
        if d[key] == 10:
            print "This dictionary has the value 10!"
    ```

    1. First, we create a dictionary with strings as the keys and numbers as the values.

    2. Then, we iterate through the dictionary, each time storing the key in `key`.

    3. Next, we check if that key's value is equal to 10.

    4. If so, we print _"This dictionary has the value 10!"_

&nbsp;
## Counting as you go
***

- A weakness of using this for-each style of iteration is that you don't know the index of the thing you're looking at.

- Generally this isn't an issue, but at times it is useful to know how far into the list you are.

- __enumerate__ works by supplying a corresponding index to each element in the list that you pass it.

    ```python
        choices = ['pizza', 'pasta', 'salad', 'nachos']

        print 'Your choices are:'
        for index, item in enumerate(choices):
            print index + 1, item
    ```

&nbsp;
## Multiple lists
***

- It's also common to need to iterate over two lists at once. This is where the built-in `zip` function comes in handy.

- `zip` will create pairs of elements when passed two lists, and will stop at the end of the shorter list.

- `zip` can handle three or more lists as well!

    ```python
        list_a = [3, 9, 17, 15, 19]
        list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

        for a, b in zip(list_a, list_b):
            if a>b:
                print a
            else:
                print b
    ```

&nbsp;
## For / else
***

- Just like with `while`, `for` loops may have an `else` associated with them.

- In this case, the `else` statement is executed `after`the `for`, but only if the for ends normally, that is, not with a break.

    ```python
        fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

        print 'You have...'
        for f in fruits:
            if f == 'tomatoes':
                print 'A tomato is not a fruit!'
                break
            print 'A', f
        else:
            print 'A fine selection of fruits!'
    ```