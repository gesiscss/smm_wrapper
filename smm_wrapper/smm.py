"""Summary
"""
from .api import SMMAPI

from .views import DataView


class SMM:

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
        """Constructor of the SMM

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


        self.api = SMMAPI(username,
                              password,
                              api_key,
                              lng,
                              protocol,
                              domain,
                              version,
                              attempts)

        self.dv = DataView(self.api)
