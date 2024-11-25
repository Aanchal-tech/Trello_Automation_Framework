import os
import sys
import pytest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# from endpoints.API_Player import API_Player
from BaseFolder.base_page import BaseClass




import json

import time
from BaseFolder.base_page import BaseClass
import requests
import configparser
from Members_API_Endpoints import Members_API_Endpoints
# from . base_page import BaseClass
from Boards_API_Endpoints import Boards_API_Endpoints


class TestBoards(BaseClass):


    # #@pytest.mark.skip
    def test_delete_all_board(self):

        env = self.get_environment()
        self.config.read(env + '.cfg')

        #url = self.config.get('base_url', 'url')
        trello_key = self.config.get('auth', 'key')
        trello_token = self.config.get('auth', 'token')
        query = {
            'key': trello_key,
            'token': trello_token,
        }
        # url ="https://api.trello.com/1/members/me/boards"
        self.api_obj = Members_API_Endpoints()
        resp = self.api_obj.get_member_boards(query)
        # response = requests.request("GET", url, params=query)
        # print(response.status_code, response.url, response.text)
        # assert response.status_code == 200, "Failed to delete all board"
        # resp = response.json()
        # print("get boards members", json.dumps(resp, indent=4))
        for dict in resp:
            print(dict['id'])
            self.test_delete_board(dict['id'])
        return resp


    def test_create_board(self):
        """Test create board endpoint
        Steps:
        1. Login to the Trello
        2. Create board
        3. Verify status code as 200
        .. Verify response schema
        .. Verify board name in Get boards response
        5. Delete board
        6. Verify status code as 200
        """
        env = self.get_environment()
        self.config.read(env + '.cfg')
        # url = self.config.get('base_url', 'url')
        trello_key = self.config.get('auth', 'key')
        trello_token = self.config.get('auth', 'token')
        query = {
            'key': trello_key,
            'token': trello_token,
            'name': 'test'
        }

        self.api_obj = Boards_API_Endpoints()
        resp = self.api_obj.create_board(query)
        # response = requests.request("POST", url, params=query)
        # print(response.status_code, response.url, response.text)
        # assert response.status_code == 200, "Failed to create new board"
        # resp = response.json()
        #print(query['name'])
        assert resp['name'] == query['name'], "Failed to verify board name - Incorrect board name"
        return resp['id']




    # def test_get_board(self):
    #
    #     board_id = self.test_create_board()
    #     env = self.get_environment()
    #     self.config.read(env + '.cfg')
    #
    #     #url = self.config.get('base_url', 'url')
    #     trello_key = self.config.get('auth', 'key')
    #     trello_token = self.config.get('auth', 'token')
    #     query = {
    #         'key': trello_key,
    #         'token': trello_token,
    #     }
    #     self.api_obj = Boards_API_Endpoints()
    #     resp = self.api_obj.get_board(board_id,query)
    #     # response = requests.request("GET", url+ board_id, params=query)
    #     # print(response.status_code, response.url, response.text)
    #     # assert response.status_code == 200, "Failed to get board"
    #     # resp = response.json()
    #     return resp['id']


    def test_update_board(self):
        board_id = self.test_create_board()
        #url = self.get_url()
        trello_key = self.config.get('auth', 'key')
        trello_token = self.config.get('auth', 'token')
        query = {
            'key': trello_key,
            'token': trello_token,
        }
        #time.sleep(20)
        self.api_obj = Boards_API_Endpoints()
        resp = self.api_obj.update_board(board_id,query)
        # response = requests.request("PUT", url + board_id, params=query)
        # print("update board response",response.text)
        # print(response.status_code, response.url, response.text)
        # assert response.status_code == 200, "Failed to update board"
        # resp = response.json()
        print("response bord id", resp['id'])
        return resp['id']



    def test_delete_board(self,board_id = None):

        if board_id is None:
            #board_id = self.test_create_board()
            pass
    #     # env = self.get_environment()
         # self.config.read(env + '.cfg')
         # url = self.config.get('base_url', 'url')
        else:
            #url = self.get_url()

            trello_key = self.config.get('auth', 'key')
            trello_token = self.config.get('auth', 'token')
            query = {
                'key': trello_key,
                'token': trello_token,
            }
        #
        #     # url = url + board_idd
        #     # print("url*****************", url)
        #     time.sleep(20)
        #     response = requests.request("DELETE", url + board_id, params=query)
        #     print(response.status_code, response.url, response.text)

            self.api_obj = Boards_API_Endpoints()
            resp = self.api_obj.delete_board(board_id,query)

            #assert resp.status_code == 200, "Failed to delete board"
        #     resp = response.json()
            return resp


tmp = TestBoards()
tmp.test_update_board()
