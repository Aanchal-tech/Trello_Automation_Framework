
# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
import configparser

class Boards:

   def __init__(self):
      self.config = configparser.ConfigParser()

   def get_environment(self):

      self.config.read('trello_automation_environment.cfg')
      env = self.config.get('system', 'environment')
      return env

   def test_create_board(self):
      """Test create board endpoint"""

      # !/usr/local/bin/python
      env = self.get_environment()

      self.config.read(env+'.cfg')

      url = self.config.get('base_url', 'url')

      # url = "https://api.trello.com/1/boards/"
      query = {
         'key': 'B4ae622b3f45563d2339eaff8bc2a6f8',
         'token': 'cf151fa047b52d4a9101fb3734a3f150cb8bc3da9c0a6e447ee200146c5d279b',
         'name': 'test'
      }
      response = requests.request("POST",url,params=query)
      print(response.status_code, response.url ,response.text)
      assert response.status_code == 201, "Failed to create new board"

      resp = response.json()
      return resp['id']




tmp = Boards()
tmp.test_create_board()
