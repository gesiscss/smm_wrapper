"""Summary
"""
from typing import Union


import os
import requests

from . import __version__


class SMMAPI:

    """The APIs provide provenance and change information about the tokens a Wikipedia article consists of, for several languages. Apart from the source language edition they draw from, their specifications and usage are identical

    Attributes:
        attempts (int): Number of attempts to be done to the server
        base (url): Base request url
        base_editor (TYPE): Description
        session (TYPE): Description
    """

    def __init__(self,
                 username: str=None,
                 password: str=None,
                 api_key: str=None,
                 lng: str="en",
                 protocol: str="http",
                 domain: str="10.6.13.139:8000",
                 version: str="v1",
                 attempts: int=2):
        """Constructor of the SMMAPI

        Args:
            username (str, optional): SMM API username
            password (str, optional): SMM API password
            api_key (str, optional): SMM API key
            lng (str, optional): the language that needs to be query
            protocol (str, optional): the protocol of the url
            domain (str, optional): the domain that hosts the api
            version (str, optional): the version of the api
            attempts (int, optional): the number of attempts before giving up trying to connect
        """

        self.session = requests.Session()
        if username and password:
            self.session.auth = (username, password)

        if api_key:
            self.session.params = {}
            self.session.params['api_key'] = api_key

        self.base = "{}://{}/api/politicians/".format(protocol, domain)
        self.attempts = attempts

    def get_politicians(self):
        """Returns a list of all entities of politicians.

        No input parameters

        Returns:
            list: result of the api query as documented in Entity list in 
                http://10.6.13.139:8000/politicians/api/politicians/
        """

        smm_api_politicians_url = '{}all/'.format(self.base)

        # return the dictionary
        return self.request(smm_api_politicians_url)

    def politician_search(self, names_contain = None, politician_id = None):
        """Returns either a list with politicians based on the text search or a given politician by id 

        Input parameters:
                        names_contain (str): Search text in first name, last name, Twitter or Facebook screen names, or Wikipedia titles
                        OR
                        politician_id (int): A unique value identifying this politician.

        Returns:
            names_contain: returns a list of all entities searched by names, firstnames and usernames
            politician_id: returns a given politician by id
        """
        if names_contain is not None:
            url = '{}all/search/'.format(self.base)
            parameters={'names_contain': names_contain}
        elif politician_id is not None:
            url = '{}all/{}/'.format(self.base, politician_id)
            parameters = {}

        return self.session.get(url=url, params=parameters).json()

    def tweets_by(self, twitter_user_id=None, politician_id=None, text_contains=None, from_date=None, to_date=None, aggregate_by='month'):
        """Returns query tweets made by politicians, or by a politician using twitter id or using politician id

        Input parameters:
                        twitter_user_id (str): twitter user id
                        OR
                        politician_id (str): A unique value identifying this politician.
                        optional:
                        text_contains (str): filter tweets by the content of the message
                        from_date (string($date)): filter by tweets posted after this date (format: YYYY-MM-DD)
                        to_date (string($date)): filter by tweets posted before this date (format: YYYY-MM-DD)
                        aggregate_by (str): criteria that will be used to aggregate (month by default)

        Returns:
            dict, result of the api query as documented in twitter tweets_by/reply_to content in http://10.6.13.139:8000/politicians/api/swagger/
        """
        if twitter_user_id is None and politician_id is None:
            url = '{}twitter/tweets_by/politicians/'.format(self.base)
            parameters={'text_contains': text_contains, 'from_date': from_date, 'to_date':to_date, 'aggregate_by': aggregate_by}
        elif twitter_user_id is not None:
            url = '{}twitter/tweets_by/politicians/user_id/{}/'.format(self.base, twitter_user_id)
            parameters={'text_contains': text_contains, 'from_date': from_date, 'to_date':to_date, 'aggregate_by': aggregate_by}
        elif politician_id is not None:
            url = '{}twitter/tweets_by/politicians/{}/'.format(self.base, politician_id)
            parameters={'text_contains': text_contains, 'from_date': from_date, 'to_date':to_date, 'aggregate_by': aggregate_by}

        return self.session.get(url=url, params=parameters).json()

    def reply_to(self, twitter_user_id=None, politician_id=None, text_contains=None, from_date=None, to_date=None, aggregate_by='month'):
        """Returns query twitter replies made by politicians, or by a politician using twitter id or using politician id

        Input parameters:
                        twitter_user_id (str): twitter user id
                        OR
                        politician_id (str): A unique value identifying this politician.
                        optional:
                        text_contains (str): filter tweets by the content of the message
                        from_date (string($date)): filter by tweets posted after this date (format: YYYY-MM-DD)
                        to_date (string($date)): filter by tweets posted before this date (format: YYYY-MM-DD)
                        aggregate_by (str): criteria that will be used to aggregate (month by default)

        Returns:
            dict, result of the api query as documented in twitter tweets_by/reply_to content in http://10.6.13.139:8000/politicians/api/swagger/
        """
        if twitter_user_id is None and politician_id is None:
            url = '{}twitter/reply_to/politicians/'.format(self.base)
            parameters={'text_contains': text_contains, 'from_date': from_date, 'to_date':to_date, 'aggregate_by': aggregate_by}
        elif twitter_user_id is not None:
            url = '{}twitter/reply_to/politicians/user_id/{}/'.format(self.base, twitter_user_id)
            parameters={'text_contains': text_contains, 'from_date': from_date, 'to_date':to_date, 'aggregate_by': aggregate_by}
        elif politician_id is not None:
            url = '{}twitter/reply_to/politicians/{}/'.format(self.base, politician_id)
            parameters={'text_contains': text_contains, 'from_date': from_date, 'to_date':to_date, 'aggregate_by': aggregate_by}

        return self.session.get(url=url, params=parameters).json()

    def posts_by(self, facebook_user_id=None, politician_id=None, text_contains=None, from_date=None, to_date=None, aggregate_by='month'):
        """Returns query posts from facebook made by politicians, or by a politician using facebook id or using politician id

        Input parameters:
                        facebook_user_id (str): facebook user id
                        OR
                        politician_id (str): A unique value identifying this politician.
                        optional:
                        text_contains (str): filter tweets by the content of the message
                        from_date (string($date)): filter by tweets posted after this date (format: YYYY-MM-DD)
                        to_date (string($date)): filter by tweets posted before this date (format: YYYY-MM-DD)
                        aggregate_by (str): criteria that will be used to aggregate (month by default)

        Returns:
            dict, result of the api query as documented in facebook posts_by/comments_by content in http://10.6.13.139:8000/politicians/api/swagger/
        """
        if facebook_user_id is None and politician_id is None:
            url = '{}facebook/posts_by/politicians/'.format(self.base)
            parameters={'text_contains': text_contains, 'from_date': from_date, 'to_date':to_date, 'aggregate_by': aggregate_by}
        elif facebook_user_id is not None:
            url = '{}facebook/posts_by/politicians/user_id/{}/'.format(self.base, facebook_user_id)
            parameters={'text_contains': text_contains, 'from_date': from_date, 'to_date':to_date, 'aggregate_by': aggregate_by}
        elif politician_id is not None:
            url = '{}facebook/posts_by/politicians/{}/'.format(self.base, politician_id)
            parameters={'text_contains': text_contains, 'from_date': from_date, 'to_date':to_date, 'aggregate_by': aggregate_by}

        return self.session.get(url=url, params=parameters).json()

    def comments_by(self, facebook_user_id=None, politician_id=None, text_contains=None, from_date=None, to_date=None, aggregate_by='month'):
        """Returns query comments from facebook made by politicians, or by a politician using facebook id or using politician id

        Input parameters:
                        facebook_user_id (str): facebook user id
                        OR
                        politician_id (str): A unique value identifying this politician.
                        optional:
                        text_contains (str): filter tweets by the content of the message
                        from_date (string($date)): filter by tweets posted after this date (format: YYYY-MM-DD)
                        to_date (string($date)): filter by tweets posted before this date (format: YYYY-MM-DD)
                        aggregate_by (str): criteria that will be used to aggregate (month by default)

        Returns:
            dict, result of the api query as documented in facebook posts_by/comments_by content in http://10.6.13.139:8000/politicians/api/swagger/
        """
        if facebook_user_id is None and politician_id is None:
            url = '{}facebook/comments_by/politicians/'.format(self.base)
            parameters={'text_contains': text_contains, 'from_date': from_date, 'to_date':to_date, 'aggregate_by': aggregate_by}
        elif facebook_user_id is not None:
            url = '{}facebook/comments_by/politicians/user_id/{}/'.format(self.base, facebook_user_id)
            parameters={'text_contains': text_contains, 'from_date': from_date, 'to_date':to_date, 'aggregate_by': aggregate_by}
        elif politician_id is not None:
            url = '{}facebook/comments_by/politicians/{}/'.format(self.base, politician_id)
            parameters={'text_contains': text_contains, 'from_date': from_date, 'to_date':to_date, 'aggregate_by': aggregate_by}

        return self.session.get(url=url, params=parameters).json()

    def wikipedia(self, wikipedia_page_id=None, politician_id=None, text_contains=None, from_date=None, to_date=None, aggregate_by='month'):
        """Returns change objects (chobs) that refer to politicians Wikipedia pages, or by a politician using wikipedia page id or using politician id

        Input parameters:
                        wikipedia_page_id (str): wikipedia page id
                        OR
                        politician_id (str): A unique value identifying this politician.
                        optional:
                        text_contains (str): filter tweets by the content of the message
                        from_date (string($date)): filter by tweets posted after this date (format: YYYY-MM-DD)
                        to_date (string($date)): filter by tweets posted before this date (format: YYYY-MM-DD)
                        aggregate_by (str): criteria that will be used to aggregate (month by default)

        Returns:
            dict, result of the api query as documented in wikipedia content in http://10.6.13.139:8000/politicians/api/swagger/
        """
        if wikipedia_page_id is None and politician_id is None:
            url = '{}wikipedia/chobs/politicians/'.format(self.base)
            parameters={'text_contains': text_contains, 'from_date': from_date, 'to_date':to_date, 'aggregate_by': aggregate_by}
        elif wikipedia_page_id is not None:
            url = '{}wikipedia/chobs/politicians/page_id/{}/'.format(self.base, wikipedia_page_id)
            parameters={'text_contains': text_contains, 'from_date': from_date, 'to_date':to_date, 'aggregate_by': aggregate_by}
        elif politician_id is not None:
            url = '{}wikipedia/chobs/politicians/{}/'.format(self.base, politician_id)
            parameters={'text_contains': text_contains, 'from_date': from_date, 'to_date':to_date, 'aggregate_by': aggregate_by}

        return self.session.get(url=url, params=parameters).json()

    def request(self, url: str, tries=2) -> dict:
        """Do the request

        Args:
            url (str): The request url
            tries (int, optional): the number of attemts to be done in the server

        Returns:
            dict: The results of the request

        Raises:
            exc: If a connection has failed
        """

        for attempt in range(0, self.attempts + 1):
            try:
                response = self.session.get(url)
                response.raise_for_status()
                return response.json()
            except Exception as exc:
                if attempt == self.attempts:
                    raise exc
                else:
                    print(f"Connection failed (attempt {attempt + 1} of {self.attempts}) ")
