import requests
import json


class API:

    def get_request(self):
        pass


class HeadHunterAPI(API):

    def __init__(self, keyword, pages):
        self.keyword = keyword
        self.pages = pages

    def get_request(self):
        for page in self.pages:
            url = "https://api.hh.ru/vacancies"
            params = {
                "per_page": 100,
                "page": page,
                "text": self.keyword,
                "archive": False
            }

            response = requests.get(url, params=params).json()
            # print(json.dumps(response, indent=2, ensure_ascii=False))
            # return json.dumps(response, indent=2, ensure_ascii=False)
            return response

    def get_vacancies(self):
        vacancies = []
        for vacancy in self.get_request():
            vacancies.append({
                "salary": vacancy,
                # "title": vacancy["name"],
                # "url": vacancy["alternate_url"],
                # "description": vacancy["snippet"]["requirement"]
            })
        print(vacancies)


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


i = HeadHunterAPI("python", "3")
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

