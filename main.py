#!/usr/bin/python3

import requests  # For easy OUI file downloading
import re  # For regular expressions
import pickle  # To save and load local OUI data

import config  # Our config file
import strings  # Our strings file


ouipattern = r"([0-9a-fA-F]{6})\s+\(.{7}\)\s+(.+)\n\s*(.*)\n\s*(.*)\n\s*(.*)"  # Seems to be good


class OUIData:
    def __init__(self, url: str, file: str):
        self.url = url
        self.file = file

        self.open()

    def open(self):
        try:
            with open(self.file, 'rb') as ouifile:
                ouidata = pickle.load(ouifile)
        except Exception as exc:
            print(strings.fail_open, exc)
            self.recieveandparse()
        for oui in ouidata:
            yield oui

    def recieveandparse(self, forced: bool = False):
        print(strings.downloading)
        try:
            downloaded = requests.get(config.oui_url)  # TODO exceptions
        except Exception as exc:
            print(strings.fail_all, exc)
            if not forced:
                print(strings.fail_all)
                exit(1)
        if downloaded.ok:
            ouidata = re.findall(ouipattern, downloaded.text)
            return ouidata


    def save(self):
        pass  # TODO


ouidata = OUIData(config.oui_url, config.oui_file)

ouilist = list(ouidata.recieveandparse())

for i in range(len(ouilist)):
    print("OUI {} is {} based in {}".format(ouilist[i][0], ouilist[i][1], ouilist[i][4]))