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

<<<<<<< HEAD
        df = pd.DataFrame(response, columns=[
            'politician_id','name', 'firstname', 'fb_ids', 'tw_ids', 'wp_ids'
=======
        df = pd.DataFrame(data=rows, columns=[
            'article_title', 'page_id', 'o_rev_id', 'o_editor', 'rev_id',
            'rev_editor', 'rev_time', 'token', 'token_id', 'in', 'out'
        ])

        return df.drop(columns=[name for name, include in zip(
            ['o_rev_id', 'o_editor', 'rev_editor', 'token_id', 'in', 'out'],
            [o_rev_id, editor, editor, token_id, _in, out]) if not include
        ])
        

    def range_rev_content_by_article_title(self,
                                           article: Union[int, str],
                                           start_rev_id: int,
                                           end_rev_id: int,
                                           o_rev_id: bool=True,
                                           editor: bool=True,
                                           token_id: bool=True,
                                           out: bool=False,
                                           _in: bool=False) -> pd.DataFrame:
        """Get the content of a range of revisions of an article, by given article title, start revison id and end revison id.

        Args:
            article (Union[int, str]): page id (int) or title (str) of the page.
            start_rev_id (int): Start revision ID
            end_rev_id (int): End revision ID
            o_rev_id (bool, optional): Origin revision ID per token
            editor (bool, optional): Editor ID/Name per token
            token_id (bool, optional): Token ID per token
            out (bool, optional): Outbound revision IDs per token
            _in (bool, optional): Outbound revision IDs per token

        Returns:
            pd.DataFrame: Return a Pandas DataFrame of the api query as documented in 1 - Content per revision  for GET /rev_content/{article_title}/{start_rev_id}/{end_rev_id}/ in
                https://api.wikiwho.net/en/api/v1.0.0-beta/
        """

        response = self.api.range_rev_content_by_article_title(
            article, start_rev_id, end_rev_id, o_rev_id, editor, token_id, out, _in)

        rows = ((response["article_title"],
                 response["page_id"],
                 token_dict["o_rev_id"] if o_rev_id else None,
                 token_dict["editor"] if editor else None,
                 rev_id,
                 rev_dict['editor'] if editor else None,
                 rev_dict['time'],
                 token_dict["str"],
                 token_dict["token_id"] if token_id else None,
                 _i,
                 _o
                 )

                for dummy_rev in response["revisions"]
                for rev_id, rev_dict in dummy_rev.items()
                for token_dict in rev_dict['tokens']
                for i, (_i, _o) in self.__get_iterator(token_dict, _in, out)
                )

        df = pd.DataFrame(data=rows, columns=[
            'article_title', 'page_id', 'o_rev_id', 'o_editor', 'rev_id',
            'rev_editor', 'rev_time', 'token', 'token_id', 'in', 'out'
        ])

        return df.drop(columns=[name for name, include in zip(
            ['o_rev_id', 'o_editor', 'rev_editor', 'token_id', 'in', 'out'],
            [o_rev_id, editor, editor, token_id, _in, out]) if not include
        ])

    def rev_ids_of_article(self,
                           article: Union[int, str],
                           editor: bool=True,
                           timestamp: bool=True) -> pd.DataFrame:
        """Get revision IDs of an article by given article title or page id.

        Args:
            article (Union[int, str]): page id (int) or title (str) of the page.
            editor (bool, optional): Editor ID/Name per token
            timestamp (bool, optional): timestamp of each revision

        Returns:
            pd.DataFrame: Return a Pandas DataFrame of the api query as documented in 1 - Content per revision for GET /rev_ids/{article_title}/ and GET /rev_ids/page_id/{page_id}/ in
                https://api.wikiwho.net/en/api/v1.0.0-beta/
        """
        response = self.api.rev_ids_of_article(article, editor, timestamp)

        rows = ((response["article_title"],
                 response["page_id"],
                 rev['timestamp'] if timestamp else None,
                 rev['id'],
                 rev['editor'] if editor else None
                 )

                for rev in response["revisions"]
                )

        df = pd.DataFrame(data=rows, columns=[
            'article_title', 'page_id', 'rev_time', 'rev_id', 'o_editor'
        ])

        return df.drop(columns=[name for name, include in zip(
            ['rev_time', 'o_editor'],
            [timestamp, editor]) if not include
        ])

    def actions(self,
                page_id: int=None,
                editor_id: int=None,
                start: str=None,
                end: str=None) -> pd.DataFrame:
        """Get monthly editons for given editor id.

        Args:
            page_id (int, optional): page id (int).   
            editor_id (int, optional): editor id (int).
            start (str, optional): Origin revision ID per token
            end (str, optional): Editor ID/Name per token

        Returns:
            pd.DataFrame: Return a Pandas DataFrame of the api query as documented in /editor/{editor_id}/ in
                https://www.wikiwho.net/en/edit_persistence/v1.0.0-beta/
        """
        response = self.api.edit_persistence(page_id, editor_id, start, end)

        rows = ((element['year_month'],
                 element["page_id"],
                 element["editor_id"],
                 element["adds"],
                 element["adds_surv_48h"],
                 element["adds_persistent"],
                 element["adds_stopword_count"],
                 element["dels"],
                 element["dels_surv_48h"],
                 element["dels_persistent"],
                 element["dels_stopword_count"],
                 element["reins"],
                 element["reins_surv_48h"],
                 element["reins_persistent"],
                 element["reins_stopword_count"],
                 )

                for element in response["editions"]
                )

        df = pd.DataFrame(data=rows, columns=[
            'year_month', 'page_id', 'editor_id',
            'adds', 'adds_surv_48h', 'adds_persistent', 'adds_stopword_count',
            'dels', 'dels_surv_48h', 'dels_persistent', 'dels_stopword_count',
            'reins', 'reins_surv_48h', 'reins_persistent', 'reins_stopword_count'
>>>>>>> d9c788aaed63b95a4a77fbd127ef9a58460fc33b
        ])
        df.set_index('politician_id', inplace=True)

        return df

<<<<<<< HEAD
<<<<<<< HEAD
    
=======
=======
>>>>>>> d9c788aaed63b95a4a77fbd127ef9a58460fc33b
    def actions_as_table(self,
                         page_id: int=None,
                         editor_id: int=None,
                         start: str=None,
                         end: str=None) -> pd.DataFrame:
        """Get monthly editons in tabular format for given page id or editor id or both.

        Args:
            page_id (int, optional): page id (int).   
            editor_id (int, optional): editor id (int).
            start (str, optional): Origin revision ID per token
            end (str, optional): Editor ID/Name per token

        Returns:
            pd.DataFrame: Return a Pandas DataFrame of the api query as documented in /editor/{editor_id}/ in
                https://www.wikiwho.net/en/edit_persistence/v1.0.0-beta/
        """
        response = self.api.edit_persistence_as_table(
            page_id, editor_id, start, end)

        df = pd.DataFrame(data=response['editions_data'], columns=response[
                          'editions_columns'])

        return df

    def edit_persistence(self,
                         page_id: int=None,
                         editor_id: int=None,
                         start: str=None,
                         end: str=None) -> pd.DataFrame:
        """Get monthly editons for given editor id.

        Args:
            page_id (int, optional): page id (int).   
            editor_id (int, optional): editor id (int).
            start (str, optional): Origin revision ID per token
            end (str, optional): Editor ID/Name per token

        Returns:
            pd.DataFrame: Return a Pandas DataFrame of the api query as documented in /editor/{editor_id}/ in
                https://www.wikiwho.net/en/edit_persistence/v1.0.0-beta/
        """
        response = self.api.edit_persistence_as_table(
            page_id, editor_id, start, end)

        df = pd.DataFrame(data=response['editions_data'], columns=response[
                          'editions_columns'])

        return df
>>>>>>> d9c788aaed63b95a4a77fbd127ef9a58460fc33b
