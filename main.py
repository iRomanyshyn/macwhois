#!/usr/bin/python3

import requests

import config
import strings

# TODO localouifile in user's home with os module for cross platform work


class OUIData:
    def __init__(self, oui, org):
        self.oui = oui
        self.org = org

    @classmethod
    def download(cls, url, file):
        """This method is used to download OUI file to local machine"""
        cls.url = url
        cls.file = file
        try:
            a = requests.get(cls.url)
            print(a)
        except:
            pass

    def open(self):
        pass


    # TODO OuiDownloadFailed exception

OUIData.download(config.oui_url, config.oui_file)