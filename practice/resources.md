# Useful Resources

This is a living document to collect effective resources and best practices into one location. Please update and expand this document as additional or improved resources for the project are found.

## Python

Python is an interpreted general purpose programing language that is comparatively easy to read and learn given its syntax and large community.

Often an introductory text to a language can serve as a good reference for basic syntax and usage guidance. One that is contained within a single page, making it easy to search within your browser, is Dave Kuhlman's [A Python Book](http://www.davekuhlman.org/python_book_01.html).

The [python standard library documentation](https://docs.python.org/3/library/index.html) can be very helpful, though a general recommendation is to use it for a more detailed understanding after getting more general concepts and use cases from the text mentioned above or from other resources listed in the General section below.

Given the size and complexity of the python docs, the [overapi.com index](http://overapi.com/python) can be a good way to quickly find the part of the python documentation.

Your own collection of completed exercises can also be a useful source of "documentation", and one that you can expand and refine as your experience grows.

## git

[Basic git commands](https://services.github.com/on-demand/downloads/github-git-cheat-sheet/)

[git docs](https://git-scm.com/doc) which includes other cheat sheets as well as videos.

## Bash (shell)

Bash (and git) have extensive documentation built into the Command Line Interface. For bash, if you want to remind yourself how a command like `ls` works, simply type `man ls` where the first token is short for "manual" and the second token is the command you wish to see the reference on. 

Within the "man" page, you can navigate forward and backward using the arrow keys, and you can "jump" forward using the space bar.As with vim, the man page may be searched using the `/` symbol, as in `/find_me` with `n` then taking us to the "next" match, and `q` will "quit" the man page view.

## General

[Mastering Markdown](https://guides.github.com/features/mastering-markdown/)

# Patterns and problem solving tips

## names and naming conventions

When naming files, functions and variables use names that are descriptive of what the contents do or are for.

## Use comments and doc strings

In addition to clear and descriptive names, use comments and "doc strings" to make code easier to understand.

```
def greeter_func(name):
    """Accepts a name and issues a greeting if the name is a string."""
    if type(name) is str:
        print("Hello " + name + ", nice to meet you!")
    else:
        # print a clear error message
        print("Error: name must be a string")
```

## Use iPython as your REPL for checking a python command
