---
layout: page
title: 12 - Isolated Environments
---
***

## Virtual Env
***

- [virtualenv](https://pypi.org/project/virtualenv/) is a very popular tool that creates isolated Python environments for Python libraries.

- It works by installing a bunch of files in a directory (eg: `env/`), and then modifying the `PATH` environment variable to prefix it with a custom bin directory (eg: `env/bin/`).

- An exact copy of the `python` or `python3` binary is placed in this directory, but Python is programmed to look for libraries relative to its path first, in the environment directory.

- It's not part of Python's standard library, but is officially blessed by the PyPA (Python Packaging Authority). Once activated, you can install packages in the virtual environment using `pip`.

&nbsp;
## Steps for setup
***

- We can install `virtualenv` package in your local machine using `pip`.

    ```sh
        pip install virtualenv
    ```

- For creating isolated environment for each projects:

    ```sh
        virtualenv project_name
    ```

- Then `activate` newly created environment for that project:

    ```sh
        source ./env/bin/activate
    ```

- We can simply `deactivate` this isolated environment and go back to default global environment by typing `deactivate` on terminal.

    ```sh
        deactivate
    ```

- For collecting all package information in the isolated environment into one file:

    ```sh
        pip freeze --local > requirements.txt
    ```

- Also we can install all required packages form `requirement.txt` into another isolated environment or machine.

    ```sh
        pip install -r requirements.txt --no-index --find-links file:///tmp/packages
    ```

  - `--no-index` - Ignore package index (only looking at `--find-links` URLs instead).

  - `-f`, `--find-links` <URL> - If a URL or path to an html file, then parse for links to archives. If a local path or file:// URL that's a directory, then look for archives in the directory listing.