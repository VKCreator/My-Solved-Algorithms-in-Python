# 1

month_expense = [2200, 2350, 2600, 2130, 2190]

print(month_expense[1] - month_expense[0])
print(sum(month_expense[:3]))
print(2000 in month_expense)
month_expense.append(1980)
month_expense[3] -= 200
print(month_expense[3])
print(month_expense)

# 2

heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']
print(len(heros))
heros.append('black panther')
heros.remove('black panther')
heros.insert(3, 'black panther')
# heros = ['doctor strange' if i in ('thor', 'hulk') else i for i in heros]
heros[1:3] = ['doctor strange']
print(dir(heros))
heros.sort()
print(heros)

# 3

max_value = int(input('Enter a number: '))

l_odd = [i for i in range(1, max_value + 1) if i % 2]
print(l_odd)

l_odd2 = list(filter(lambda x: x % 2, range(1, max_value + 1)))
print(l_odd2)
