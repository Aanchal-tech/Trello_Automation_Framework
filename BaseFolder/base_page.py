import requests
import configparser
import os
import pytest

class BaseClass():

    def get_environment(self):
        ""
        self.config = configparser.ConfigParser()

        self.config.read('trello_automation_environment.cfg')
        self.env = self.config.get('system', 'environment')
        print("env****", self.env)
        return self.env

    def get_url(self):
        ""
        env = self.get_environment()
        self.config.read(env + '.cfg')
        url = self.config.get('base_url', 'url')

        return url
