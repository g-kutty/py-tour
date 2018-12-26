---
layout: page
title: 05 - Loop
---
***

## Python for Loops
***

- Python `for` loops can be used to iterate over and perform an action one time for each element in a list.

- Proper `for` loop syntax assigns a temporary value, the current item of the list, to a variable on each successive iteration: `for <temporary value> in <a list>:`

- `for` loop bodies must be indented to avoid an `IndentationError`.

    ```python
        dog_breeds = ["boxer", "bulldog", "shiba inu"]

        # Print each breed:
        for breed in dog_breeds:
            print(breed)
    ```

&nbsp;
## Python Loops with `range()`
***

- In Python, a `for` loop can be used to perform an action a specific number of times in a row.

- The `range()` function can be used to create a list that can be used to specify the number of iterations in a `for` loop.

    ```python
        # Print the numbers 0, 1, 2:
        for i in range(3):
            print(i)

        # Print "WARNING" 3 times:
        for i in range(3):
            print("WARNING")
    ```

&nbsp;
## The Python break Keyword
***

- In a Python loop, the `break` keyword escapes the loop, regardless of the iteration number. Once `break` executes, the program will continue to execute after the loop.

    ```python
        numbers = [0, 254, 2, -1, 3]

        for num in numbers:
            if (num < 0):
                print("Negative number detected!")
                break
            print(num)

        print("Finished looping")

        # Output:
        # 1
        # 25
        # Negative number detected!
        # Finished looping
    ```

&nbsp;
## The Python continue Keyword
***

- In Python, the `continue` keyword is used inside a loop to skip the remaining code inside the loop code block and begin the next loop iteration.

    ```python
        big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]

        # Print only positive numbers:
        for i in big_number_list:
            if i < 0:
                continue
            print(i)
    ```

&nbsp;
## Python While Loops
***

- In Python, a `while` loop will repeatedly execute a code block as long as a condition evaluates to True.

- The condition of a `while` loop is always checked first before the block of code runs. If the condition is not met initially, then the code block will never run.

    ```python
        # This loop will only run 1 time
        hungry = True
        while hungry:
            print("Time to eat!")
            hungry = False

        # This loop will run 5 times
        i = 1
        while i < 6:
            print(i)
            i = i + 1
    ```

&nbsp;
## Python Nested Loops
***

- In Python, loops can be nested inside other loops. Nested loops can be used to access items of lists which are inside other lists.

- The item selected from the outer loop can be used as the list for the inner loop to iterate over.

    ```python
        groups = [["Jobs", "Gates"], ["Newton", "Euclid"], ["Einstein", "Feynman"]]

        # This outer loop will iterate over each list in the groups list
        for group in groups:
            # This inner loop will go through each name in each list
            for name in group:
                print(name)
    ```

&nbsp;
### Python List Comprehension
***

- Python list comprehensions provide a concise way for creating lists.

- It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses: `[EXPRESSION for ITEM in LIST <if CONDITIONAL>]`.

- The expressions can be anything - any kind of object can go into a list.

- A list comprehension always returns a list.

    ```python
        # List comprehension for the squares of all even numbers between 0 and 9
        result = [x**2 for x in range(10) if x % 2 == 0]

        print(result)
        # [0, 4, 16, 36, 64]
    ```