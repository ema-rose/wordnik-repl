# Useful Resources

This is a living document to collect effective resources and best practices into one location. Please update and expand this document as additional or improved resources for the project are found.

## Python

Python is an interpreted general purpose programing language that is comparatively easy to read and learn given its syntax and large community.

Often an introductory text to a language can serve as a good reference for basic syntax and usage guidance. One that is contained within a single page, making it easy to search within your browser, is Dave Kuhlman's [A Python Book](http://www.davekuhlman.org/python_book_01.html).

The [python standard library documentation](https://docs.python.org/3/library/index.html) can be very helpful, though a general recommendation is to use it for a more detailed understanding after getting more general concepts and use cases from the text mentioned above or from other resources listed in the General section below.

Given the size and complexity of the python docs, the [overapi.com index](http://overapi.com/python) can be a good way to quickly find the part of the python documentation you are looking for.

Your own collection of completed exercises can also be a useful source of "documentation", and one that you can expand and refine as your experience grows.

One of the main benefits of python is its readability, which is improved when developers follow the same conventions on how to format python files for humans -- called `style` even though the python interpreter would be able to read the code with many alternate style conventions.

Checking code against agreed conventions and using tools to check the code for simple errors of syntax or use is often called `linting`. This project will use `flake8` and `pylint` as linting tools. A helpful resource for addressing the style issues raised by these tools is [google's python style guide](https://google.github.io/styleguide/pyguide.html).

## git

[Basic git commands](https://services.github.com/on-demand/downloads/github-git-cheat-sheet/)

[git docs](https://git-scm.com/doc) which includes other cheat sheets as well as videos.

## Bash (shell)

Bash (and git) have extensive documentation built into the Command Line Interface. For bash, if you want to remind yourself how a command like `ls` works, simply type `man ls` where the first token is short for "manual" and the second token is the command you wish to see the reference on. 

Within the "man" page, you can navigate forward and backward using the arrow keys, and you can "jump" forward using the space bar.As with vim, the man page may be searched using the `/` symbol, as in `/find_me` with `n` then taking us to the "next" match, and `q` will "quit" the man page view.

## Editors & IDE

Most developers have preferences for one -- or sometimes a small number -- of editing tools for working with code. 

Some of these tools are referred to as "editors" while others are referred to as an "Integrated Development Environment" or "IDE". Generally an IDE will be a richer interface, have more tooling and 'help' built in and/or enabled by default, and may be language or platform specific.

The "right" tool(s) to use are those that make the developer most productive. Many python developers find [pycharm](https://google.github.io/styleguide/pyguide.html) an effective python IDE, and almost all developers use "vi" or ["vim"](https://vim.sourceforge.io/docs.php) when interacting with code from the CLI. This is in part because `vim` or `vi` (an earlier version of the same kind of editor) is present/easy to install on most any system.

Though considered an "editor", `vim` has a large community and extensive functionality/plugins that can make it an appropriate tool for even large complex projects. 

These two tools are as good as any others for a new python programmer. Start with them, focus on getting the project completed, and then explore other tools and use the ones that make you the most productive. When working closely with other developers who are highly proficient with a tool you don't know, that can be an excellent opportunity to learn that tool and ease collaboration.

All tools have `key bindings`, meaning key combinations that produce behavior without having to navigate with the mouse or through many menus. Many IDEs offer "vim bindings" since vim is broadly used. A good introduction to the vim bindings is the game [Vim Adventures](https://vim-adventures.com/).

Many searches for `how to x in vim` will land you on the [vim tips wiki](http://vim.wikia.com/wiki/Vim_Tips_Wiki).

A video based resource that has been helpful is [vimcasts.org](http://vimcasts.org/episodes/).

Pycharm offers extensive [documentation and videos](https://www.jetbrains.com/pycharm/documentation/) for developers new to their tool.

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
