---
layout: page
title: 11 - File Input/Output
---
***

- If you want to read information from a file on your computer, and/or write that information to another file? This process is called `file I/O` (the "I/O" stands for "input/output")

&nbsp;
## The open() Function
***

- Let's walk through the process of writing to a file one step at a time.

    ```python
        f = open("output.txt", "w")
    ```

- This told Python to open `output.txt` in `"w"` mode ("w" stands for "write"). We stored the result of this operation in a file object, `f`.

&nbsp;
## Writing
***

- We can write to a Python file like so:

    ```python
        my_file.write("Data to be written")
    ```

- The `.write()` method takes a string argument, so we'll need to do a few things here:

- You must close the file. You do this simply by calling `my_file.close()`

- If you don't close your file, Python won't write to it properly.

&nbsp;
## Reading
***

- Finally, we want to know how to read from our `output.txt` file. As you might expect, we do this with the `read()` function, like so:

    ```python
        print my_file.read()
    ```

&nbsp;
## Reading Between the Lines
***

- What if we want to read from a file line by line, rather than pulling the entire file in at once. Thankfully, Python includes a `.readline()` method that does exactly that.

- If you open a file and call `.readline()` on the file object, you'll get the first line of the file. subsequent calls to .readline() will return successive lines.

&nbsp;
## PSA: Buffering Data
***

- We keep telling you that you always need to close your files after you're done writing to them. Here's why!

- During the I/O process, data is _buffered_: this means that it is held in a temporary location before being written to the file.

- Python doesn't _flush the buffer_ — that is, write data to the file — until it's sure you're done writing.

- If you write to a file without closing, the data won't make it to the target file.

&nbsp;
## The 'with' and 'as' Keywords
***

- There is a way to get Python to automatically close our files.

- You may not know this, but file objects contain a special pair of built-in methods: `__enter__()` and `__exit__()`.

- The details aren't important, but what is important is that when a file object's `__exit__()` method is invoked, it automatically closes the file.

- How do we invoke this method? With with and as. The syntax looks like this:

    ```python
        with open("file", "mode") as variable:
            # Read or write to the file
    ```

&nbsp;
## Case Closed?
***

- Finally, we'll want a way to test whether a file we've opened is closed. Sometimes we'll have a lot of file objects open, and if we're not careful, they won't all be closed. How can we test this?

    ```python
        f = open("bg.txt")
        f.closed
        # False
        f.close()
        f.closed
        # True
    ```

- Python file objects have a `closed` attribute which is `True` when the file is closed and `False` otherwise.

- By checking `file_object.closed`, we'll know whether our file is closed and can call `close()` on it if it's still open.