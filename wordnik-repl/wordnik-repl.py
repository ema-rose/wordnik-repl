"""A terminal based vocabulary game."""

import os
import pdb
import sys

import api

PROMPT = 'wordnik repl >> '
EXIT = ['exit', 'exit()', 'quit', 'quit()']
ASK4HELP = ['-h', '--help', 'help']
HELP = """Help under construction. Use CTRL-C to exit."""
GAME_LISTS = {
    'master': '',
    'known': '',
    'unknown': ''
}


def call_method(target_class, target_method):
    """Provide access to objects through the repl."""
    try:
        method = getattr(target_class, target_method)
    except AttributeError:
        print(
            'Class `{}` has no method `{}`'.format(
                target_class.__class__.__name__, target_method
            )
        )
        return
    method()


def repl(session):
    """Main input/output loop."""
    while True:
        iterate = input(session.prompt).strip().lower()
        if iterate in ASK4HELP:
            print(HELP)
            continue
        if iterate in EXIT:
            sys.exit()
        else:
            if iterate == 'cls':
                clear_screen()
                continue
            if iterate == 'pdb':
                pdb.set_trace()
                continue
        call_method(session, iterate)
        if session.out is not '':
            print(session.out)


def clear_screen():
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
        self.prompt = PROMPT
        self.out = ''
        self.menu = {}
        self.api = api.ApiHandler(self.wnu, self.wnp, self.wnk)

    def test(self):
        """Test."""
        print('WORKS!')

    def begin(self):
        """Command for user to start game."""
        self._startGame()
        self.out = self.permalinks

    def _startGame(self):
        """Get words from lists and invoke game."""
        self._getPermalinks()

    def _saveResults(self):
        """Save game score."""
        pass

    def _getPermalinks(self):
        """Construct permaLinks names from existing wordlists."""
        self.permalinks = self.api.wordLists()


repl(Session())
