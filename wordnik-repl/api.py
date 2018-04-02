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
