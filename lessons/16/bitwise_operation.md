---
layout: page
title: 16 - Bitwise Operations
---
***

## Just a Little BIT
***

- __Bitwise operations__ might seem a little esoteric and tricky at first, but you'll get the hang of them pretty quickly.

- Bitwise operations are operations that directly manipulate bits. In all computers, numbers are represented with bits, a series of zeros and ones. In fact, pretty much everything in a computer is represented by bits.

    ```python
        print 5 >> 4  # Right Shift
        print 5 << 1  # Left Shift
        print 8 & 5   # Bitwise AND
        print 9 | 4   # Bitwise OR
        print 12 ^ 42 # Bitwise XOR
        print ~88     # Bitwise NOT
    ```

&nbsp;
## The Base 2 Number System
***

- When we count, we usually do it in base 10. That means that each place in a number can hold one of ten values, 0-9.

- In _binary_ we count in _base two_, where each place can hold one of two values: 0 or 1.

- Each place in a decimal number represents a power of _ten_, where each place in a binary number represents a power of two.

- The rightmost bit is the 1's bit(two to the zero power),  the next bit is the 2's bit(two to the first), then 4, 8, 16, 32, and so on.

- The binary number '1010' is 10 in base 2 because the 8's bit and the 2's bit are _"on"_:

    ```python
        8's bit   4's bit   2's bit   1's bit
        1         0         1         0
        8    +    0    +    2    +    0  = 10
    ```

- In Python, you can write numbers in binary format by starting the number with `0b`. When doing so, the numbers can be operated on like any other number!

    ```python
        print 0b1,    #1
        print 0b10,   #2
        print "\nsum = ", 0b1 + 0b10
    ```

&nbsp;
## The bin() Function
***

- There are Python functions that can aid you with bitwise operations. In order to print a number in its binary representation, you can use the `bin()` function.

- Takes an integer as input and returns the binary representation of that integer in a string.(Keep in mind that after using the bin function, you can no longer operate on the value like a number.)

- You can also represent numbers in base 8 and base 16 using the `oct()` and `hex()` functions.

&nbsp;
## int()'s Second Parameter
***

- What you might not know is that the int function actually has an optional second parameter.

    ```python
        int("110", 2)
        # ==> 6
    ```

- When given a string containing a number and the base that number is in, the function will return the value of that number converted to corresponding base.

&nbsp;
## Slide to the Left! Slide to the Right
***

- The next two operations we are going to talk about are the left and right shift bitwise operators.

    ```python
        # Left Bit Shift (<<)  
        0b000001 << 2 == 0b000100 (1 << 2 = 4)
        0b000101 << 3 == 0b101000 (5 << 3 = 40)

        # Right Bit Shift (>>)
        0b0010100 >> 3 == 0b000010 (20 >> 3 = 2)
        0b0000010 >> 2 == 0b000000 (2 >> 2 = 0)
    ```

- Shift operations are similar to rounding down after dividing and multiplying by 2 (respectively).

- Note that you can only do bitwise operations on an `integer`. Trying to do them on _strings_ or _floats_ will result in nonsensical output!

&nbsp;
## Binary AND
***

- The bitwise AND (`&`) operator compares two numbers on a bit level and returns a number where the bits of that number are turned on if the corresponding bits of `both` numbers are 1.

    ```python
         a:   00101010   42
         b:   00001111   15
      ===================
     a & b:   00001010   10
    ```

&nbsp;
## Binary OR
***

- The bitwise OR (`|`) operator compares two numbers on a bit level and returns a number where the bits of that number are turned on if either of the corresponding bits of either number are 1.

    ```python
        a:  00101010  42
        b:  00001111  15
    ================
    a | b:  00101111  47
    ```

- Note that the bitwise `|` operator can only create results that are greater than or equal to the larger of the two integer inputs.

&nbsp;
## Binary XOR
***

- The XOR (`^`) or exclusive or operator compares two numbers on a bit level and returns a number where the bits of that number are turned on if `either` of the corresponding bits of the two numbers are `1`, _but not both_.

    ```python
            a:  00101010   42
            b:  00001111   15
        ================
        a ^ b:  00100101   37
    ```

&nbsp;
## Binary NOT
***

- The bitwise NOT operator (`~`) just flips all of the bits in a single number.

- What this actually means to the computer is actually very complicated, so we're not going to get into it.

- Just know that mathematically, this is equivalent to adding one to the number and then making it negative.

&nbsp;
## The Man Behind the Bit Mask
***

- A bit mask is just a variable that aids you with bitwise operations.

- A bit mask can help you turn specific bits on, turn others off, or just collect data from an integer about which bits are on or off.

    ```python
        num  = 0b1100
        mask = 0b0100
        desired = num & mask
        if desired > 0:
            print "Bit was on"
    ```

- In the example above, we want to see if the third bit from the right is on.

    1. First, we first create a variable num containing the number `12`, or `0b1100`.

    2. Next, we create a `mask` with the `third` bit on.

    3. Then, we use a bitwise _AND_ operation to see if the third bit from the right of `num` is `on`.

    4. If `desired` is greater than zero, then the third bit of `num` must have been one.

&nbsp;
## Turn It On
***

- You can also use masks to turn a bit in a number on using `|`.

    ```python
        a = 0b110 # 6
        mask = 0b1 # 1
        desired =  a | mask # 0b111, or 7
    ```

- Using the bitwise `|` operator will turn a corresponding bit on if it is off and leave it on if it is already on.

&nbsp;
## Just Flip Out
***

- Using the XOR (`^`) operator is very useful for flipping bits.

    ```python
        a = 0b110 # 6
        mask = 0b111 # 7
        desired =  a ^ mask # 0b1
    ```

&nbsp;
## Slip and Slide
***

- Finally, you can also use the left shift (<<) and right shift (>>) operators to slide masks into place.

    ```python
        a = 0b101
        # Tenth bit mask
        mask = (0b1 << 9)
        desired = a | mask
    ```

- Let's say that I want to turn on the 10th bit from the right of the integer `a`.

- Instead of writing out the entire number, we slide a bit over using the `<<` operator.

- We use 9 because we only need to slide the mask nine places over from the first bit to reach the tenth bit.