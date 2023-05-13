# from sre_compile import isstring
import pandas

squirrel = pandas.read_csv("D:\Software\Python\\New_Shit__\Angela_Yu__\Day_25 #usa_game\Squirrel_Data.csv")
# squirrel = pandas.read_csv("D:\Software\Python\\New_Shit__\Angela_Yu__\Day_25 #usa_game\squirrel_count.csv")

# colors = squirrel["Primary Fur Color"].to_list()
# color = list(i for i in set(colors) if isstring(i))
# sc = [colors.count(i) for i in color]

# fur_color = {"fur_color": color, "count": sc}

# print(fur_color)
# fur = pandas.DataFrame(fur_color)
# fur.to_csv("New_Shit__/Angela_Yu__/Day_25 #/squirrel_count.csv")

print(squirrel)
