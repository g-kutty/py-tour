---
layout: page
title:
---
***

## Dictionary
***

- A __dictionary__ is similar to a list, but you access values by looking up a `key` instead of an `index`. A key can be any string or number.

- Dictionaries are enclosed in curly braces, like so:

    ```python
        d = {'key1' : 1, 'key2' : 2, 'key3' : 3}
    ```

- This is a dictionary called `d` with three key-value pairs. The key `key1` points to the value _1_, `key2` to _2_, and so on.

- Dictionaries are great for things like phone books (pairing a name with a phone number), login pages (pairing an e-mail address with a username), and more!

&nbsp;
## New Entries
***

- Like Lists, Dictionaries are `mutable`. This means they can be changed after they are created.

- One advantage of this is that we can add new `key/value` pairs to the dictionary after it is created like so:

    ```python
        dict_name[new_key] = new_value
    ```

- An empty pair of curly braces `{}` is an empty dictionary, just like an empty pair of `[]` is an empty list.

- The length `len()` of a dictionary is the number of key-value pairs it has.

&nbsp;
## Changing Your Mind
***

- Because dictionaries are mutable, they can be changed in many ways. Items can be removed from a dictionary with the `del` command:

    ```python
        del dict_name[key_name]
    ```

- will remove the key `key_name` and its associated value from the dictionary.

- A new value can be associated with a key by assigning a value to the key, like so:

    ```python
        dict_name[key] = new_value
    ```