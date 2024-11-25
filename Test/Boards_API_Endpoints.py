"""
API endpoints for Boards
"""
from BaseFolder.base_page import BaseClass
import requests
import time
import json
from boards_schemas import Schemas

class Boards_API_Endpoints(BaseClass):
    "Class for boards endpoints"

    def boards_url(self, suffix=''):
        self.base_url = self.get_url()
        return self.base_url + '/boards' + suffix

    def create_board(self, query):
        url = self.boards_url()
        response = requests.request("POST", url, params=query)
        print(response.status_code, response.url, response.text)
        resp = response.json()
        print(response.text)
        # schema validations
        validate_schemas = Schemas()
        print("^^^^^^^^", validate_schemas.creat_board_201(json.loads(response.text)))
        return resp


    def get_board(self,board_id,query):
        url = self.boards_url()
        response = requests.request("GET", url + "/" + board_id, params=query)
        print(response.status_code, response.url, response.text)
        assert response.status_code == 200, "Failed to get board"
        resp = response.json()
        return resp


    def update_board(self,board_id,query):
        url = self.boards_url()
        response = requests.request("PUT", url + "/" + board_id, params=query)
        print("update board response",response.text)
        print(response.status_code, response.url, response.text)
        assert response.status_code == 200, "Failed to update board"
        resp = response.json()
        validate_schemas = Schemas()
        print("^^^^^^^^^" , validate_schemas.update_board_200(json.loads(response.text)))
        return resp

    def delete_board(self,board_id,query):
        url = self.boards_url()
        time.sleep(20)
        response = requests.request("DELETE", url + "/" + board_id, params=query)
        #print(response.status_code, response.url, response.text)
        print(response.url)
        assert response.status_code == 200, "Failed to delete board"
        resp = response.json()
        return resp

