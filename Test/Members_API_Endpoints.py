"""
API endpoints for Boards
"""
from BaseFolder.base_page import BaseClass
import requests


class Members_API_Endpoints(BaseClass):
    "Class for boards endpoints"

    def member_url(self, suffix=''):
        self.base_url = self.get_url()
        return self.base_url + '/members/me/boards' + suffix

    def get_member_boards(self, query):
        url = self.member_url()
        response = requests.request("GET", url, params=query)
        #print(response.status_code, response.url, response.text)
        assert response.status_code == 200, "Failed"
        resp = response.json()
        return resp
        # print("get boards members", json.dumps(resp, indent=4))




        # url = self.boards_url()
        # response = requests.request("POST", url, params=query)
        # print(response.status_code, response.url, response.text)
        # resp = response.json()
        # # schema validations
        # return resp
