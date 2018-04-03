"""Module to handle calls to the wordnik API."""

import requests


BASE_URI = 'https://api.wordnik.com/v4'


def sanity():
    """tbd."""
    print('Sanity from the API module.')


def full_uri(resource, method, sub_method=''):
    """Construct full URI.

    Paramater names may be confusing because wordnik api is not consistent.
    """
    if sub_method:
        return '{}/{}.json/{}/{}'.format(
            BASE_URI, resource, method, sub_method
        )
    else:
        return '{}/{}.json/{}'.format(BASE_URI, resource, method)


class ApiHandler(object):
    """Interface to wordnik API that manages its own tokens."""

    def __init__(self, user, pw, key):
        """Request initial token."""
        self.user = user
        self.pw = pw
        self.headers = {'api_key': key}
        self.headers['auth_token'] = self._refresh_token()

    @staticmethod
    def _api_error(message, req):
        """API error output."""
        base_msg = '\n[ERROR] {} Status: {} on url: {} returned: {}'
        print(base_msg.format(
            message,
            req.status_code,
            req.url,
            req.content
        ))

    def _refresh_token(self):
        uri = full_uri('account', 'authenticate', self.user)
        req = requests.post(uri, headers=self.headers, data=self.pw)
        if req.status_code == 200:
            print('\n[INFO] (re)Authenticated.')
            return req.json()['token']
        else:
            self._api_error('Unable to authenticate.', req)

    def wordLists(self):
        """Return dict of name, permalink."""
        uri = full_uri('account', 'wordLists')
        req = requests.get(uri, headers=self.headers)
        if req.status_code == 200:
            wordlists = {}
            for json_object in req.json():
                wordlists[json_object['name']] = json_object['permalink']
            return wordlists
        else:
            self._api_error('Unable to retrieve word lists.', req)

    def wordsOnList(self, permalink):
        """Return list of words given a permalink."""
        uri = full_uri('wordList', permalink, 'words')
        req = requests.get(uri, headers=self.headers)
        if req.status_code == 200:
            words = []
            for json_object in req.json():
                words.append(json_object['word'])
            return words
        else:
            self._api_error('Unable to retrieve words on wordlist.', req)

    def defineWord(self, word):
        """Return the longest definition for a word."""
        uri = full_uri('word', word, 'definitions')
        req = requests.get(uri, headers=self.headers)
        if req.status_code == 200:
            length = len(req.json())
            for json_object in req.json():
                if length == 1:
                    return json_object['text']
                i = 0
                the_def = ''
                while i < length:
                    if len(json_object['text']) > len(the_def):
                        the_def = json_object['text']
                    i += 1
            return the_def
        else:
            self._api_error('Unable to get definition.', req)
