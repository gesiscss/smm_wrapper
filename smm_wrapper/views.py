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

    def politicians_df(self) -> pd.DataFrame:
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

        # rows = ((response["article_title"],
        #          response["page_id"],
        #          token_dict["o_rev_id"] if o_rev_id else None,
        #          token_dict["editor"] if editor else None,
        #          token_dict["str"],
        #          token_dict["token_id"] if token_id else None,
        #          _i,
        #          _o)

        #         for token_dict in response["all_tokens"]
        #         for i, (_i, _o) in self.__get_iterator(token_dict, _in, out)
        #         )

        df = pd.DataFrame(response, columns=[
            'politician_id','name', 'firstname', 'fb_ids', 'tw_ids', 'wp_ids'
        ])
        df.set_index('politician_id', inplace=True)

        return df

    