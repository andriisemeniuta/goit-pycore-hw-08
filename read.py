import json

# ДЕСЕРИАЛИЗАЦИЯ (Процесс распаковки из файла)
# 1. Открываем тот же файл, но теперь для чтения ('r' - read)
with open("data.json", "r") as f:
    # 2. Команда load "загружает" данные обратно в переменную
    yesterday_data = json.load(f)

print(f"Программа вспомнила! Вчерашний пробег: {yesterday_data['mileage']} км. and last city war {yesterday_data['last_city']} ")