sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

len_of_sentences = {i: len(i) for i in sentence.split(" ")}

print(*len_of_sentences.items(), sep="\n")
