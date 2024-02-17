import configuration
import data
import requests
# Евгения Асташова, 13-я когорта — Финальный проект. Инженер по тестированию плюс

# Функция создания нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)


# Функция получения трека заказа
def get_order_track():
    response = post_new_order(data.order_body)
    new_order = response.json()
    track = "?t=" + str(new_order["track"])
    return track


# Функция поиска заказа по номеру
def oder_by_numer():
    track = get_order_track()
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK + track)