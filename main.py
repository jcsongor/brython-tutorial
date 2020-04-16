from browser import ajax, document
from browser.html import UL, LI
import json

class CharactersApi:
    @classmethod
    def get_all(cls, callback):
        ajax.get(
            "https://rickandmortyapi.com/api/character/1,2,3,4,5,6,7,8",
            oncomplete=cls._callback_with_result(callback)
            )

    @staticmethod
    def _callback_with_result(callback):
        return lambda req:callback(json.loads(req.text))




class Characters:
    def __init__(self, list_id, api):
        self._list = document[list_id]
        self._api = api

    def load(self):
        self._api.get_all(self.show_list)

    def show_list(self, items):
        self._list.html = ""
        self._list <= self._generate_list(items)

    def _generate_list(self, items):
        ul = UL()
        for item in items:
            ul <= self._generate_list_element(item)
        return ul

    def _generate_list_element(self, item):
        li = LI(item["name"])
        return li


characters = Characters(list_id="characters", api=CharactersApi)
characters.load()
