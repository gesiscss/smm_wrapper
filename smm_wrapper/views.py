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

    def __init__(self, api):
        """Constructor of the DataView
        Args:
            api (TYPE): the SMMAPI
        """
        self.api = api

    def get_politicians(self) -> pd.DataFrame:
        """Get entities of all politicians and their respective facebook, twitter and wikipedia ids.

        Returns:
            dataframe: result of the api query as documented in Entity list in 
                http://10.6.13.139:8000/politicians/api/politicians/
            politician_id:int,  unique identifier for a politician
            name:str, name of a politician
            firstname:str, firstname of a politician
            fb_ids:list(int), ids of all facebook accounts for a politician
            tw_ids:list(int), ids of all twitter accounts for a politician
            wp_ids:list(int), ids of all wikipedia pages for a politician
        """
        response = self.api.get_politicians()

        return pd.DataFrame(response, columns=[
            'politician_id', 'name', 'firstname', 'affiliation', 'fb_ids', 'tw_ids', 'wp_ids'
        ]).set_index('politician_id')

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
            DataFrame, result of the api query as documented in twitter tweets_by/reply_to content in http://10.6.13.139:8000/politicians/api/swagger/
        """

        response = self.api.tweets_by(
            twitter_user_id, politician_id, text_contains, from_date, to_date, aggregate_by)

        if twitter_user_id is not None:
            response['twitter_user_id'] = twitter_user_id
        if politician_id is not None:
            response['politician_id'] = politician_id
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


    def replies_to(self, twitter_user_id=None, politician_id=None, text_contains=None, from_date=None, to_date=None, aggregate_by='month'):
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
            DataFrame, result of the api query as documented in twitter tweets_by/reply_to content in http://10.6.13.139:8000/politicians/api/swagger/
        """

        response = self.api.replies_to(
            twitter_user_id, politician_id, text_contains, from_date, to_date, aggregate_by)

        if twitter_user_id is not None:
            response['twitter_user_id'] = twitter_user_id
        if politician_id is not None:
            response['politician_id'] = politician_id
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
