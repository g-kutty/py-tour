---
layout: page
title:
---
***

## Lists
***

- __Lists__ are a _data structure_ you can use to store a collection of different pieces of information as a sequence under a single variable name.

    ```python
    list_name = [item_1, item_2]
    ```

- A list can also be empty: _empty_list = []_

&nbsp;
## Access by Index
***

- You can access an individual item on the list by its `index`. An index is like an address that identifies the item's place in the list.

- The index appears directly after the list name, in between brackets, like this: `list_name[index]`.

- List indices begin with `0`, not `1!`.

&nbsp;
## New Neighbors
***

- A list index behaves like any other variable name! It can be used to access as well as assign values.

    ```python
    # List
    zoo_animals = ["dog", "cat", "elephant", "lion"]
    ```

- You can access a list index like this:

    ```python
    # Gets the value "dog"
    zoo_animals[0]
    ```

- You can do assignment with index like this:

    ```python
    # Changes "elephant" to "bear"
    zoo_animals[2] = "bear"
    ```

&nbsp;
## Late Arrivals & List Length
***

- A list doesn't have to have a fixed length. You can add items to the end of a list any time you like!

    ```python
    letters = ['a', 'b', 'c']
    letters.append('d')
    print len(letters)
    print letters
    ```

  1. In the above example, we first create a list called `letters`.

  2. Then, we add the string `'d'` to the end of the _letters_ list.

  3. Next, we print out `4`, the length of the _letters_ list.

  4. Finally, we print out _['a', 'b', 'c', 'd']_

&nbsp;
## List Slicing
***

- Sometimes, you only want to access a portion of a list. Consider the following code:

    ```python
    letters = ['a', 'b', 'c', 'd', 'e']
    slice = letters[1:3]
    print slice
    print letters
    ```

  1. First, we create a list called `letters`.

  2. Then, we take a subsection of the list and store it in the slice list.

  3. we include the element with the `first` index, but we exclude the element with the `second` index.

- You can slice a string exactly like a `list!` In fact, you can think of strings as lists of characters.

&nbsp;
## Maintaining Order
***

- Sometimes you need to search for an item in a list.

    ```python
    animals = ["dog", "cattle", "tiger"]
    print animals.index("cattle")
    ```

  1. First, we create a list called `animals` with three strings.

  2. Then, we print the first index that contains the string `cattle`, which will print `1`.

- We can also `insert` items into a list.

    ```python
    animals.insert(1, "dog")
    print animals
    ```

  1. We insert `dog` at index `1`, which moves everything down by `1`.

  2. We print out _["ant", "dog", "bat", "cat"]_

&nbsp;
## For One and All
***

- If you want to do something with every item in the list, you can use a __for loop__.

    ```python
    for variable in list_name:
        # Do stuff!
    ```

- A variable name follows the `for` keyword; it will be assigned the value of each list item in turn.

- The line ends with a colon (`:`) and the indented code that follows it will be executed once per item in the list.

- If your list is a jumbled mess, you may need to `sort()` it.

    ```python
    animals = ["cat", "ant", "bat"]
    animals.sort()

    for animal in animals:
        print animal
    ```

    1. First, we create a list called `animals` with three strings. The strings are not in alphabetical order.

    2. Then, we sort _animals_ into alphabetical order. Note that `.sort()` modifies the list rather than returning a new list.

    3. Then, for each item in _animals_, we print that item out as _"ant", "bat", "cat"_ on their own line each.

&nbsp;
## Remove a Few Things
***

- Sometimes you need to remove something from a `list`.

- There is many ways to remove item from list:

  1. `list.pop(index)` will remove the item at index from the list and return it to you:

        ```python
            n = [1, 3, 5]

            # Returns 3 (the item at index 1)
            v = n.pop(1)

            # Print 3
            print v

            # Prints [1, 5]
            print n
        ```

  2. `list.remove(item)` will remove the actual item if it finds it:

        ```python
            # Removes 1 from the list,
            # NOT the item at index 1
            n.remove(1)

            # Prints [3, 5]
            print n
        ```

  3. `del(n[1])` is like `.pop` in that it will remove the item at the given index, but it won't return it:

        ```python
            # Doesn't return anything
            del(n[1])

            # Prints [1, 5]
            print n
        ```

&nbsp;
## Passing a range into a function
***

- In Python `range()` function is just a shortcut for generating a list, so you can use ranges in all the same places you can use lists.

    ```python
        range(6) # => [0, 1, 2, 3, 4, 5]
        range(1, 6) # => [1, 2, 3, 4, 5]
        range(1, 6, 3) # => [1, 4]
    ```

- The range function has three different versions:

    1) range(stop)

    2) range(start, stop)

    3) range(start, stop, step)

- In all cases, the `range()` function returns a list of numbers from `start` up to (but not including) `stop`. Each item increases by `step`.

- If omitted, `start` defaults to `0` and `step` defaults to `1`.