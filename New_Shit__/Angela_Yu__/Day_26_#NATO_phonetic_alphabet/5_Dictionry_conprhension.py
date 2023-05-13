from faker import Faker
from prettytable import PrettyTable

fake = Faker()
index = int(input("Enter index length: "))
name_list = (fake.name() for i in range(index))
zipcode_list = (fake.phone_number() for i in range(index))

hitman = {i: j for i, j in zip(name_list, zipcode_list)}


display = PrettyTable()
display.align = "l"

display.field_names = ("Name", "Phone")
display.add_rows(hitman.items())
print(display)

black_hitman = {i:j for i, j in hitman.items() if int(str(j)[-2:]) >= 69}
display.clear()
display.header = False
display.title = "Black_Hitman"
display.add_rows(black_hitman.items())

print(display)
