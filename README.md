# Beyond the Basic Stuff with Python

Examples and exercises from Beyond the Basic Stuff with Python by Al Sweigart

A free version of the book can be found at [https://inventwithpython.com/beyond/](https://inventwithpython.com/beyond/).

## Introduction

- [Learn X in Y minutes Where X = Python](https://learnxinyminutes.com/docs/python/)
- [Python Crash Course - Cheat Sheets](https://ehmatthes.github.io/pcc/cheatsheets/README.html)

Recommended reading:


- Python Crash Course (No Starch Press, 2019) by Eric Matthes
- Impractical Python Projects (No Starch Press, 2018) by Lee Vaughan
- Serious Python (No Starch Press, 2018) by Julien Danjou

Further reading:

- Effective Python (Addison-Wesley Professional, 2019) by Brett Slatkin
- Python Cookbook (O’Reilly Media, 2013) by David Beazley and Brian K. Jones
- Fluent Python (O’Reilly Media, 2021) by Luciano Ramalho

---

Part I - Getting Started

---

## Chapter 1 - Dealing with Errors and Asking for Help

- [Python Help](https://www.python.org/about/help/)
- [How do I as a good question on Stack Overflow](https://stackoverflow.com/help/how-to-ask/)
- [Learn Python at Reddit](https://www.reddit.com/r/learnpython/)

## Chapter 2 - Environment Setup and the Command Line

```python
from pathlib import Path
Path.home()     # home directory of user
Path.cwd()      # current working directory
```

Recommended reading for using the command line:

- The Linux Command Line, 2nd Edition (2019) by William Shotts, 
- Linux Basics for Hackers (2018) by OccupyTheWeb,
- PowerShell for Sysadmins (2020) by Adam Bertram

History command on MS Windows:

```bash
doskey /history
```

List subfolder contents on MS Windows:

```bash
dir /s *.py
```

List subfolder contents on macOS and Linux:

```bash
find . -name "*.py"
```

Viewing environment variables with `set` (on Windows) or `env` (on macOS and Linux).

View the current path variable with `path` (on Windows) or `echo $PATH` (on macOS and Linux).

---

Part 2 - Best Practices, Tools, and Techniques

---

## Chapter 3 - Code Formatting with Black

- [PEP 8 - Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
- [Black](https://github.com/psf/black/)

## Chapter 4 - Choosing Understandable Names

