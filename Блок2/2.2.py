import json

task_data = {}

def load_task_data():
    global task_data
    try:
        with open('task_data.json', 'r') as file:
            task_data = json.load(file)
    except FileNotFoundError:
        pass

def save_task_data():
    with open('task_data.json', 'w') as file:
        json.dump(task_data, file)

def add_task(description, category):
    if category not in task_data:
        task_data[category] = []
    task_data[category].append({'description': description, 'completed': False})

def mark_task_completed(category, index):
    if category in task_data and index < len(task_data[category]):
        task_data[category][index]['completed'] = True

def print_task_summary():
    for category, tasks in task_data.items():
        print(f'Category: {category}')
        for i, task in enumerate(tasks):
            status = 'Задача выполнена' if task['completed'] else 'Задача не выполнена'
            print(f'{i + 1}. {task["description"]} - {status}')
        print()

load_task_data()
print('Welcome to the task tracker!')

while True:
    action = input('Введите действие (1 - добавить; 2 - завершить; 3 - сводка; 4 - выход): ')
    if action == '1':
        description = input('Введите описание: ')
        category = input('Введите категорию: ')
        add_task(description, category)
    elif action == '2':
        category = input('Введите категорию задачи, которую вы хотите отметить как выполненную: ')
        index = int(input('Введите индекс задачи, которую нужно отметить как выполненную: ')) - 1
        mark_task_completed(category, index)
    elif action == '3':
        print_task_summary()
    elif action == '4':
        save_task_data()
        print('Данные задачи сохранены. До встречи!')
        break
    else:
        print('Недопустимое действие. Пожалуйста, попробуйте снова.')