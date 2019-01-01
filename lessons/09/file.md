---
layout: page
title: 09 - Files
---
***

## Reading a File
***

- Computers use file systems to store and retrieve data. Each file is an individual container of related information.

- If you've ever saved a document, downloaded a song, or even sent an email you've created a file on some computer somewhere.

    ```python
        with open('file_name.txt') as cool_doc:
            cool_contents = cool_doc.read()
        print(cool_contents)
    ```

- This opens a file object called `cool_doc` and creates a new indented block where you can read the contents of the opened file.

- We then read the contents of the file `cool_doc` using `cool_doc`.`read()` and save the resulting string into the variable `cool_contents`.

- Then we print `cool_contents`, which outputs the content in the file.

&nbsp;
## Iterating Through Lines
***

- When we read a file, we might want to grab the whole document in a single string, like `.read()` would return.

- But what if we wanted to store each line in a variable? We can use the `.readlines()` function to read a text file line by line instead of having the whole thing.

    ```python
        with open('keats_sonnet.txt') as keats_sonnet:
            for line in keats_sonnet.readlines():
                print(line)
    ```

- The above script creates a temporary file object called `keats_sonnet` that points to the file _keats_sonnet.txt_.

- It then iterates over each line in the document and prints the entire file out.

&nbsp;
## Reading a Line
***

- Sometimes you don't want to iterate through a whole file. For that, there's a different file method, `.readline()`, which will only read a single line at a time.

- If the entire document is read line by line in this way subsequent calls to `.readline()` will not throw an error but will start returning an empty string (`""`).

    ```python
        with open('millay_sonnet.txt') as sonnet_doc:
            first_line = sonnet_doc.readline()
            second_line = sonnet_doc.readline()
            print(second_line)
    ```

- This script also creates a file object called `sonnet_doc` that points to the file __millay_sonnet.txt__.

- It then reads in the first line using `sonnet_doc`.`readline()` and saves that to the variable `first_line`.

- It then saves the second line into the variable `second_line` and then prints it out.

&nbsp;
## Writing a File
***

- Reading a file is all well and good, but what if we want to create a file of our own? With Python we can do just that.

- It turns out that our `open()` function that we're using to open a file to read needs another argument to open a file to write to.

    ```python
        with open('generated_file.txt', 'w') as gen_file:
            gen_file.write("What an incredible file!")
    ```

- Here we pass the argument `'w'` to `open()` in order to indicate to open the file in write-mode.

- The default argument is `'r'` and passing `'r'` to `open()` opens the file in read-mode as we've been doing.

- This code creates a new file in the same folder as the script and gives it the text.

- If there is already a file named same as we're about to create, it will completely overwrite that file, erasing whatever its contents were before.

&nbsp;
## Appending to a File
***

- So maybe completely deleting and overwriting existing files is something that bothers you.

- Instead of opening the file using the argument `'w'` for write-mode, we open it with `'a'` for append-mode.

    ```python
        with open('generated_file.txt', 'a') as gen_file:
            gen_file.write("... and it still is")
    ```

- This code will adds the line as a new line to the file instead of overwrite whole file.

&nbsp;
## What's With "with"?
***

- We've been opening these files with this `with` block so far, but it seems a little weird that we can only use our file variable in the indented block.

- The with keyword invokes something called a _context manager_ for the file that we're calling `open()` on.

- This context manager takes care of opening the file when we call `open()` and then closing the file after we leave the indented block.

- Since your files exist outside your Python script, we need to tell Python when we're done with them so that it can close the connection to that file. If you are not using `with` clause.

- Leaving a file connection open unnecessarily can affect performance or impact other programs on your computer that might be trying to access that file.

- The `with` syntax replaces older ways to access files where you need to call `.close()` on the file object manually.

    ```python
        fun_cities_file = open('fun_cities.txt', 'a')

        # We can now append a line to "fun_cities".
        fun_cities_file.write("Montréal")

        # But we need to remember to close the file
        fun_cities_file.close()
    ```

&nbsp;
## What Is a CSV File?
***

- Text files aren't the only thing that Python can read, but they're the only thing that we don't any need additional parsing library to understand.

- CSV files are an example of a text file that impose a structure to their data. CSV stands for Comma-Separated Values.

- CSV files are usually the way that data from spreadsheet software is exported into a portable format.

- Notice that the first row of the CSV file doesn't actually represent any data, just the labels of the data that's present in the rest of the file.

- The rest of the rows of the file are the same as the rows in the spreadsheet software, just instead of being separated into different cells they're separated by commas.

&nbsp;
## Reading a CSV File
***

- Even though we can read these lines as text without a problem, there are ways to access the data in a format better suited for programming purposes.

- In Python we can convert that data into a dictionary using the `csv` library's `DictReader` object.

- Here's how we'd create a list of the email addresses of all of the users in the db table:

    ```python
        import csv

        list_of_email_addresses = []
        with open('users.csv', newline='') as users_csv:
            user_reader = csv.DictReader(users_csv)
            for row in user_reader:
                list_of_email_addresses.append(row['Email'])
    ```

