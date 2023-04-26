with open("D:\Software\Python\\New_Shit__\Angela_Yu__\Day_26 #NATO_phonetic_alphabet\\file1.txt") as file1:
    with open("D:\Software\Python\\New_Shit__\Angela_Yu__\Day_26 #NATO_phonetic_alphabet\\file2.txt") as file2:
        file1 = [int(i) for i in file1]
        file2 = [int(i) for i in file2]

common_numbers = sorted([i for i in file1 if i in file2])
print(common_numbers)
