---
layout: page
title:
---
***

## Installing Pipenv
***

- __Pipenv__ is a tool that aims to bring the best of all packaging worlds (bundler, composer, npm, cargo, yarn, etc.) to the Python world.

- It automatically creates and manages a virtualenv for your projects, as well as adds/removes packages from your `Pipfile` as you install/uninstall packages.

- It also generates the ever-important `Pipfile.lock`, which is used to produce deterministic builds.

- The problems that Pipenv seeks to solve are multi-faceted:

  - You no longer need to use `pip` and `virtualenv` separately. They work together.

  - Managing a `requirements.txt` file can be problematic, so Pipenv uses `Pipfile` and `Pipfile.lock` to separate abstract dependency declarations from the last tested combination.

  - Hashes are used everywhere, always. Security. Automatically expose security vulnerabilities.

  - Strongly encourage the use of the latest versions of dependencies to minimize security risks arising from outdated components.

  - Give you insight into your dependency graph (e.g. `pipenv graph`).

  - Streamline development workflow by loading `.env` files.

&nbsp;
## Pipenv Features
***

- Enables truly _deterministic_ builds, while easily specifying _only what you want_.

- Generates and checks file hashes for locked dependencies.

- Automatically install required Pythons, if `pyenv` is available.

- Automatically finds your project home, recursively, by looking for a `Pipfile`.

- Automatically generates a `Pipfile`, if one doesn’t exist.

- Automatically creates a virtualenv in a standard location.

- Automatically adds/removes packages to a `Pipfile` when they are un/installed.

- Automatically loads `.env` files, if they exist.

The main commands are _install_, _uninstall_, and _lock_, which generates a `Pipfile.lock`. These are intended to replace `pip install` usage, as well as manual virtualenv management (to activate a virtualenv, run `pipenv shell`).

&nbsp;
## Basic Concepts
***

- A virtualenv will automatically be created, when one doesn’t exist.

- When no parameters are passed to `install`, all packages [`packages`] specified will be installed.

- To initialize a Python 3 virtual environment, run $ `pipenv --three`.

- To initialize a Python 2 virtual environment, run $ `pipenv --two`.

- Otherwise, whatever virtualenv defaults to will be the default.

&nbsp;
## Other Commands
***

- `graph` will show you a dependency graph of your installed dependencies.

- `shell` will spawn a shell with the virtualenv activated. This shell can be deactivated by using `exit`.

- `run` will run a given command from the virtualenv, with any arguments forwarded (e.g. $ _pipenv run python_ or $ _pipenv run pip freeze_).

- `check` checks for security vulnerabilities and asserts that PEP 508 requirements are being met by the current environment.