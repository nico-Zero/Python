from random import shuffle

data = input("Enter a string to encode:- ")
indexs = list(range(len(data))) 
shuffle(indexs)
print(indexs)

encoded_data = [data[i] for i in indexs]
print("".join(encoded_data))
