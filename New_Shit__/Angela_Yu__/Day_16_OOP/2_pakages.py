from prettytable import PrettyTable
from random import randint
from faker import Faker


f = Faker()
table = PrettyTable()

table.add_column(str(randint(1, 10)), [f.name() for _ in range(10)])
table.border = False
table.header = False


table.clear()

table.add_column(str(randint(1, 10)), [f.name() for _ in range(10)])
table.align = 'l'

print(table)
print()
