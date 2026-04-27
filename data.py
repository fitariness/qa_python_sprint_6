class OrderTestData:
    """Данные для позитивного сценария заказа"""

    USER_TOP = {
        "name": "Иван",
        "last_name": "Петров",
        "address": "Москва, ул. Ленина, д. 10, кв. 5",
        "metro_station": "Сокольники",
        "phone": "+79991234567",
        "delivery_date": "27.04.2026",
        "rental_period": "сутки",
        "color": "black",
        "comment": "Позвоните за час",
    }

    USER_BOTTOM = {
        "name": "Мария",
        "last_name": "Сидорова",
        "address": "Санкт-Петербург, Невский проспект, 20",
        "metro_station": "Черкизовская",
        "phone": "+79167654321",
        "delivery_date": "28.04.2026",
        "rental_period": "двое суток",
        "color": "grey",
        "comment": "Оставьте у двери",
    }
