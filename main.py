from browser import ajax
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




