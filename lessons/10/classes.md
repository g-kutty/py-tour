---
layout: page
title: 10 - Classes
---
***

## Types
***

- Python equips us with many different ways to store data.

- A `float` is a different kind of number from an `int`, and we store different data in a `list` than we do in a `dict`. These are known as different _types_.

- We can check the type of a Python variable using the `type()` function.

    ```python
        a_string = "Cool String"
        an_int = 12

        print(type(a_string))
        # prints "<class 'str'>"

        print(type(an_int))
        # prints "<class 'int'>"
    ```

- Above, we defined two variables, and checked the `type` of these two variables. A variable's type determines what you can do with it and how you can use it.

- You can't `.get()` something from an integer, just as you can't add two dictionaries together using `+`. This is because those operations are defined at the `type` level.

&nbsp;
## Class
***

- A _class_ is a template for a data type. It describes the kinds of information that class will hold and how a programmer will interact with that data.

- Define a class using the class keyword. [PEP 8 Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/#class-names) recommends capitalizing the names of classes to make them easier to identify.

    ```python
        class CoolClass:
            pass
    ```

- In the above example we created a class and named it `CoolClass`.

- We used the `pass` keyword in Python to indicate that the body of the class was intentionally left blank so we don't cause an `IndentationError`.

&nbsp;
## Instantiation
***

- A class doesn't accomplish anything simply by being defined. A class must be instantiated.

- In other words, we must create an _instance_ of the class, in order to breathe life into the schematic.

- Instantiating a class looks a lot like calling a function. We would be able to create an instance of our defined `CoolClass` as follows:

    ```python
        cool_instance = CoolClass()
    ```

- Above, we created an object by adding parentheses to the name of the class. We then assigned that new instance to the variable `cool_instance` for safe-keeping.

&nbsp;
## Object-Oriented Programming
***

- A class instance is also called an _object_. The pattern of defining classes and creating objects to represent the responsibilities of a program is known as _Object Oriented Programming_ or OOP.

- Instantiation takes a class and turns it into an object, the `type()` function does the opposite of that. When called with an object, it returns the class that the object is an instance of.

    ```python
        print(type(cool_instance))
        # prints "<class '__main__.CoolClass'>"
    ```

- We then print out the `type()` of `cool_instance` and it shows us that this object is of type `__main__.CoolClass`.

- In Python `__main__` means "this current file that we're running" and so one could read the output from `type()` to mean "the class `CoolClass` that was defined here, in the script you're currently running."

&nbsp;
## Class Variables
***

- When we want the same data to be available to every instance of a class we use a _class variable_.

- A class variable is a variable that's the same for every instance of the class.

- You can define a class variable by including it in the indented part of your class definition, and you can access all of an object's class variables with `object`.`variable` syntax.

    ```python
        class Musician:
            title = "Rockstar"

        drummer = Musician()
        print(drummer.title)
        # prints "Rockstar"
    ```

- Above we defined the class `Musician`, then instantiated `drummer` to be an object of type `Musician`.

- We then printed out the drummer's `.title` attribute, which is a class variable that we defined as the string "Rockstar".

- If we defined another musician, like `guitarist = Musician()` they would have the same `.title` attribute.

&nbsp;
## Methods
***

- _Methods_ are functions that are defined as part of a class. The first argument in a method is always the object that is calling the method.

- Convention recommends that we name this first argument `self`. Methods always have at least this one argument.

- We define methods similarly to functions, except that they are indented to be part of the class.

    ```python
        class Dog():
            dog_time_dilation = 7

            def time_explanation(self):
                print("Dogs experience {} years for every 1 human year.".format(self.dog_time_dilation))

        pipi_pitbull = Dog()
        pipi_pitbull.time_explanation()
        # Prints "Dogs experience 7 years for every 1 human year."
    ```

- Above we created a `Dog` class with a `time_explanation` method that takes one argument, `self`, which refers to the object calling the function.

- We created a `Dog` named `pipi_pitbull` and called the `.time_explanation()` method on our new object for Pipi.

- Notice we didn't pass any arguments when we called `.time_explanation()`, but were able to refer to `self` in the function body.

- When you call a method it automatically passes the object calling the method as the first argument.

&nbsp;
## Methods with Arguments
***

- Methods can also take more arguments than just `self`:

    ```python
        class DistanceConverter:
            kms_in_a_mile = 1.609
            def how_many_kms(self, miles):
                return miles * self.kms_in_a_mile

        converter = DistanceConverter()
        kms_in_5_miles = converter.how_many_kms(5)
        print(kms_in_5_miles)
        # prints "8.045"
    ```

- Above we defined a `DistanceConverter` class, instantiated it, and used it to convert 5 miles into kilometers.

- Notice again that even though `how_many_kms` takes two arguments in its definition, we only pass miles, because self is implicitly passed.

&nbsp;
## Constructors
***

- There are several methods that we can define in a Python class that have special behavior.

- These methods are sometimes called "magic", because they behave differently from regular methods.

- Another popular term is _dunder_ methods, so-named because they have two underscores (double-underscore abbreviated to "dunder") on either side of them.

- The first dunder method we're going to use is the `__init__` method.  This method is used to _initialize_ a newly created object. It is called every time the class is instantiated.

- Methods that are used to prepare an object being instantiated are called _constructors_.

- The word "constructor" is used to describe similar features in other object-oriented programming languages.

- But programmers who refer to a constructor in Python are usually talking about the `__init__` method.

    ```python
        class Shouter:
            def __init__(self):
                print("HELLO?!")

        shout1 = Shouter()
        # prints "HELLO?!"

        shout2 = Shouter()
        # prints "HELLO?!"
    ```

- Above we created a class called `Shouter` and every time we create an instance of `Shouter` the program prints out a shout.

- Pay careful attention to the instantiation syntax we use. `Shouter()` looks a lot like a function call, doesn't it? If it's a function, can we pass parameters to it?

- We absolutely can, and those parameters will be received by the `__init__` method.

    ```python
        class Shouter:
            def __init__(self, phrase):
                # make sure phrase is a string
                if type(phrase) == str:

                    # then shout it out
                    print(phrase.upper())

        shout1 = Shouter("shout")
        # prints "SHOUT"

        shout2 = Shouter("shout")
        # prints "SHOUT"

        shout3 = Shouter("let it all out")
        # prints "LET IT ALL OUT"
    ```

- Above we've updated our `Shouter` class to take the additional parameter phrase. When we created each of our objects we passed an argument to the constructor.

- The constructor takes the argument `phrase` and, if it's a string, prints out the all-caps version of `phrase`.

&nbsp;
## Instance Variables
***

- Instance variables are owned by instances of the class. This means that for each object or instance of a class, the instance variables are different.

- Unlike class variables, instance variables are defined within methods.

- In the `Shark` class example below, `name` and `age` are instance variables:

    ```python
        class Shark:
            def __init__(self, name, age):
                self.name = name
                self.age = age
    ```

- When we create a Shark object, we will have to define these variables, which are passed as parameters within the constructor method or another method.

    ```python
        class Shark:
            def __init__(self, name, age):
                self.name = name
                self.age = age

        new_shark = Shark("Sammy", 5)
    ```

- As with class variables, we can similarly call to print instance variables:

    ```python
        class Shark:
            def __init__(self, name, age):
                self.name = name
                self.age = age

        new_shark = Shark("Sammy", 5)
        print(new_shark.name)
        print(new_shark.age)
    ```

&nbsp;
## Attribute Functions
***

- Instance variables and class variables are both accessed similarly in Python. This is no mistake, they are both considered _attributes_ of an object.

- If we attempt to access an attribute that is neither a class variable nor an instance variable of the object Python will throw an `AttributeError`.

    ```python
        class NoCustomAttributes:
            pass

        attributeless = NoCustomAttributes()

        try:
            attributeless.fake_attribute
        except AttributeError:
            print("This text gets printed!")

        # prints "This text gets printed!"
    ```

- What if we aren't sure if an object has an attribute or not?

- `getattr()` is a Python function that works a lot like the usual dot-syntax but we can supply a third argument that will be the default if the object does not have the given attribute.

- What if we only really care whether the attribute exists? `hasattr()` will return `True` if an object has a given attribute and `False` otherwise.

- Calling those functions looks like this:

    ```python
        hasattr(attributeless, "fake_attribute")
        # returns False

        getattr(attributeless, "other_fake_attribute", 800)
        # returns 800, the default value
    ```

&nbsp;
## Self
***

- Since we can already use dictionaries to store key-value pairs, using objects for that purpose is not really useful.

- Instance variables are more powerful when you can guarantee a rigidity to the data the object is holding.

- This convenience is most apparent when the constructor creates the instance variables, using the arguments passed into it.

- If we were creating a search engine, and we wanted to create classes for each separate entry we could return. We'd do that like this:

    ```python
        class SearchEngineEntry:
            def __init__(self, url):
                self.url = url

        codecademy = SearchEngineEntry("www.codecademy.com")
        wikipedia = SearchEngineEntry("www.wikipedia.org")

        print(codecademy.url)
        # prints "www.codecademy.com"

        print(wikipedia.url)
        # prints "www.wikipedia.org"
    ```

- Since the `self` keyword refers to the object and not the class being called, we can define a `secure` method on the `SearchEngineEntry` class that returns the secure link to an entry.

    ```python
        class SearchEngineEntry:
            secure_prefix = "https://"
            def __init__(self, url):
                self.url = url

            def secure(self):
                return "{prefix}{site}".format(prefix=self.secure_prefix, site=self.url)
    ```

- Above we define our `secure()` method to take just the one required argument, `self`. We access both the class variable `self`.`secure_prefix` and the instance variable `self`.`url` to return a secure URL.

- This is the strength of writing object-oriented programs. We can write our classes to structure the data that we need and write methods that will interact with that data in a meaningful way.

&nbsp;
## Everything is an Object
***

- Attributes can be added to user-defined objects after instantiation, so it's possible for an object to have some attributes that are not explicitly defined in an object's constructor.

- We can use the `dir()` function to investigate an object's attributes at runtime.

- `dir()` is short for directory and offers an organized presentation of object attributes.

    ```python
        class FakeDict:
            pass

        fake_dict = FakeDict()
        fake_dict.attribute = "Cool"

        dir(fake_dict)
        # Prints ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'attribute']
    ```

- That's certainly a lot more attributes than we defined! Python automatically adds a number of attributes to all objects that get created.

- These internal attributes are usually indicated by double-underscores. But sure enough, `attribute` is in that list.

- Do you remember being able to use `type()` on Python's native data types? This is because they are also objects in Python. Their classes are `int`, `float`, `str`, `list`, and `dict`.

    ```python
        fun_list = [10, "string", {'abc': True}]

        type(fun_list)
        # Prints <class 'list'>

        dir(fun_list)
        # Prints ['__add__', '__class__', [...], 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
    ```

- Above we define a new list. We check it's type and see that's an instantiation of class `list`.

- We use `dir()` to explore its attributes, and it gives us a large number of internal Python dunder attributes, but, afterward, we get the usual list methods.

&nbsp;
## String Representation
***

- One of the first things we learn as programmers is how to print out information that we need for debugging.

- Unfortunately, when we print out an object we get a default representation that seems fairly useless.

    ```python
        class Employee():
            def __init__(self, name):
                self.name = name

        argus = Employee("Argus Filch")
        print(argus)
        # prints "<__main__.Employee object at 0x104e88390>"
    ```

- This default string representation gives us some information, like where the class is defined and our computer's memory address where this object is stored.

- We learned about the dunder method `__init__`. Now, we will learn another dunder method called `__repr__`.

- This is a method we can use to tell Python what we want the _string representation_ of the class to be.

- `__repr__` can only have one parameter, `self`, and must return a string.

- In our `Employee` class above, we have an instance variable called `name` that should be unique enough to be useful when we're printing out an instance of the `Employee` class.

    ```python
        class Employee():
            def __init__(self, name):
                self.name = name

            def __repr__(self):
                return self.name

        argus = Employee("Argus Filch")
        print(argus)
        # prints "Argus Filch"
    ```

- We implemented the `__repr__` method and had it return the `.name` attribute of the object. When we printed the object out it simply printed the `.name` of the object! Cool!