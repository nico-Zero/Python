from random import shuffle

data = input("Enter a string to be encoded:- ")
indexes = list(range(len(data)))
shuffle(indexes)
de_key = {j: i for i, j in enumerate(data)}
en_key = {i: j for i, j in zip(data, indexes)}

print(de_key)
print(en_key)

encoded_message = [en_key[i] for i in indexes]
