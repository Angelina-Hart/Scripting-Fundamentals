
import requests
import json


class AccessApi:
    """
    Class AccessApi is used to abstract lower level access to course required API

    Attributes
    ----------
    url : str
        A valid website used to hold the courses json filesS

    Methods
    -------
    url_active()
        returns True if the url is currently responding without errors, and False if not.

    get_end_point(endpoint)
        returns the json output of the GET request

    """
    def __init__(self, url):
        """
        Parameters
        ----------
        url: str
           a valid website forexample: http://google.com
        """
        

    @property
    def url(self) -> str:
        

    @url.setter
    def url(self, url: str):
        

    def url_active(self) -> bool:
       

    def get_end_point(self, end_point:str) -> dict:
        """
            Parameters
            ----------
            end_point: str
               a valid endpoint on a website  "api/sites/master.json"
        """
      
    def get_status_code(self, end_point:str) -> int:
        """
            Parameters
            ----------
            end_point: str
               a valid endpoint on a website  "api/sites/master.json"
        """


    def get_elapsed_time(self, end_point:str) -> float:
        """
            Parameters
            ----------
            end_point: str
               a valid endpoint on a website  "api/sites/master.json"
        """



