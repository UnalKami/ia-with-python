import pandas as pd

from helpers import check_data, calculate_total, format_currency

path = 'data/sales.csv'

if check_data(path):
    df = pd.read_csv(path)

totals = []
for index, row in df.iterrows():
    totals.append(calculate_total(row['quantity'], row['price']))

df['total'] = totals

print('Sales Data:')
for index, row in df.iterrows():
    formatted_total = format_currency(row['total'])
    print(f'{row['product']}: {formatted_total}')

formatted_grand_total = format_currency(df['total'].sum())
print(f'Grand Total: {formatted_grand_total}')