# Ефремова Светлана, 12-я когорта — Финальный проект. Инженер по тестированию плюс
import data
import sender_request

# Сохранение номера трека заказа:
def track_order():
    return str(sender_request.post_new_order(data.order_body))

# Функция проверки 200 кода ответа:
def positive(track):
   order_response = sender_request.get_order_tract(track)
   assert order_response.status_code == 200

# Тест. Успех -код ответа 200 :
def test_kod_response():
     positive(track_order())


