---
layout: page
title:
---
***

- __Frozen set__ is just an `immutable` version of a Python set object. While elements of a set can be modified at any time, elements of frozen set remains the same after creation.

    ```python
        # Tuple of vowels
        vowels = ('a', 'e', 'i', 'o', 'u')

        fSet = frozenset(vowels)
        print('The frozen set is:', fSet)
    ```