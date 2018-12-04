#!/usr/bin/python3

import requests
import re

import config
import strings

# TODO localouifile in user's home with os module for cross platform work

ouiparseregex = r"^([0-9a-f]{6})\s*\(.{7}\)\s*(.+)$"

class OUIData:
    def __init__(self, oui, org):
        self.oui = oui
        self.org = org

    def download(self, url):
        self.url = url
        return requests.get(self.url)

    def open(self):
        pass


    # TODO OuiDownloadFailed exception

a = OUIData.download(config.oui_url)

print(re.search(ouiparseregex, a.text,'gmi'))