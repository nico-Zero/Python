with open("New_Shit__/Angela_Yu__/Day_26 #/file1.txt") as file1:
    with open("New_Shit__/Angela_Yu__/Day_26 #/file2.txt") as file2:
        file1 = [int(i) for i in file1]
        file2 = [int(i) for i in file2]

common_numbers = sorted([i for i in file1 if i in file2])
print(common_numbers)
