import random

dict1 = {}
dict2 = {}

for _ in range(5):
    key = str(random.randint(1, 100))
    value = random.uniform(1.0, 100.0)
    dict1[key] = value

for _ in range(5):
    key = str(random.randint(1, 100))
    value = random.uniform(1.0, 100.0)
    dict2[key] = value

print("Исходные словари:")
print("dict1:", dict1)
print("dict2:", dict2)

intersection = set(dict1.values()) & set(dict2.values())

new_dict = {}
for key, value in dict1.items():
    if value in intersection:
        new_dict[key] = value

print("Новый словарь:")
print(new_dict)