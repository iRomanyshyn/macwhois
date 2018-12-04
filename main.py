#!/usr/bin/python3

# TODO localouifile in user's home with os module for cross platform work


class OuiData:
    def __init__(self, oui, org):
        self.oui = oui
        self.org = org
        # TODO 'download' method, 'open' method (with pickle or similar), OuiDownloadFailed exception