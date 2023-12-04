import json

budget_data = {}

def load_budget_data():
    global budget_data
    try:
        with open('budget_data.json', 'r') as file:
            budget_data = json.load(file)
    except FileNotFoundError:
        pass

def save_budget_data():
    with open('budget_data.json', 'w') as file:
        json.dump(budget_data, file)

def add_transaction(description, amount, category):
    if category not in budget_data:
        budget_data[category] = []
    budget_data[category].append({'описание': description, 'сумма': amount})

def print_budget_summary():
    for category, transactions in budget_data.items():
        print(f'Категория: {category}')
        total_amount = sum(transaction['amount'] for transaction in transactions)
        print(f'Общая сумма: {total_amount}')
        for transaction in transactions:
            print(f'{transaction["description"]}: {transaction["amount"]}')
        print()

load_budget_data()
print('Добро пожаловать на бюджетный трекер!')

while True:
    action = input('Введите действие (add/summary/exit): ')
    if action == 'add':
        description = input('Введите описание: ')
        amount = float(input('Введите сумму: '))
        category = input('Введите категорию: ')
        add_transaction(description, amount, category)
    elif action == 'summary':
        print_budget_summary()
    elif action == 'exit':
        save_budget_data()
        print('Бюджетные данные сохранены. До встречи!')
        break
    else:
        print('Недопустимое действие. Пожалуйста, попробуйте снова')
