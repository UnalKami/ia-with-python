import os

def check_data(path):
    print(f'Current directory: {os.getcwd()}')

    data_path = path

    if os.path.exists(data_path):
        print('Data found')
        return True
    else:
        print('Missing data, please check!')
        return False

def calculate_total(quantity, price):
    return price*quantity

def format_currency(amount):
    return f'{amount:,.2f}'

check_data('data/sales.csv')