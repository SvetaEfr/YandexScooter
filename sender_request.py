import configuration
import requests
import data

# Создание заказа:
def post_new_order(body):
    new_order = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body, headers=data.headers).json()
    return (new_order['track'])


# Получение заказа по треку:
def get_order_tract(track):
     return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH + track)




