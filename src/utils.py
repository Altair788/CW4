from config import VACANCIES_JSON_PATH, SETTINGS_PATH
from src.api import HeadHunterAPI
from src.jsonsaver import JSONSaver
from src.vacancy import Vacancy


def interact_with_user():
    """
        Функция для взаимодействия с пользователем и управления работой программы.

        Функция предоставляет пользователю меню с различными действиями, такими как:
        - Поиск вакансий на hh.ru и сохранение их в файл
        - Вычисление средней зарплаты по сохраненным вакансиям
        - Вывод топ N вакансий по зарплате
        - Поиск вакансий по ключевому слову в описании

        Пользователь может выбирать действие, вводя соответствующий номер, и программа будет
        выполнять выбранное действие.
        """
    hh_api = HeadHunterAPI(SETTINGS_PATH)
    json_saver = JSONSaver(VACANCIES_JSON_PATH)

    while True:
        print("\nВыберите действие:")
        print("1. Ввести поисковый запрос для запроса вакансий из hh.ru")
        print("2. Узнать среднюю зарплату")
        print("3. Получить топ N вакансий по зарплате")
        print("4. Получить вакансии с ключевым словом в описании")
        print("5. Завершить работу")

        user_choice = input("Введите номер действия: ")

        if user_choice == "1":
            search_query = input("Введите поисковый запрос: ")
            hh_vacancies: list[dict] = hh_api.get_vacancies(search_query)
            json_saver.save_to_file(hh_vacancies)
            vacancies_list: list[Vacancy] = json_saver.get_vacancies_from_file()
            if len(vacancies_list) == 0:
                print("По вашему запросу вакансий не найдено. Введите другой запрос.")
            else:
                print("Вакансии успешно получены и сохранены в файл.")

        elif user_choice == "2":
            vacancies_list: list[Vacancy] = json_saver.get_vacancies_from_file()
            # Рассчитываем среднюю зарплату на основе списка вакансий и выводим
            average_salary: float = json_saver.calculate_average_salary(vacancies_list)
            print(f"Средняя зарплата по всем вакансиям: {average_salary}")

        elif user_choice == "3":
            top_count = int(input("Введите количество вакансий для вывода: "))
            sorted_vacancies: list[Vacancy] = sorted(json_saver.get_vacancies_from_file(),
                                                     key=lambda x: x.salary.get('from', 0),
                                                     reverse=True)
            top_vacancies: list[Vacancy] = sorted_vacancies[:top_count]

            print(f"Топ {top_count} вакансий по зарплате:")
            for vacancy in top_vacancies:
                print(vacancy)
                print()

        elif user_choice == "4":
            keyword = input("Введите ключевое слово (фразу) для поиска в описаниях вакансий: ")
            output_count = int(input("Введите количество вакансий для вывода: "))
            found_vacancies = []
            for vacancy in json_saver.get_vacancies_from_file():
                if keyword.lower() in vacancy.requirement.lower():
                    found_vacancies.append(vacancy)
            if found_vacancies:
                print(f"Список вакансий с ключевым словом (фразой) '{keyword}' в описании:")
                for vacancy in found_vacancies[:output_count]:
                    print(vacancy)
            else:
                print(f"Вакансий с ключевым словом '{keyword}' в описании не найдено.")

        elif user_choice == "5":
            print("Программа завершена.")
            break

        else:
            print("Некорректный ввод. Повторите попытку.")


if __name__ == "__main__":
    interact_with_user()
