class OrderData:
    #тестовые данный для заказа
    # Набор данных 1 - для кнопки Заказать в шапке страницы
    ORDER_SET_TOP = {
        "name": "Евгений",
        "surname": "Онегин",
        "address": "ул. Ленина, д. 10",
        "metro": "Черкизовская",
        "phone": "+79131234567",
        "date": "19.06.2026",
        "rental_period": "сутки",
        "color": "black",
        "comment": "Позвоните за час",
        "button_location": "top"
    }
    
    # Набор данных 2 - для кнопки Заказать внизу страницы
    ORDER_SET_BOTTOM = {
        "name": "Анна",
        "surname": "Ахматова",
        "address": "пр. Мира, д. 25",
        "metro": "Сокольники",
        "phone": "+79137654321",
        "date": "20.06.2026",
        "rental_period": "двое суток",
        "color": "grey",
        "comment": "",
        "button_location": "bottom"
    }
    
    #список всех наборов данных
    ORDER_SETS = [ORDER_SET_TOP, ORDER_SET_BOTTOM]
    
    #URL для проверки логотипов
    SCOOTER_EXPECTED_URL = "https://qa-scooter.education-services.ru/"
    YANDEX_EXPECTED_DOMAINS = ["ya.ru", "dzen.ru", "yandex.ru"]