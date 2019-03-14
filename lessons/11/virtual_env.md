---
layout: page
title:
---
***

## Virtual Env
***

- __Virtualenv__ is a tool to create isolated python environments.

- Virtualenv creates a folder which contains all the necessary executables to use the packages that a python project would need.

&nbsp;
## Usage
***

- Install virtualenv via pip

    ```python
        pip install virtualenv
    ```

- You can create a virtualenv using the following command:

  ```python
      virtualenv env_name
  ```

- After running this command, a directory named `env_name` will be created. This is the directory which contains all the necessary executables to use the packages that a python project would need.

- This is where python packages will be installed. If you want to specify python interpreter of your choice, for example python 3, It can be done using the following command:

  ```python
      virtualenv -p /usr/bin/python3 virtualenv_name
  ```

- Now after creating virtual environment, you need to `activate` it. Remember to activate the relevant virtual environment every time you work on the project. This can be done using the following command:

  ```python
      source virtualenv_name/bin/activate
  ```

- Once the virtual environment is activated, the name of your virtual environment will appear on left side of terminal. This will let you know that the virtual environment is currently active.

- Now you can install `dependencies` related to the project in this virtual environment. For example if you are using Flask 1.0.1 for a project, you can install it like you install other packages.

  ```python
      pip install Flask==1.0.1
  ```

- The Flask 1.0.1 package will be placed in virtualenv_name folder and will be isolated from the complete system.

- Once you are done with the work, you can `deactivate` the virtual environment by the following command:

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