"""Summary
"""
import pandas as pd
import itertools
from typing import Union

from .api import SMMAPI
from . import __version__


class DataView:

    """Qurey methods for correspondence of the SMMAPI methods
    Attributes:
        api (TYPE): Description
    """

    def __init__(self, api, id_column):
        """Constructor of the DataView
        Args:
            api (TYPE): the SMMAPI
        """
        self.api = api
        self.id_column = id_column

    def get_politicians(self) -> pd.DataFrame:
        """Get entities of all politicians and their respective facebook, twitter and wikipedia ids.

        Returns:
            dataframe: result of the api query as documented in Entity list in 
                http://mediamonitoring.gesis.org/politicians/api/politicians/
            politician_id:int,  unique identifier for a politician
            name:str, name of a politician
            firstname:str, firstname of a politician
            affiliation:str, party to which a politician is affiliated
            fb_ids:list(int), ids of all facebook accounts for a politician
            tw_ids:list(int), ids of all twitter accounts for a politician
            wp_ids:list(int), ids of all wikipedia pages for a politician
            wp_titles:list(string), wikipedia titles associated to the politician
        """
        response = self.api.get_all()

        return pd.DataFrame(response, columns=[
            'politician_id', 'name', 'firstname', 'affiliation', 'fb_ids', 'tw_ids', 'wp_ids', 'wp_titles'
        ]).set_index('politician_id')

    def get_politician(self, _id) -> pd.DataFrame:
        """Get entities of a politicians and their respective facebook, twitter and wikipedia ids.
        Input parameters:
                        _id (str): A unique value identifying this politician or an organization.

        Returns:
            dataframe: result of the api query as documented in Entity list in 
                http://mediamonitoring.gesis.org/politicians/api/politicians/
            politician_id:int,  unique identifier for a politician
            name:str, name ofs a politician
            firstname:str, firstname of a politician
            affiliation:str, party to which a politician is affiliated
            fb_ids:list(int), ids of all facebook accounts for a politician
            tw_ids:list(int), ids of all twitter accounts for a politician
            wp_ids:list(int), ids of all wikipedia pages for a politician
            wp_titles:list(string), wikipedia titles associated to the politician
        """
        response = self.api.get(_id)

        return pd.Series(response)

    def get_organizations(self) -> pd.DataFrame:
        """Get entities of all organizations and their respective facebook, twitter and wikipedia ids.

        Returns:
            dataframe: result of the api query as documented in Entity list in 
                http://mediamonitoring.gesis.org/api/organizations/all
            organization_id:int,  unique identifier for an organization
            name:str, name of an organization
            category:str, type of an organization (media or a party)
            subcategory:str, subcategory of an organization (name of a party or type of media)
            fb_ids:list(int), ids of all facebook accounts for an organization
            tw_ids:list(int), ids of all twitter accounts for an organization
            wp_ids:list(int), ids of all wikipedia pages for an organization
            wp_titles:list(string), wikipedia titles associated to the organization
        """
        response = self.api.get_all()

        return pd.DataFrame(response, columns=[
            'organization_id', 'name', 'category', 'subcategory', 'fb_ids', 'tw_ids', 'wp_ids', 'wp_titles'
        ]).set_index('organization_id')


    def get_organization(self, _id) -> pd.DataFrame:
        """Get entities of an organization and their respective facebook, twitter and wikipedia ids.
        Input parameters:
                        _id (str): A unique value identifying this politician or an organization.

        Returns:
            dataframe: result of the api query as documented in Entity list in 
                http://mediamonitoring.gesis.org/politicians/api/politicians/
            politician_id:int,  unique identifier for a politician
            name:str, name ofs a politician
            firstname:str, firstname of a politician
            affiliation:str, party to which a politician is affiliated
            fb_ids:list(int), ids of all facebook accounts for a politician
            tw_ids:list(int), ids of all twitter accounts for a politician
            wp_ids:list(int), ids of all wikipedia pages for a politician
            wp_titles:list(string), wikipedia titles associated to the politician
        """
        response = self.api.get(_id)

        return pd.Series(response)


    def get_all(self) -> pd.DataFrame:
        """Get all entities and their respective facebook, twitter and wikipedia ids.

        Returns:
            dataframe: result of the api query as documented in Entity list in 
                http://mediamonitoring.gesis.org/api/organizations/all
            organization_id:int,  unique identifier for an organization
            name:str, name of an organization
            category:str, type of an organization (media or a party)
            subcategory:str, subcategory of an organization (name of a party or type of media)
            fb_ids:list(int), ids of all facebook accounts for an organization
            tw_ids:list(int), ids of all twitter accounts for an organization
            wp_ids:list(int), ids of all wikipedia pages for an organization
            wp_titles:list(string), wikipedia titles associated to the organization
        """
        response = self.api.get_all()

        return pd.DataFrame(response).set_index(self.id_column)


    def get_one(self, _id) -> pd.DataFrame:
        """Get an entity and their respective facebook, twitter and wikipedia ids.
        Input parameters:
                        _id (str): A unique value identifying this politician or an organization.

        Returns:
            dataframe: result of the api query as documented in Entity list in 
                http://mediamonitoring.gesis.org/politicians/api/politicians/
            politician_id:int,  unique identifier for a politician
            name:str, name ofs a politician
            firstname:str, firstname of a politician
            affiliation:str, party to which a politician is affiliated
            fb_ids:list(int), ids of all facebook accounts for a politician
            tw_ids:list(int), ids of all twitter accounts for a politician
            wp_ids:list(int), ids of all wikipedia pages for a politician
            wp_titles:list(string), wikipedia titles associated to the politician
        """
        response = self.api.get_one(_id)

        return pd.Series(response)

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
            DataFrame, result of the api query as documented in twitter tweets_by/reply_to content in http://mediamonitoring.gesis.org/api/politicians/swagger/
        """

        response = self.api.tweets_by(
            twitter_user_id, _id, text_contains, from_date, to_date, aggregate_by)

        if twitter_user_id is not None:
            response['twitter_user_id'] = twitter_user_id
        if _id is not None:
            response['_id'] = _id
        if text_contains is not None:
            response['text_contains'] = text_contains
        if from_date is not None:
            response['from_date'] = from_date
        if to_date is not None:
            response['to_date'] = to_date

        response.pop('response_type')
        response.pop('aggregated_by')
        response['date'] = response.pop('labels')
        response['tweets'] = response.pop('values')

        df = pd.DataFrame(response)

        df['date'] = pd.to_datetime(df['date'])

        return df


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
            DataFrame, result of the api query as documented in twitter tweets_by/reply_to content in http://mediamonitoring.gesis.org/api/politicians/swagger/
        """

        response = self.api.replies_to(
            twitter_user_id, _id, text_contains, from_date, to_date, aggregate_by)

        if twitter_user_id is not None:
            response['twitter_user_id'] = twitter_user_id
        if _id is not None:
            response['_id'] = _id
        if text_contains is not None:
            response['text_contains'] = text_contains
        if from_date is not None:
            response['from_date'] = from_date
        if to_date is not None:
            response['to_date'] = to_date

        response.pop('response_type')
        response.pop('aggregated_by')
        response['date'] = response.pop('labels')
        response['replies'] = response.pop('values')

        df = pd.DataFrame(response)

        df['date'] = pd.to_datetime(df['date'])

        return df

    def posts_by(self, facebook_user_id=None, _id=None, text_contains=None, from_date=None, to_date=None, aggregate_by='month'):
        """Returns query facebook posts made by politicians, or by a politician using facebook id or using politician id

        Input parameters:
                        facebook_user_id (str): facebook user id
                        OR
                        _id (str): A unique value identifying this politician or an organization.
                        optional:
                        text_contains (str): filter facebook posts by the content of the message
                        from_date (string($date)): filter by facebook posts posted after this date (format: YYYY-MM-DD)
                        to_date (string($date)): filter by facebook posts posted before this date (format: YYYY-MM-DD)
                        aggregate_by (str): criteria that will be used to aggregate (month by default)

        Returns:
            DataFrame, result of the api query as documented in facebook posts_by content in http://mediamonitoring.gesis.org/api/politicians/swagger/
        """

        response = self.api.posts_by(
            facebook_user_id, _id, text_contains, from_date, to_date, aggregate_by)

        if facebook_user_id is not None:
            response['facebook_user_id'] = facebook_user_id
        if _id is not None:
            response['_id'] = _id
        if text_contains is not None:
            response['text_contains'] = text_contains
        if from_date is not None:
            response['from_date'] = from_date
        if to_date is not None:
            response['to_date'] = to_date

        response.pop('response_type')
        response.pop('aggregated_by')
        response['date'] = response.pop('labels')
        response['posts'] = response.pop('values')

        df = pd.DataFrame(response)

        df['date'] = pd.to_datetime(df['date'])

        return df

    def comments_by(self, facebook_user_id=None, _id=None, text_contains=None, from_date=None, to_date=None, aggregate_by='month'):
        """Returns query facebook comments made by politicians, or by a politician using facebook id or using politician id

        Input parameters:
                        facebook_user_id (str): facebook user id
                        OR
                        _id (str): A unique value identifying this politician or an organization.
                        optional:
                        text_contains (str): filter facebook comments by the content of the message
                        from_date (string($date)): filter by facebook comments posted after this date (format: YYYY-MM-DD)
                        to_date (string($date)): filter by facebook comments posted before this date (format: YYYY-MM-DD)
                        aggregate_by (str): criteria that will be used to aggregate (month by default)

        Returns:
            DataFrame, result of the api query as documented in facebook comments_by content in http://mediamonitoring.gesis.org/api/politicians/swagger/
        """

        response = self.api.comments_by(
            facebook_user_id, _id, text_contains, from_date, to_date, aggregate_by)

        if facebook_user_id is not None:
            response['facebook_user_id'] = facebook_user_id
        if _id is not None:
            response['_id'] = _id
        if text_contains is not None:
            response['text_contains'] = text_contains
        if from_date is not None:
            response['from_date'] = from_date
        if to_date is not None:
            response['to_date'] = to_date

        response.pop('response_type')
        response.pop('aggregated_by')
        response['date'] = response.pop('labels')
        response['comments'] = response.pop('values')

        df = pd.DataFrame(response)

        df['date'] = pd.to_datetime(df['date'])

        return df

    def wikipedia(self, wikipedia_page_id=None, _id=None, text_contains=None, from_date=None, to_date=None, aggregate_by='month'):
        """Returns query wikipedia change objects (chobs) made by politicians, or by a politician using wikipedia id or using politician id

        Input parameters:
                        wikipedia_page_id (str): wikipedia page id
                        OR
                        _id (str): A unique value identifying this politician or an organization.
                        optional:
                        text_contains (str): filter chobs by the content of the message
                        from_date (string($date)): filter by chobs posted after this date (format: YYYY-MM-DD)
                        to_date (string($date)): filter by chobs posted before this date (format: YYYY-MM-DD)
                        aggregate_by (str): criteria that will be used to aggregate (month by default)

        Returns:
            DataFrame, result of the api query as documented in wikipedia content in http://mediamonitoring.gesis.org/api/politicians/swagger/
        """

        response = self.api.wikipedia(
           wikipedia_page_id, _id, text_contains, from_date, to_date, aggregate_by)

        if wikipedia_page_id is not None:
            response['wikipedia_page_id'] = wikipedia_page_id
        if _id is not None:
            response['_id'] = _id
        if text_contains is not None:
            response['text_contains'] = text_contains
        if from_date is not None:
            response['from_date'] = from_date
        if to_date is not None:
            response['to_date'] = to_date
        if aggregate_by is None:
            response.pop('response_type')
            df = pd.DataFrame(response)
            df = df['chobs'].apply(pd.Series)[['right_token','left_token', 'ins_tokens', 'del_tokens', 
            'right_token_str', 'left_token_str', 'ins_tokens_str', 'del_tokens_str']]
            #df = df[['right_token','left_token']]

        else:
            response.pop('response_type')
            response.pop('aggregated_by')
            response['date'] = response.pop('labels')
            response['chobs'] = response.pop('values')
            df = pd.DataFrame(response)
            df['date'] = pd.to_datetime(df['date'])

        return df

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
            dataframe, result of the api query as documented in twitter (general public) content in http://mediamonitoring.gesis.org/api/politicians/swagger/
        """

        response = self.api.general_tweets(
           twitter_user_id, text_contains, from_date, to_date, aggregate_by)

        if twitter_user_id is not None:
            response['twitter_user_id'] = twitter_user_id
        if text_contains is not None:
            response['text_contains'] = text_contains
        if from_date is not None:
            response['from_date'] = from_date
        if to_date is not None:
            response['to_date'] = to_date

        response.pop('response_type')
        response.pop('aggregated_by')
        response['date'] = response.pop('labels')
        response['tweets'] = response.pop('values')

        df = pd.DataFrame(response)

        df['date'] = pd.to_datetime(df['date'])

        return df
