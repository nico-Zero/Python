x = True
y = False

temp = int(input("Enter the temperature:- "))

if temp >= 0 and temp <= 30:
    print("Temperature is good today","Just go outside and have fun.",sep="\n")
elif temp <= 0 or temp >= 30:
    print("Temperaure is really bad today","fuck you world",sep="\n")
    
print()
if not (temp >= 0 and temp <= 30):
    print("Temperature is good today","Just go outside and have fun.",sep="\n")
elif not (temp <= 0 or temp >= 30):
    print("Temperaure is really bad today","fuck you world",sep="\n")
