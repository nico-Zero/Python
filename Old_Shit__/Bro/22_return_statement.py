def calculater(num):
    try:
        return eval(num)
    except:
        pass

while True:
    print("=",calculater(input(">>>")))