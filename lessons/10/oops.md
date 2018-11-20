---
layout: page
title: 10 - OOP
---
***

## Class basics
***

- [Classes](https://g-kutty.github.io/py-tour/lessons/10/class) can be very useful for storing complicated objects with their own methods and variables.

- Defining a class is much like defining a function, but we use the `class` _keyword_ instead. We also use the word `object` in _parentheses_ because we want our classes to inherit the object class.

- This means that our class has all the properties of an object, which is the simplest, most basic class.

    ```python
        class ClassName(object):
            # Class statements go here
    ```

&nbsp;
## Initializing a class
***

- There is a special function named `__init__()` that gets called whenever we create a new instance of a class. It exists by default, even though we don't see it.

- However, we can define our own `__init__()` function inside the class, overwriting the default version.

- We might want to do this in order to provide more input variables, just like we would with any other function.

- The first argument passed to `__init__()` must always be the keyword `self` - this is how the object keeps track of itself internally, but we can pass additional variables after that.

- In order to assign a variable to the class, we use `dot` notation.

- For instance, if we passed new variable into our class, inside the `__init__()` function we would say:

    ```python
        self.new_variable = new_variable
    ```

&nbsp;
## Create an instance of a class
***

- We can use classes to create new objects, which we say are `instances` of those classes.

- Creating a new instance of a class is as easy as saying:

    ```python
        newObject = ClassName()
    ```

&nbsp;
## Class member variables
***

- Classes can have `member` variables that store information about each class object.

- We call them member variables since they are information that belongs to the class object.

- Creating member variables and assigning them initial values is as easy as creating any other variable:

    ```python
        class ClassName(object):
            memberVariable = "initialValue"
    ```

&nbsp;
## Referring to member variables
***

- Calling class member variables works the same whether those values are created within the class or values are passed into the new object at initialization.

- We use _dot_ notation to access the member variables of classes since those variables belong to the object.

- For instance, if we had created a member variable named `new_variable`, a new instance of the class named `new_object` could access this variable by saying:

    ```python
        new_object.new_variable
    ```

&nbsp;
## Modifying member variables
***

- We can modify variables that belong to a class the same way that we initialize those member variables.

- This can be useful when we want to change the value a variable takes on based on something that happens inside of a class method.

&nbsp;
## Creating class methods
***

- Besides member variables, classes can also have their own methods. For example:

    ```python
        class Square(object):
            def __init__(self, side):
                self.side = side

            def perimeter(self):
                return self.side * 4
    ```

- The `perimeter()` class method is identical to defining any other function, except that it is written inside of the `Square` class definition.

&nbsp;
## Inheritance
***

- One of the benefits of classes is that we can create more complicated classes that __inherit__ variables or methods from their _parent classes_.

- This saves us time and helps us build more complicated objects, since these _child classes_ can also include additional variables or methods.

    ```python
        class ChildClass(ParentClass):
            # new variables and functions go here
    ```

- Normally we use `object` as the parent class because it is the most basic type of class, but by specifying a different class, we can inherit more complicated functionality.

&nbsp;
## Overriding methods
***

- __Overriding__ is the property of a class to change the implementation of a method provided by one of its base classes.

- Overriding is a very important part of OOP since it makes inheritance utilize its full power. By using method overriding a class may _"copy"_ another class, avoiding duplicated code, and at the same time enhance or customize part of it.

- In Python method overriding occurs by simply defining in the child class  a method with the same name of a method in the parent class.

    ```python
        class Parent(object):
            """Parent class"""

            def __init__(self):
                self.value = 4

            def get_value(self):
                return self.value

        class Child(Parent):
            """Child class inherit Parent class"""

            def get_value(self):
                return self.value + 1
    ```

&nbsp;
## Building useful classes
***

- Chances are, you won't be designing Car _classes_ in the real world anytime soon. Usually, classes are most useful for holding and accessing abstract collections of data.

- One useful class method to override is the built-in `__repr__()` method, which is short for _representation_.

- By providing a return value in this method, we can tell Python how to represent an object of our class.

    ```python
        class Point3D(object):
            """3D representation of points"""

            def __init__(self, x, y, z):
                self.x = x
                self.y = y
                self.z = z

            def __repr__(self):
                return "(%d, %d, %d)" % (self.x, self.y, self.z)

        my_point = Point3D(1, 2, 3)
        print(my_point)
    ```