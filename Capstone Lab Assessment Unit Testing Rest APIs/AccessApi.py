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
        self.url = url

    @property
    def url(self) -> str:
        return self.url

    @url.setter
    def url(self, url: str):
        self.url = url

    def url_active(self) -> bool:
        response = requests.get(self.url)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            return False
        return True

    def get_end_point(self, end_point:str) -> dict:
        """
            Parameters
            ----------
            end_point: str
               a valid endpoint on a website  "api/sites/master.json"
        """
        new_url = self.url + end_point
        got_file = requests.get(new_url)
        file_text = json.loads(got_file.text)
        return file_text
      
    def get_status_code(self, end_point:str) -> int:
        """
            Parameters
            ----------
            end_point: str
               a valid endpoint on a website  "api/sites/master.json"
        """
        new_url = self.url + end_point
        got_file = requests.get(new_url)
        return got_file.status_code

    def get_elapsed_time(self, end_point:str) -> float:
        """
            Parameters
            ----------
            end_point: str
               a valid endpoint on a website  "api/sites/master.json"
        """
        
        new_url = self.url + end_point
        got_file = requests.get(new_url)
        return got_file.elapsed




