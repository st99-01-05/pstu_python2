import random

my_list_1 = [random.randint(1, 100) for _ in range(40)]
print("Исходный список:", random_list)

unique_list = list(set(my_list_1))
print("Список без дубликатов:", unique_list)