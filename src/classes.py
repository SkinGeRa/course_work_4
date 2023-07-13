import requests
import json


class API:

    def get_request(self):
        pass


class HeadHunterAPI(API):

    def __init__(self):
        self.keyword = input()
        self.pages = input()

    def get_request(self):
        url = "https://api.hh.ru/vacancies"
        params = {
            "per_page": 100,
            "page": self.pages,
            "text": self.keyword,
            "archive": False,
            "only_with_salary": True
        }

        response = requests.get(url, params=params).json()
        return response

    def get_vacancies(self):
        vacancies_hh = []
        item = self.get_request()
        for index in range(1):
            vacancies_hh.append(dict(name=item['items'][index]["name"], salary=item['items'][index]["salary"],
                                     url=item['items'][index]["alternate_url"], desk=item['items'][index]["snippet"]))
        return vacancies_hh


class SuperJobAPI(API):

    def __init__(self):
        self.keyword = input()
        self.pages = input()

    def get_request(self):
        url = "https://api.superjob.ru/2.0/vacancies"
        params = {
            "count": 100,
            "page": 0,
            "keyword": self.keyword,
            "archive": False
        }

        headers = {
            "X-Api-App-Id":
                "v3.r.116248728.6532cac47802b647c5688bb6219463b48eee2adf.c9404e770c3089eb5d02b8a6aca4fd214676433a"
        }

        response = requests.get(url, params=params, headers=headers).json()
        return response

    def get_vacancies(self):
        vacancies_sj = []
        item = self.get_request()
        for index in range(1):
            vacancies_sj.append(
                dict(name=item['objects'][index]["profession"], salary=item['objects'][index]["payment_from"],
                     url=item['objects'][index]["link"], desk=item['objects'][index]["candidat"]))
        return vacancies_sj


i = SuperJobAPI()
print(i.get_vacancies())


class Vacancy:
    def __init__(self, title, url, salary, description):
        self.title = title
        self.url = url
        self.salary = salary
        self.description = description

    def __gt__(self, other):
        return self.salary > other.salary


class JSON:
    def add_vacancy(self):
        pass

    def get_vacancies_by_salary(self):
        pass

    def delete_vacancy(self):
        pass


class JSONSaver(JSON):

    def save_vacancy(self):
        pass
