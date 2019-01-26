---
layout: page
title: 11 - Isolated Environments
---
***

## Virtual Environment
***

- A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated python virtual environments for them.

- ### Why do we need a virtual environment?

  - Imagine a scenario where you are working on two web based python projects and one of them uses a Django 1.9 and the other uses Django 1.10 and so on.
  
  - In such situations virtual environment can be really useful to maintain dependencies of both the projects.

- ### When and where to use a virtual environment?

  - By default, every project on your system will use these same directories to store and retrieve site packages.

  - This is a real problem for Python since it can’t differentiate between versions in the “site-packages” directory. So both v1.9 and v1.10 would reside in the same directory with the same name.

  - This is where virtual environments come into play. To solve this problem, we just need to create two separate virtual environments for both the projects.

  - The great thing about this is that there are no limits to the number of environments you can have since they’re just directories containing a few scripts.

  - Virtual Environment should be used whenever you work on any Python based project. It is generally good to have one new virtual environment for every Python based project you work on.
  
  - So the dependencies of every project are isolated from the system and each other.
