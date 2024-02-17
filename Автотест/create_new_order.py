import data
import sender_stand_request

# Евгения Асташова, 13-я когорта — Финальный проект. Инженер по тестированию плюс

# Функция проверки позитивного сценария
def positive_assert():
    order_response = sender_stand_request.oder_by_numer()
    assert order_response.status_code == 200


# Тест 1. Успешное нахождение заказа по треку
def test_create_new_order_success_response():
    positive_assert()