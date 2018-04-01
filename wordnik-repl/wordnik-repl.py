"""A terminal based vocabulary game."""

import sys
import os


sanity = 'Sanity!'  # TODO remove
PROMPT = 'wordnik repl >> '
EXIT = ['exit', 'exit()', 'quit', 'quit()']
ASK4HELP = ['-h', '--help', 'help']
HELP = """Help under construction. Use CTRL-C to exit."""


def repl(Session, prompt=PROMPT, out='', cls=False):
    """Main input/output loop."""
    while True:
        iterate = input(PROMPT)
        if iterate.strip().lower() in ASK4HELP:
            print(HELP)
            continue
        if iterate.strip().lower() in EXIT:
            sys.exit()
        else:
            if cls:
                cls()
            if out is not '':
                print(out)
            print('No help')


def cls():
    """Cross platform screen clear."""
    os.system('cls' if os.name == 'nt' else 'clear')


class Session(object):
    """An instance of the repl."""

    def __init__(self):
        """Set up a session to own user and run games."""
        self._check4user()

    def _check4user(self):
        """Create user from env vars or from prompt."""
        print(sanity)

session = Session()
repl(session)
