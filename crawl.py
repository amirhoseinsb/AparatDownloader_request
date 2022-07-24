import time

import requests

from abc import ABC, abstractmethod

from config import BASE_PATH


class Crawl(ABC):

    @abstractmethod
    def get_request(self, url, stream=False):
        pass


class LinkCrawl(Crawl):

    def __init__(self, url):
        self.url = url
        self.content = None

    def get_request(self, url, stream=False):
        """
        Send get request and store data in self.content
        :param url:
        :param stream:
        :return:
        """
        uid = url.split("/")[-1]
        path = BASE_PATH + uid
        try:
            response = requests.get(path)
        except requests.exceptions.ConnectionError:
            print("Connection Error.")
            print("The request will be automatically resubmitted.")
            print("Wait a few moments...")
            time.sleep(3)
            self.get_request(url)
        else:
            json_content = response.json()
            self.content = json_content.get("data")

    def get_all_links(self):
        """
        Parse self.content and store link in a list
        :return:
        """
        pass

    def get_all_qualities(self):
        """
        Parse self.content and store qualities in a list
        :return:
        """
        pass

    def match_quality_and_link(self):
        """
        Match links and qualities in a dict
        example: {"480": "sample-link", ...}
        :return:
        """
        pass

    def get_link(self, quality):
        """
        Return specific link
        :return:
        """
        pass
