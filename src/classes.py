import requests
import json


class API:

    def get_request(self):
        pass


class HeadHunterAPI(API):

    def __init__(self):
        pass

    @staticmethod
    def get_request(keyword="python"):
        url = "https://api.hh.ru/vacancies"
        params = {
            "per_page": 100,
            "page": 0,
            "text": keyword,
            "archive": False
        }

        response = requests.get(url, params=params).json()
        print(json.dumps(response, indent=2, ensure_ascii=False))


class SuperJobAPI(API):

    def __init__(self):
        pass

    @staticmethod
    def get_request(keyword="python"):
        url = "https://api.superjob.ru/2.0/vacancies"
        params = {
            "count": 100,
            "page": 0,
            "keyword": keyword,
            "archive": False
        }

        headers = {
            "X-Api-App-Id":
                "v3.r.116248728.6532cac47802b647c5688bb6219463b48eee2adf.c9404e770c3089eb5d02b8a6aca4fd214676433a"
        }

        response = requests.get(url, params=params, headers=headers).json()
        print(json.dumps(response, indent=2, ensure_ascii=False))


print(HeadHunterAPI.get_request())
