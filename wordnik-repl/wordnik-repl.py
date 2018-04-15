"""A terminal based vocabulary game."""

import os
import pdb
import sys

import api
import game

PROMPT = 'wordnik repl >> '
EXIT = ['exit', 'exit()', 'quit', 'quit()']
ASK4HELP = ['-h', '--help', 'help']
HELP = """Help under construction. Use CTRL-C to exit."""
GAME_LISTS = [
    'master',
    'known',
    'unknown',
]


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


def pdb_time(message):
    """Warn dev of an error, but don't exit."""
    print('[ERROR] {} -- please enter pbd'.format(message))


def repl(session):
    """Main input/output loop."""
    while True:
        if session.header:
            print(session.header)
        if session.flush is True:
            session.flush = False
            print(session.out)
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
        self.flush = True
        self.prompt = PROMPT
        self.header = 'The wordnik repl interface, alpha sub 0.0.1'
        self.out = 'Type "begin" to start the game (alpha)'
        self.menu = {}
        self.api = api.ApiHandler(self.wnu, self.wnp, self.wnk)
        self.master_dict = {}

    def test(self):
        """Test."""
        print('WORKS!')

    def begin(self):
        """Command for user to start game."""
        if self.master_dict == {}:
            self._startGame()
            self.out = ("Words should have printed above as they were being "
                        "defined.\nRecommendation: enter `pdb` from the wordnik "
                        "repl and type `session.master_dict`.")
            self.master_dict = self._buildDictionary(self.permalinks['master'])
        self.current_game = game.Game(self.master_dict)
        self.current_game.play()
        print("\nGame over")

    def _startGame(self):
        """Get words from lists and invoke game."""
        self._getPermalinks()

    def _getPermalinks(self):
        """Construct permaLinks names from existing wordlists."""
        all_lists = self.api.wordLists()
        permalinks = {}
        for key, value in all_lists.items():
            if key.lower() in GAME_LISTS:
                permalinks[key.lower()] = value
        if len(permalinks) is not 3:
            pdb_time("permalinks not == 3")
        self.permalinks = permalinks

    def _buildDictionary(self, permalink):
        """Look up all definitions."""
        word_list = self.api.wordsOnList(permalink)
        word_dict = {}
        for word in word_list:
            word_dict[word] = self.api.defineWord(word)
            print(word)
        print('\nDone!')
        return word_dict

    def _saveResults(self):
        """Save game score."""
        pass


session = Session()
repl(session)
