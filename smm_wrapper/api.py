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
                 domain: str="mediamonitoring.gesis.org",
                 unit: str="",
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
        self.unit = unit

        self.session = requests.Session()
        if username and password:
            self.session.auth = (username, password)

        if api_key:
            self.session.params = {}
            self.session.params['api_key'] = api_key

        self.base = "{}://{}/api/{}/".format(protocol, domain, self.unit)
        self.attempts = attempts

    def get_all(self):
        """Returns a list of all entities of politicians/organizations.

        No input parameters

        Returns:
            list: result of the api query as documented in Entity list in 
                http://mediamonitoring.gesis.org/api/politicians/swagger/
        """

        smm_api_url = '{}all/'.format(self.base)

        # return the dictionary
        return self.request(smm_api_url)

    def get_one(self, _id):
        """Returns the information of one politician/organization.
        
        Input parameters:
            _id (int): the id of the entity politician or organiation
        
        Returns:
            list: result of the api query as documented in Entity list in 
                http://mediamonitoring.gesis.org/api/politicians/swagger/
        
        
        """

        smm_api_url = '{}all/{}'.format(self.base, _id)

        # return the dictionary
        return self.request(smm_api_url)

    def all_search(self, names_contain = None, _id = None):
        """Returns either a list with politicians/organizations based on the text search or a given politician 
        or organization by id 

        Input parameters:
                        names_contain (str): Search text in first name, last name, Twitter or Facebook screen names, or Wikipedia titles
                        OR
                        _id (int): A unique value identifying this politician or organization

        Returns:
            names_contain: returns a list of all entities searched by names, firstnames and usernames
            _id: returns a given politician or organization by id
        """
        if names_contain is not None:
            url = '{}all/search/'.format(self.base)
            parameters={'names_contain': names_contain}
        elif _id is not None:
            url = '{}all/{}/'.format(self.base, _id)
            parameters = {}

        return self.session.get(url=url, params=parameters).json()

    def tweets_by(self, twitter_user_id=None, _id=None, text_contains=None, from_date=None, to_date=None, aggregate_by='month'):
        """Returns query tweets made by politicians, or by a politician using twitter id or using politician id

        Input parameters:
                        twitter_user_id (str): twitter user id
                        OR
                        _id (str): A unique value identifying this politician or an organization.
                        optional:
                        text_contains (str): filter tweets by the content of the message
                        from_date (string($date)): filter by tweets posted after this date (format: YYYY-MM-DD)
                        to_date (string($date)): filter by tweets posted before this date (format: YYYY-MM-DD)
                        aggregate_by (str): criteria that will be used to aggregate (month by default)

        Returns:
            dict, result of the api query as documented in twitter tweets_by/replies_to content in http://mediamonitoring.gesis.org/api/politicians/swagger/swagger/
        """
        if twitter_user_id is None and _id is None:
            url = '{}twitter/tweets_by/{}/'.format(self.base, self.unit)
            parameters={'text_contains': text_contains, 'from_date': from_date, 'to_date':to_date, 'aggregate_by': aggregate_by}
        elif twitter_user_id is not None:
            url = '{}twitter/tweets_by/{}/user_id/{}/'.format(self.base, self.unit, twitter_user_id)
            parameters={'text_contains': text_contains, 'from_date': from_date, 'to_date':to_date, 'aggregate_by': aggregate_by}
        elif _id is not None:
            url = '{}twitter/tweets_by/{}/{}/'.format(self.base, self.unit, _id)
            parameters={'text_contains': text_contains, 'from_date': from_date, 'to_date':to_date, 'aggregate_by': aggregate_by}

        return self.session.get(url=url, params=parameters).json()

    def replies_to(self, twitter_user_id=None, _id=None, text_contains=None, from_date=None, to_date=None, aggregate_by='month'):
        """Returns query twitter replies made by politicians, or by a politician using twitter id or using politician id

        Input parameters:
                        twitter_user_id (str): twitter user id
                        OR
                        _id (str): A unique value identifying this politician or an organization.
                        optional:
                        text_contains (str): filter tweets by the content of the message
                        from_date (string($date)): filter by tweets posted after this date (format: YYYY-MM-DD)
                        to_date (string($date)): filter by tweets posted before this date (format: YYYY-MM-DD)
                        aggregate_by (str): criteria that will be used to aggregate (month by default)

        Returns:
            dict, result of the api query as documented in twitter tweets_by/replies_to content in http://mediamonitoring.gesis.org/api/politicians/swagger/swagger/
        """
        if twitter_user_id is None and _id is None:
            url = '{}twitter/replies_to/{}/'.format(self.base, self.unit)
            parameters={'text_contains': text_contains, 'from_date': from_date, 'to_date':to_date, 'aggregate_by': aggregate_by}
        elif twitter_user_id is not None:
            url = '{}twitter/replies_to/{}/user_id/{}/'.format(self.base, self.unit, twitter_user_id)
            parameters={'text_contains': text_contains, 'from_date': from_date, 'to_date':to_date, 'aggregate_by': aggregate_by}
        elif _id is not None:
            url = '{}twitter/replies_to/{}/{}/'.format(self.base, self.unit, _id)
            parameters={'text_contains': text_contains, 'from_date': from_date, 'to_date':to_date, 'aggregate_by': aggregate_by}

        return self.session.get(url=url, params=parameters).json()

    def posts_by(self, facebook_user_id=None, _id=None, text_contains=None, from_date=None, to_date=None, aggregate_by='month'):
        """Returns query posts from facebook made by politicians, or by a politician using facebook id or using politician id

        Input parameters:
                        facebook_user_id (str): facebook user id
                        OR
                        _id (str): A unique value identifying this politician or organization.
                        optional:
                        text_contains (str): filter tweets by the content of the message
                        from_date (string($date)): filter by tweets posted after this date (format: YYYY-MM-DD)
                        to_date (string($date)): filter by tweets posted before this date (format: YYYY-MM-DD)
                        aggregate_by (str): criteria that will be used to aggregate (month by default)

        Returns:
            dict, result of the api query as documented in facebook posts_by/comments_by content in http://mediamonitoring.gesis.org/api/politicians/swagger/swagger/
        """
        if facebook_user_id is None and _id is None:
            url = '{}facebook/posts_by/{}/'.format(self.base, self.unit)
            parameters={'text_contains': text_contains, 'from_date': from_date, 'to_date':to_date, 'aggregate_by': aggregate_by}
        elif facebook_user_id is not None:
            url = '{}facebook/posts_by/{}/user_id/{}/'.format(self.base, self.unit, facebook_user_id)
            parameters={'text_contains': text_contains, 'from_date': from_date, 'to_date':to_date, 'aggregate_by': aggregate_by}
        elif _id is not None:
            url = '{}facebook/posts_by/{}/{}/'.format(self.base, self.unit, _id)
            parameters={'text_contains': text_contains, 'from_date': from_date, 'to_date':to_date, 'aggregate_by': aggregate_by}

        return self.session.get(url=url, params=parameters).json()

    def comments_by(self, facebook_user_id=None, _id=None, text_contains=None, from_date=None, to_date=None, aggregate_by='month'):
        """Returns query comments from facebook made by politicians, or by a politician using facebook id or using politician id

        Input parameters:
                        facebook_user_id (str): facebook user id
                        OR
                        _id (str): A unique value identifying this politician or an organization.
                        optional:
                        text_contains (str): filter tweets by the content of the message
                        from_date (string($date)): filter by tweets posted after this date (format: YYYY-MM-DD)
                        to_date (string($date)): filter by tweets posted before this date (format: YYYY-MM-DD)
                        aggregate_by (str): criteria that will be used to aggregate (month by default)

        Returns:
            dict, result of the api query as documented in facebook posts_by/comments_by content in http://mediamonitoring.gesis.org/api/politicians/swagger/swagger/
        """
        if facebook_user_id is None and _id is None:
            url = '{}facebook/comments_by/{}/'.format(self.base, self.unit)
            parameters={'text_contains': text_contains, 'from_date': from_date, 'to_date':to_date, 'aggregate_by': aggregate_by}
        elif facebook_user_id is not None:
            url = '{}facebook/comments_by/{}/user_id/{}/'.format(self.base, self.unit, facebook_user_id)
            parameters={'text_contains': text_contains, 'from_date': from_date, 'to_date':to_date, 'aggregate_by': aggregate_by}
        elif _id is not None:
            url = '{}facebook/comments_by/{}/{}/'.format(self.base, self.unit, _id)
            parameters={'text_contains': text_contains, 'from_date': from_date, 'to_date':to_date, 'aggregate_by': aggregate_by}

        return self.session.get(url=url, params=parameters).json()

    def wikipedia(self, wikipedia_page_id=None, _id=None, text_contains=None, from_date=None, to_date=None, aggregate_by='month'):
        """Returns change objects (chobs) that refer to politicians Wikipedia pages, or by a politician using wikipedia page id or using politician id

        Input parameters:
                        wikipedia_page_id (str): wikipedia page id
                        OR
                        _id (str): A unique value identifying this politician or an organization.
                        optional:
                        text_contains (str): filter chobs by the content of the message
                        from_date (string($date)): filter by chobs  after this date (format: YYYY-MM-DD)
                        to_date (string($date)): filter by chobs before this date (format: YYYY-MM-DD)
                        aggregate_by (str): criteria that will be used to aggregate (month by default)

        Returns:
            dict, result of the api query as documented in wikipedia content in http://mediamonitoring.gesis.org/api/politicians/swagger/swagger/
        """
        if wikipedia_page_id is None and _id is None:
            url = '{}wikipedia/chobs/{}/'.format(self.base, self.unit)
            parameters={'text_contains': text_contains, 'from_date': from_date, 'to_date':to_date, 'aggregate_by': aggregate_by}
        elif wikipedia_page_id is not None:
            url = '{}wikipedia/chobs/{}/page_id/{}/'.format(self.base, self.unit, wikipedia_page_id)
            parameters={'text_contains': text_contains, 'from_date': from_date, 'to_date':to_date, 'aggregate_by': aggregate_by}
        elif _id is not None:
            url = '{}wikipedia/chobs/{}/{}/'.format(self.base, self.unit, _id)
            parameters={'text_contains': text_contains, 'from_date': from_date, 'to_date':to_date, 'aggregate_by': aggregate_by}

        return self.session.get(url=url, params=parameters).json()

    def general_tweets(self, twitter_user_id=None, text_contains=None, from_date=None, to_date=None, aggregate_by='month'):
        """Returns query tweets made by the general population. This tweets were collected separatedly using keywords.

        Input parameters:
                        optional:
                        twitter_user_id (str): twitter user id 
                        text_contains (str): filter chobs by the content of the message
                        from_date (string($date)): filter by chobs  after this date (format: YYYY-MM-DD)
                        to_date (string($date)): filter by chobs before this date (format: YYYY-MM-DD)
                        aggregate_by (str): criteria that will be used to aggregate (month by default)

        Returns:
            dict, result of the api query as documented in twitter (general public) content in http://mediamonitoring.gesis.org/api/politicians/swagger/swagger/
        """
        if twitter_user_id is None:
            url = '{}twitter/general_population/'.format(self.base)
            parameters={'text_contains': text_contains, 'from_date': from_date, 'to_date':to_date, 'aggregate_by': aggregate_by}
        else:
            url = '{}twitter/general_population/user_id/{}/'.format(self.base, twitter_user_id)
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
