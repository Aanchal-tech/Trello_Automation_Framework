import time
# from Constants import Login_credentials
import requests
import pytest


class TrelloAutomation:

    def __init__(self, key= Login_credentials.login_key,
                 token= Login_credentials.login_token):
        self.key = key
        self.token = token

    def create_board(self):
        """Create new trello board"""

        params = {'key': self.key, 'token': self.token, 'name': 'Board_6'}
        b = requests.post("https://api.trello.com/1/boards", params=params)
        print(b.text)
        ddict = b.json()
        id = ddict['id']
        return id

    def create_list(self):
        """Create list in new board"""

        board_id = self.create_board()
        params = {'key': self.key, 'token': self.token, 'name': 'WORK', 'idBoard': board_id}
        l = requests.post("https://api.trello.com/1/lists", params=params)
        print(l.text)
        ddict = l.json()
        list_id = ddict['id']
        print("list_id: ", list_id)
        return list_id

    def create_card_list(self):
        """Create card in new list"""

        list_id = self.create_list()
        params = {'key': self.key, 'token': self.token, 'idList': list_id}
        add_card_in_list = requests.request("POST", 'https://api.trello.com/1/cards', params=params)
        print("adding card into list:", add_card_in_list.text)
        dict = add_card_in_list.json()
        card_id = dict['id']
        print("card_id: ", card_id)
        return card_id

    # def create_attachment_card(self):
    #     """Create attachment in to card"""
    #     headers = {
    #         "Accept": "application/json"
    #     }
    #     card_id = self.create_card_list()
    #     params = {'key': self.key, 'token': self.token, 'url': 'https://unsplash.com/photos/odxB5oIG_iA'}
    #     attachment_on_card = requests.post('https://api.trello.com/1/cards/' + card_id + '/attachments',
    #                                        headers=headers, params=params)
    #     print("create attcahemnt on card", attachment_on_card.text)
    #     dictt = attachment_on_card.json()
    #     attachment_id = dictt['id']
    #     print("attachment_id", attachment_id)
    #     return attachment_id

    def Delete_card(self):
        """Delete card """
        list_id = self.create_list()
        card_id = self.create_card_list()
        params = {'key': self.key, 'token': self.token, 'idList': list_id, 'id': card_id}
        req = requests.Request("DELETE", 'https://api.trello.com/1/cards/' + card_id, params=params)
        # prepared = req.prepare()
        print("url : ", req.url)
        # print("Deleting  card into list:",Delete_card_in_list)

    def Delete_Board(self):
        """Delete Board"""

        board_id = self.create_board()
        time.sleep(15)
        params = {'key': self.key, 'token': self.token}
        req = requests.delete("https://api.trello.com/1/boards/" + board_id, params=params)
        print("url : ", req.url)


tmp = TrelloAutomation()
tmp.Delete_Board()
