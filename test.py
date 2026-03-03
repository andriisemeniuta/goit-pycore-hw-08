import json

# Твои данные (например, пробег и город)
# В памяти Python это просто объект (словарь)
my_trip = {
    "mileage": 1500,
    "last_city": "Berlin"
}

# СЕРИАЛИЗАЦИЯ (Процесс упаковки в файл)
# 1. Открываем файл 'data.json' для записи ('w' - write)
with open("data.json", "w") as f:
    # 2. Используем команду dump, чтобы "вывалить" данные в файл
    json.dump(my_trip, f)

print("Данные успешно упакованы в файл data.json!")