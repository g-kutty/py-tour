---
layout: page
title:
---
***

## Virtual Env
***

- We use a module named __virtualenv__ which is a tool to create isolated Python environments.

- virtualenv creates a folder which contains all the necessary executables to use the packages that a Python project would need.

- ### Installing virtualenv

    ```python
        pip install virtualenv
    ```
- ### Test your installation:

    ```python
        virtualenv --version
    ```

- ### Using virtualenv

  - You can create a virtualenv using the following command:

    ```python
        virtualenv my_name
    ```

  - After running this command, a directory named my_name will be created. This is the directory which contains all the necessary executables to use the packages that a Python project would need.

  - This is where Python packages will be installed. If you want to specify Python interpreter of your choice, for example Python 3, it can be done using the following command:

    ```python
        virtualenv -p /usr/bin/python3 virtualenv_name
    ```

  - Now after creating virtual environment, you need to activate it. Remember to activate the relevant virtual environment every time you work on the project. This can be done using the following command:

    ```python
        source virtualenv_name/bin/activate
    ```

  - Once the virtual environment is activated, the name of your virtual environment will appear on left side of terminal. This will let you know that the virtual environment is currently active.

  - Now you can install dependencies related to the project in this virtual environment. For example if you are using Django 1.9 for a project, you can install it like you install other packages.

    ```python
        pip install Django==1.9
    ```

  - The Django 1.9 package will be placed in virtualenv_name folder and will be isolated from the complete system.

  - Once you are done with the work, you can deactivate the virtual environment by the following command:

    ```python
        deactivate
    ```

  - We can collect all package information in the isolated environment into one file using command:

    ```sh
        pip freeze --local > requirements.txt
    ```

  - For installing all required packages form `requirement.txt` into another isolated environment or machine.

    ```sh
        pip install -r requirements.txt --no-index --find-links file:///tmp/packages
    ```

  - `--no-index` - Ignore package index (only looking at `--find-links` URLs instead).

  - `-f`, `--find-links` <URL> - If a URL or path to an html file, then parse for links to archives. If a local path or file:// URL that's a directory, then look for archives in the directory listing.