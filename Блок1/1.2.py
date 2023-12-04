import random

my_list_1 = []
my_list_2 = []
n = 100
for i in range(n):
    my_list_1.append(random.randint(1, 99))
    my_list_2.append(random.randint(1, 99))
print(my_list_1)
print(my_list_2)

my_result = my_list_1[::2] + my_list_2[1::2]
print(my_result)