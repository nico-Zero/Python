import random

def choice(x):
    return random.randint(0,len(x)-1)

fruits = ["mango","apple","orange","banana","jalo","Pinaaple"]
name = ["yuvraj","Zeronico","rona","jack","tony"]

name.append("Jhonsion")
name.extend(["Nova","zero","natasa","dakofe","tastor"])

print(f"{name[choice(name)].upper()} ate {fruits[choice(fruits)].upper()}")
