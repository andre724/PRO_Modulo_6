import pytest 
from requests import get,post
from json import loads


class TestAPI:
    def setup(self):
        self.url = "http://127.0.0.1:8000"

    def test_APIstatus(self):
        resp = get(self.url)
        assert resp.ok
    
    def test_APIresponse(self):
        resp = get(self.url)
        message = loads(resp.text)
        assert message["message"] == "Hello World"
    
    def test_POSTmethod(self):
        resp = post(self.url + "/operador/"
        , json = {"valor1": 2, "valor2": 3, "operador":'+'})

        result = loads(resp.text)
        resposta_esperada = {
             "resultado": 5   
        }
        assert result == resposta_esperada
