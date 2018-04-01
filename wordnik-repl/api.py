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
        self.token = self._refresh_token()

    def _refresh_token(self):
        uri = full_uri('account', 'authenticate', self.user)
        req = requests.post(uri, headers=self.headers, data=self.pw)
        if req.status_code == 200:
            print('\n[INFO] (re)Authenticated.')
            return req.json()['token']
        else:
            print('\n[ERROR] Unable to authenticate. Status: {}  '
                  'Content: {}'.format(req.status_code, req.content))
