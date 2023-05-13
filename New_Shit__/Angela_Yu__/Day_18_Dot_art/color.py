import colorgram


def colors(j: int):
    x = colorgram.extract("D:\Software\Python\\New_Shit__\Angela_Yu__\Day_18 #Dot_art\pic\\five.jpeg", j)
    return [(i.rgb.r, i.rgb.g, i.rgb.b) for i in x]


color_list = [
    "Crimson",
    "DarkRed",
    "DeepPink",
    "DarkGreen",
    "OrangeRed",
    "DarkKhaki",
    "Lavender",
    "Magenta",
    "DarkMagenta",
    "MediumSlateBlue",
]

print(colors(10))
