is_male = True
if is_male == True:
    print("You are a male.")
else:
    print("You are not a male.")

is_male = False
if is_male == True:
    print("You are a male.")
else:
    print("You are not a male.")

is_male = True
is_tall = True
if is_male or is_tall:
    print("You are a male or tall or both.")
else:
    print("You nither male nor tall.")


is_male = True
is_tall = True
if is_male and is_tall:
    print("You are a tall male.")
else:
    print("You nither male nor tall nor both.")

is_male = True
is_tall = True
if is_male and is_tall:
    print("You are a tall male.")
elif is_male and not (is_tall):
    print("You are short male.")
elif not (is_male) and is_tall:
    print("You are not male but tall.")
else:
    print("You nither male nor tall nor both.")
