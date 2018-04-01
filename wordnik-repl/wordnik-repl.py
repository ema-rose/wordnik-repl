"""A terminal based vocabulary game."""

import sys
import os

import api

sanity = 'Sanity!'  # TODO remove
PROMPT = 'wordnik repl >> '
EXIT = ['exit', 'exit()', 'quit', 'quit()']
ASK4HELP = ['-h', '--help', 'help']
HELP = """Help under construction. Use CTRL-C to exit."""
GAME_LISTS = {
    'alpha': '',
    'beta': '',
    'gamma': '',
    'delta': '',
    'epsilon': ''
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


def repl(session, prompt=PROMPT, out='', cls=False):
    """Main input/output loop."""
    while True:
        iterate = input(PROMPT).strip().lower()
        if iterate in ASK4HELP:
            print(HELP)
            continue
        if iterate in EXIT:
            sys.exit()
        else:
            if iterate == 'cls':
                clear_screen()
            if out is not '':
                print(out)
            if iterate == 'pdb':
                import pdb
                pdb.set_trace()
            # print('... under construction ...')
            call_method(session, iterate)


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
        self.api = api.ApiHandler(self.wnu, self.wnp, self.wnk)

    def test(self):
        """Test."""
        print('WORKS!')


session = Session()
repl(session)
