def convert_to_title(f_name, l_name):
    if f_name == "":
        return "First Name is missing..."
    elif l_name == "":
        return "Last Name is missing..."
    else:
        return f_name.title(), l_name.title()


first_name = input("What is your first name? ")
last_name = input("What is your last name? ")

print(*convert_to_title(first_name, last_name))