- We pass the additional keyword argument `newline=''` to the file opening `open()` function so that we don't accidentally mistake a line break in one of our data fields as a new row in our CSV.

- We use csv.DictReader(users_csv) which converts the lines of our CSV file to Python dictionaries.

- The keys of the dictionary are, by default, the entries in the first line of our CSV file.

&nbsp;
## Reading Different Types of CSV Files
***

- We've been acting like CSV files are Comma-Separated Values files. It's true that CSV stands for that, but it's also true that other ways of separating values are valid CSV files these days.

- People used to call Tab-Separated Values files TSV files, but as other separators grew in popularity.

- So we call all files with a list of different values a CSV file and then use different delimiters (like a comma or tab) to indicate where the different values start and stop.

- Let's say we had an address book. Since addresses usually use commas in them, we'll need to use a different delimiter for our information.

- Since none of our data has semicolons (`;`) in them, we can use those.

    ```txt
        Name;Address;Telephone
        Donna Smith\n; House Name, Place\n, Post Office;906-918-6560
        Smith Master\n;House Name, Place\n, Post Office;906-917-8956
    ```

- Notice the `\n` character, this is the escape sequence for a new line.

- The possibility of a new line escaped by a `\n` character in our data is why we pass the `newline=''` keyword argument to the `open()` function.

    ```python
        import csv

        with open('addresses.csv', newline='') as addresses_csv:
            address_reader = csv.DictReader(addresses_csv, delimiter=';')
            for row in address_reader:
                print(row['Address'])
    ```

- The above code will print out all the addresses in this CSV file.

- Notice that when we call `csv.DictReader` we pass in the `delimiter` parameter, which is the string that's used to delineate separate fields in the CSV.

&nbsp;
## Writing a CSV File
***

```python
    import csv

    big_list = [
        {
            'name': 'Fredrick Stein',
            'userid': 6712359021,
            'is_admin': False
        },
        {
            'name': 'Wiltmore Denis',
            'userid': 2525942,
            'is_admin': False
        }
    ]

    with open('output.csv', 'w') as output_csv:
        fields = ['name', 'userid', 'is_admin']
        output_writer = csv.DictWriter(output_csv, fieldnames=fields)

        output_writer.writeheader()
        for item in big_list:
            output_writer.writerow(item)
```

- In our code above we had a set of dictionaries with the same keys for each, a prime candidate for a CSV.

- We import the `csv` library, and then open a new CSV file in write-mode by passing the `'w'` argument to the `open()` function.

- We then define the fields we're going to be using into a variable called `fields`. We then instantiate our CSV writer object and pass two arguments.

- The first is `output_csv`, the file handler object. The second is our list of fields `fields` which we pass to the keyword parameter `fieldnames`.

- We can start adding lines to the file itself! First we want the headers, so we call `.writeheader()` on the writer object.

- Then We call `output_writer`.`writerow()` with the `item` dictionaries which writes each line to the CSV file.

&nbsp;
## Reading a JSON File
***

- We can also use Python's file tools to read and write JSON.

- JSON, an abbreviation of JavaScript Object Notation, is a file format inspired by the programming language JavaScript.

- JSON's format is endearingly similar to Python dictionary syntax, and so JSON files might be easy to read from a Python developer standpoint.

- Nonetheless, Python comes with a `json` package that will help us parse JSON files into actual Python dictionaries.

- Suppose we have a JSON file like the following:

    ```python
        {
            'user': 'ellen_greg',
            'action': 'purchase',
            'item_id': '14781239',
        }
    ```

- We would be able to read that in as a Python dictionary with the following code:

    ```python
        import json

        with open('purchase_14781239.json') as purchase_json:
            purchase_data = json.load(purchase_json)

        print(purchase_data['user'])
        # Prints 'ellen_greg'
    ```

- First we import the `json` package. We opened the file using our trusty `open()` command.

- Since we're opening it in read-mode we just need to pass the file name. We save the file in the temporary variable `purchase_json`.

- We continue by parsing `purchase_json` using `json`.`load()`, creating a Python dictionary out of the file.

- Saving the results into `purchase_data` means we can interact with it.

&nbsp;
## Writing a JSON File
***

- Naturally we can use the `json` library to translate Python objects to JSON as well.

- This is especially useful in instances where you're using a Python library to serve web pages, you would also be able to serve JSON.

- Let's say we had a Python dictionary we wanted to save as a JSON file:

    ```python
        turn_to_json = {
            'eventId': 674189,
            'dateTime': '2015-02-12T09:23:17.511Z',
            'chocolate': 'Semi-sweet Dark',
            'isTomatoAFruit': True
        }
    ```

- We'd be able to create a JSON file with that information by doing the following:

    ```python
        import json

        with open('output.json', 'w') as json_file:
            json.dump(turn_to_json, json_file)
    ```

- We import the `json` module, open up a write-mode file under the variable `json_file`, and then use the `json`.`dump()` method to write to the file.