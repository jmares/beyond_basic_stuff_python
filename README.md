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

- [PEP8 - Naming Conventions](https://www.python.org/dev/peps/pep-0008/#naming-conventions)

## Chapter 5 - Finding Code Smells

A *code smell* is a source code pattern that signals potential bugs.

Examples:

- duplicate code
- magic numbers
- commented-out code and dead code
- print debugging
- variables with numeric suffixes
- classes that should just Be functions or modules
- list comprehensions within list comprehensions
- empty except blocks and poor error messages

## Chapter 6 - Writing Pythonic Code

```python
import this
```

>**The Zen of Python**  
> \- by *Tim Peters*  
>   
>Beautiful is better than ugly.   
>Explicit is better than implicit.   
>Simple is better than complex.   
>Complex is better than complicated.   
>Flat is better than nested.  
>Sparse is better than dense.  
>Readability counts.  
>Special cases aren't special enough to break the rules.  
>Although practicality beats purity.  
>Errors should never pass silently.  
>Unless explicitly silenced.  
>In the face of ambiguity, refuse the temptation to guess.  
>There should be one-- and preferably only one --obvious way to do it.  
>Although that way may not be obvious at first unless you're Dutch.  
>Now is better than never.  
>Although never is often better than *right* now.  
>If the implementation is hard to explain, it's a bad idea.  
>If the implementation is easy to explain, it may be a good idea.   
>Namespaces are one honking great idea -- let's do more of those!  

Examples

- Use `enumerate()` instead of `range()`
- Use the `with` statement instead of `open()` and `close()`
- Use `is` to compare with `None` instead of `==`
- Use raw strings if your string has many backslashes
- Format strings with f-strings
- Making shallow copies of lists
- Use `get()` and `setdefault()` with dictionaries
- Use `collections.defaultdict` for default values
- Use dictionaries instead of a `switch` statement
- Python’s ugly ternary operator
- Chaining assignment and comparison operators

## Chapter 7 - Programming Jargon

```python
def spam():
    print('Spam! Spam! Spam!')

spam()
# Spam! Spam! Spam!

nospam = spam
nospam()
# Spam! Spam! Spam!

def twice(func):
    func()
    func()

twice()
# Spam! Spam! Spam!
# Spam! Spam! Spam!
```

## Chapter 8 - Common Python Gotchas

- Don’t add or delete items from a list while looping over it.    

The best practice is to create a new list rather than modifying an existing one.   

- Don’t copy mutable values without `copy.copy()` and `copy.deepcopy()`.    

Use `copy.copy()` for a list and `copy.deepcopy()` for a list of lists.

- Don’t use mutable values for default arguments.

Using a mutable object (e.g. a list) for the default argument has a subtle problem: the list is created when the function’s def statement executes, not each time the function is called. Any changes made to that list when the function is called, will affect the function the next time it is called.

- Don’t build strings with string concatenation

The pythonic way to build strings is to append the smaller strings to a list and then join the list together into one string.   
See script `buildstrings.py`.

- Don’t expect `sort()` to sort alphabetically

```python
letters = ['z', 'A', 'a', 'Z']
letters.sort(key=str.lower)
```

- Don’t assume floating-point numbers are perfectly accurate

If exact precision is needed, use the `decimal` module.

- Don’t chain inequality `!=` operators

- Don’t forget the comma in single-item tuples

## Chapter 9 - Esoteric Python Oddities

- Preallocated integers
- String interning
- Python’s fake increment and decrement operators
- `all(list)` as evaluating the claim “none of the items in this list are falsey”
- Boolean values are integer values
- Chaining multiple kinds of operators
- Python’s antigravity feature