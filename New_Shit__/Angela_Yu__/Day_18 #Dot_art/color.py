import colorgram


def colors(j: int):
    x = colorgram.extract("New_Shit__/Angela_Yu__/Day_18 #/pic/five.jpeg", j)
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
    "RebeccaPurple",
    "DarkMagenta",
    "MediumSlateBlue",
]

