itens = [('Bubblegum', 202), ('Toffee', 118), ('Ice cream', 2250), ('Milk chocolate', 1680), ('Doughnut', 1075), ('Pancake', 80)]
print('Earned amount:')
income = 0
for item, price in itens:
    income += price
    print(f'{item}: ${price}')
print(f'\nIncome: ${income}')

staff_expenses = int(input('Staff expenses:\n '))
other_expenses = int(input('Other expenses:\n '))
print(f'Net income: ${income - (staff_expenses + other_expenses)}')