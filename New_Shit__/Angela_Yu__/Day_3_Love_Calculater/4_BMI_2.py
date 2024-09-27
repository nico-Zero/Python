while 1:
    weight = input("Enter your weight in kg: ")

    if weight == "exit":
        print("Exiting...")
        break

    height = input("Enter your height in m: ")

    if height == "exit":
        print("Exiting...")
        break

    BMI = round(float(weight) / (float(height) ** 2), 2)

    if BMI <= 18.5: 
        print(f"Your BMI is {BMI}, You are underweight.")
    elif BMI <= 25:
        print(f"Your BMI is {BMI}, You are normal weight.")
    elif BMI <= 30:
        print(f"Your BMI is {BMI}, You are overweight.")
    elif BMI <= 35:
        print(f"Your BMI is {BMI}, You are obese.")
    elif BMI:
        print(f"Your BMI is {BMI}, You are clinically obese.")
