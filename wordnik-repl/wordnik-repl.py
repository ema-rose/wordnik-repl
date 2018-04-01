"""A terminal based vocabulary game."""

import sys
import os

import api

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
            if iterate == 'pdb':
                import pdb
                pdb.set_trace()
            print('... under construction ...')


def cls():
    """Cross platform screen clear."""
    os.system('cls' if os.name == 'nt' else 'clear')


def env_check(var):
    """Check for env var."""
    try:
        key = os.environ[var]
    except KeyError as err:
        if var in str(err):
            print('[ERROR] No {} env var provided.'
                  ' Please set and restart.'.format(var))
            exit(1)
        else:
            raise err
    return key


class Session(object):
    """An instance of the repl."""

    def __init__(self):
        """Set up a session to own user and run games."""
        self.wnp = env_check('WNP')
        self.wnu = env_check('WNU')
        self.wnk = env_check('WNK')
        self.api = api.ApiHandler(self.wnu, self.wnp, self.wnk)


api.sanity()
session = Session()
repl(session)
