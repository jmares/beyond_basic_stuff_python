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

## Chapter 10 - Effective Functions

**Function Names**:

Descriptive and containing a verb.

**Function Size Trade-Offs**:

**Function Parameters and Arguments**

- Default Arguments
- Using * and ** to Pass Arguments to Functions
- Using * to Create Variadic Functions
- Using ** to Create Variadic Functions
- Using * and ** to Create Wrapper Functions

**Functional Programming**

Functional programming is a programming paradigm that emphasizes writing functions that perform calculations without modifying global variables or any external state.

- Side Effects
- Higher-Order Functions
- Lambda Functions
- Mapping and Filtering with List Comprehensions

To define a Python lambda function, use the lambda keyword, followed by a comma-delimited list of parameters (if any), a colon, and then an expression that acts as the return value. Because functions are first-class objects, you can assign a lambda function to a variable, effectively replicating what a def statement does.

**Return Values Should Always Have the Same Data Type**

**Raising Exceptions vs. Returning Error Codes**

## Chapter 11 - Comments, Docstrings, and Type Hints

> “Programs must be written for people to read,     
> and only incidentally for machines to execute.”   

**Comments**

```python
# This is a single-line comment.

"""This is a
multiline string that
also works as a multiline comment. """
```

Codetags

| Tag    | Description     | 
|:------ |:--------------- |
| #TODO  | Introduces a general reminder about work that needs to be done |
| #FIXME | Introduces a reminder that this part of the code doesn’t entirely work |
| #HACK  | Introduces a reminder that this part of the code works, perhaps barely, but that the code should be improved |
| #XXX   | Introduces a general warning, often of high severity |


**Docstrings**

Docstrings are multiline comments that appear either at the top of a module’s `.py` source code file or directly following a `class` or `def` statement.

```python
def get(self, url, **kwargs):
    """Sends a GET request. Returns :class:`Response` object.

    :param url: URL for the new :class:`Request` object.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :rtype: requests.Response
    """
...
```

**Type Hints**

```python
def describeNumber(number: int) -> str:
    if number % 2 == 1:
        return 'An odd number. '
    elif number == 42:
        return 'The answer. '
    else:
        return 'Yes, that is a number. '

myLuckyNumber: int = 42
print(describeNumber(myLuckyNumber))
```

Although Python supports syntax for type hints, the Python interpreter completely ignores them. You will need to install a third-party type checker like Mypy.

To specify type hints with multiple types, import `Union` from the built-in `typing` module.

```python
from typing import Union
spam: Union[int, str, float] = 42
spam = 'hello'
spam = 3.14
```

## Chapter 12 - Organizing Your Code Projects with Git

- Use [cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.3/) to create new (complex) Python projects
- [Pro Git by Scott Charcon](https://git-scm.com/book/en/v2)
- [Version Control by Example by Eric Sink]()

## Chapter 13 - Measuring Performance and Big O Algorithm Analysis

Modules used:

- `timeit`: for small snippets of code
- `cProfile`: for entire functions or programs

Code from book to test cProfile

```python
import cProfile, rsaCipher
cProfile.run("rsaCipher.encryptAndWriteToFile('encrypted_file.txt', 'al_sweigart_pubkey.txt', 'abc'*100000)")
```

**Big O Algorithm Analysis**

> How code slows as data grows.

## Chapter 14 - Practice Projects

1. The Tower of Hanoi
2. Four in a Row

## Chapter 15 - Object-Oriented Programming and Classes

The `__qualname__` attribute:

```python
>>> type(42)  # The object 42 has a type of int.
<class 'int'>
str(type(42))  # Passing the type object to str() returns a messy string.
"<class 'int'>"
>>> type(42).__qualname__ # The __qualname__ attribute is nicer looking.
'int'
```

# Chapter 16 - Object-Oriented Programming and Inheritance

> Creating multiple levels of inheritance doesn’t add organization  
>so much as bureaucracy to your code.