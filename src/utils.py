from config import VACANCIES_JSON_PATH
from src.api import HeadHunterAPI
from src.file_manager import JSONSaver
from src.vacancy import Vacancy


def interact_with_user():
    file_path = VACANCIES_JSON_PATH  # Укажите путь к файлу JSON
    json_saver = JSONSaver(file_path)
    hh_api = HeadHunterAPI(file_path)  # Передаем путь к файлу для API hh.ru

    while True:
        print("\nВыберите действие:")
        print("1. Ввести поисковый запрос для запроса вакансий из hh.ru")
        print("2. Получить топ N вакансий по зарплате")
        print("3. Получить вакансии с ключевым словом в описании")
        print("4. Завершить работу")

        user_choice = input("Введите номер действия: ")

        if user_choice == "1":
            search_query = input("Введите поисковый запрос: ")
            vacancies = hh_api.get_vacancies(search_query)
            for vacancy in vacancies:
                json_saver.add_vacancy(vacancy)
            print("Вакансии успешно получены и сохранены в файл.")

        elif user_choice == "2":
            top_count = int(input("Введите количество вакансий для вывода: "))
            sorted_vacancies = sorted(json_saver.get_vacancies(), key=lambda x: x.salary.get('from', 0), reverse=True)
            top_vacancies = sorted_vacancies[:top_count]
            print(f"Топ {top_count} вакансий по зарплате:")
            for vacancy in top_vacancies:
                print(vacancy)

        elif user_choice == "3":
            keyword = input("Введите ключевое слово для поиска в описании: ")
            relevant_vacancies = [v for v in json_saver.get_vacancies() if keyword in v.requirement]
            print(f"Вакансии с ключевым словом '{keyword}' в описании:")
            for vacancy in relevant_vacancies:
                print(vacancy)

        elif user_choice == "4":
            print("Программа завершена.")
            break

        else:
            print("Некорректный ввод. Повторите попытку.")


if __name__ == "__main__":
    interact_with_user()
