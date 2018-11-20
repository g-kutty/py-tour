---
layout: page
title:
---
***

## Why Use Classes?
***

- Python is an object-oriented programming language, which means it manipulates programming constructs called `objects`.

- You can think of an object as a single data structure that contains data as well as functions.

- The functions of an object are called its methods. For example,

    ```python
        len("Eric")
    ```

- Python is checking to see whether the string object you passed it has a length, and if it does, it returns the value associated with that attribute.

- When you call:

    ```python
        my_dict.items()
    ```

- Python checks to see if `my_dict` has an `items()` method (which all dictionaries have) and executes that method if it finds it.

- A class is just a way of organizing and producing objects with similar attributes and methods.

&nbsp;
## Class Syntax
***

- A basic class consists only of the `class` keyword, the name of the class, and the class from which the new class `inherits` in parentheses.

    ```python
        class NewClass(object):
            # Class magic here
    ```

- This gives them the powers and abilities of a Python object. By convention, user-defined Python class names start with a capital letter.

- `__init__()`. This function is required for classes, and it's used to initialize the objects it creates.

- `__init__()` always takes at least one argument, `self`, that refers to the object being created.

- This is a Python convention; there's nothing magic about the word `self`. However, it's overwhelmingly common to use _self_ as the first parameter in `__init__()`, so you should do this so that other people will understand your code.

- Python will use the first parameter that `__init__()` receives to refer to the object being created; this is why it's often called `self`, since this parameter gives the object being created its identity.

&nbsp;
## Instantiating Your First Object
***

- We can access attributes of our objects using dot notation. Here's how it works:

    ```python
        class Square(object):
            def __init__(self):
                self.sides = 4

        my_shape = Square()
    ```

    1. First we create a class named `Square` with an attribute `sides`.

    2. Outside the class definition, we create a new instance of `Square` named `my_shape` and access that attribute using `my_shape.sides`.

&nbsp;
## Class Scope
***

- Another important aspect of Python classes is scope. The scope of a variable is the context in which it's visible to the program.

- When dealing with classes, you can have `variables` that are available everywhere (`global` variables), variables that are only available to members of a certain class (`member` variables), and variables that are only available to particular instances of a class (`instance` variables)

- When a class has its own functions, those functions are called `methods`. You've already seen one such method: `__init__()`. But you can also define your own methods!

&nbsp;
## They're Multiplying!
***

- A class can have any number of `member variables`. These are variables that are available to all members of a class.

    ```python
        class Animal(object):
            """Animal class represent animals category and their features"""

            def __init__(self, name, age):
                self.name = name
                self.age = age
                self.is_alive = True

        # Create instance of class Animal
        hippo = Animal("Jake", 12)
        cat = Animal("Boots", 3)

        # Print member variable
        print(hippo.is_alive)

        # Modify member variable value
        hippo.is_alive = False

        # Print again
        print(hippo.is_alive)
        print(cat.is_alive)
    ```

    1. In the example above, we create two instances of an `Animal`.

    2. Then we print out `True`, the default value stored in hippo's `is_alive` member variable.

    3. Next, we set that to `False` and print it out to make sure.

    4. Finally, we print out `True`, the value stored in cat's `is_alive` member variable. We only changed the variable in hippo, not in cat.

&nbsp;
## It's Not All Animals and Fruits
***

- However, classes and objects are often used to model real-world objects.

- Here we have a basic `ShoppingCart` class for creating shopping cart objects for website customers; though basic, it's similar to what you'd see in a real program.

    ```python
    class ShoppingCart(object):
    """Create shopping cart objects for users of our fine website"""

        def __init__(self, customer_name):
            self.customer_name = customer_name
            self.items_in_cart = {}

        def add_item(self, product, price):
            """Add new product to the cart"""

            if product not in self.items_in_cart:
                self.items_in_cart[product] = price
                print(product + " added.")
            else:
                print(product + " is already in the cart.")

        def remove_item(self, product):
            """Remove item from the cart"""

            if product in self.items_in_cart:
                del self.items_in_cart[product]
                print(product + " removed.")
            else:
                print(product + " is not in the cart.")

    my_cart = ShoppingCart("George")
    my_cart.add_item("Keyboard", 150)
    my_cart.remove_item("Keyboard")
    ```

&nbsp;
## Warning: Here Be Dragons
***

- Inheritance is a tricky concept, so let's go through it step by step.

- Inheritance is the process by which one class takes on the attributes and methods of another, and it's used to express an is-a relationship.

- For example, a `Panda` is a bear, so a Panda class could inherit from a `Bear` class.

&nbsp;
## Inheritance Syntax
***

- In Python, inheritance works like this:

    ```python
        class DerivedClass(BaseClass):
            # code goes here
    ```

- `DerivedClass` is the new class you're making and `BaseClass` is the class from which that new class inherits.

&nbsp;
## Override!
***

- Sometimes you'll want one class that inherits from another to not only take on the methods and attributes of its parent, but to _override_ one or more of them.

    ```python
        class Employee(object):
            """Parent class"""

            def __init__(self, name):
                self.name = name

            def great(self, other):
                print("Hello %s" % other.name)

        class CEO(Employee):
            """Child class inherit  parent class Employee"""

            def great(self, other):
                print("Get back to work, %s" % other.name)

        ceo = CEO("Tony")
        emp = Employee("George")
        emp.great(ceo)
        emp.great(emp)
    ```

- Rather than have a separate `greet_underling` method for our CEO. we override (or re-create) the `greet` method on top of the base `Employee.greet` method.

&nbsp;
## This Looks Like a Job For...
***

- On the flip side, sometimes you'll be working with a derived class (or _subclass_) and realize that you've overwritten a method or attribute defined in base class (also called a parent or _superclass_) that you actually need.

- Have no fear! You can directly access the attributes or methods of a super class with Python's built-in `super` call.

- The syntax looks like this:

    ```python
        class Derived(Base):
            def m(self, input):
                return super(Derived, self).m(input)
    ```

- Where `m()` is a method from the base class.