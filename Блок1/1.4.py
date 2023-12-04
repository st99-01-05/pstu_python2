import random

dictionary = {}

# В качестве ключей используем строки, а в качестве значений - целые числа или числа с плавающей точкой
for i in range(10):
    key = "key" + str(i)
    value = random.uniform(0, 1)
    dictionary[key] = value

print("Сгенерированный словарь:")
for key, value in dictionary.items():
    print(key, ":", value)

# Создаем пустой список для хранения кортежей
tuples_list = []
# Используем множество для хранения уже обработанных значений
processed_values = set()

for value in dictionary.values():
    if value in processed_values:
        continue
    keys = [key for key, val in dictionary.items() if val == value]
    tuple_value = (value, keys)
    tuples_list.append(tuple_value)
    processed_values.add(value)

print("Список кортежей:")
for tuple_value in tuples_list:
    print(tuple_value)