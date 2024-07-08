from src.utils import interact_with_user


def main() -> None:
    """
    Главная функция для взаимодействия с пользователем через консоль.
    Вызывает функцию interact_with_user().
    """

    try:
        interact_with_user()
    except Exception as e:
        print(f"При запуске возникла ошибка {e}")


if __name__ == "__main__":
    main()
