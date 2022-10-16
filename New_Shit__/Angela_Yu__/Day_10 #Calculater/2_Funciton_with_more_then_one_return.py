def convert_to_title(f_name, l_name):
    if f_name == "" or l_name =="":
        return "Nothing was Entered..."
    return f_name.title(), l_name.title()

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")

print(*convert_to_title(first_name, last_name))

