import random

random_list = [random.randint(1, 100) for _ in range(10)]
print("Исходный список:", random_list)

reversed_list = random_list[::-1]
print("Перевернутый список:", reversed_list)
