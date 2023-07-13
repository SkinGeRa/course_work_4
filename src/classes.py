import requests
import json


class API:

    def get_request(self):
        pass


class HeadHunterAPI(API):

    def __init__(self, keyword):
        self.keyword = keyword
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
        # return json.dumps(response, indent=2, ensure_ascii=False)
        return response

    def get_vacancies(self):
        vacancies = []
        item = self.get_request()
        for index in range(10):
            print(item['items'][index]["name"])
            print(item['items'][index]["salary"])
            print(item['items'][index]["alternate_url"])
            print(item['items'][index]["snippet"])



class SuperJobAPI(API):

    def __init__(self, keyword=input(), pages=input()):
        self.keyword = keyword
        self.pages = pages

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
        return json.dumps(response, indent=2, ensure_ascii=False)

    def get_vacancies(self):
        vacancies = []
        for vacancy in self.get_request():
            # vacancies.append({
            #     vacancy,
                # "title": vacancy["name"],
                # "url": vacancy["alternate_url"],
                # "description": vacancy["snippet"]["requirement"]
            # })
        # print(vacancies)
            print(vacancy["objects"])


i = HeadHunterAPI("python")
# for i in i.get_request():
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

