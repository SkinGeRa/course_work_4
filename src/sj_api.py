from src.abstract_classes import GetAPI
import requests


class SuperJobAPI(GetAPI):
    """
    Класс для работы с API сервиса SuperJob
    """

    def get_requests(self, vacancy):
        headers = {
            "X-Api-App-Id": "v3.r.116248728.6532cac47802b647c5688bb6219463b48eee2adf.c9404e770c3089eb5d02b8a6aca4fd214676433a"
        }
        params = {
            "keyword": vacancy,
            "page": "1"}

        superjob_vacancies = requests.get("https://api.superjob.ru/2.0/vacancies/",
                                          params=params,
                                          headers=headers)

        return superjob_vacancies.json()['objects']

    def get_vacancies(self, vacancy):
        data = self.get_requests(vacancy)
        vacancies = []
        for vacancy in data:
            area = vacancy['address']
            name = vacancy['profession']
            description = vacancy['candidat']
            employer = vacancy['firm_name']
            url = vacancy['link']
            salary_from = vacancy['payment_from']
            salary_to = vacancy['payment_to']
            currency = vacancy['currency']

            vacancies.append({'area': area, 'name': name, 'description': description, 'employer': employer, 'url': url,
                              'salary_from': salary_from, 'salary_to': salary_to, 'currency': currency})
        return vacancies
