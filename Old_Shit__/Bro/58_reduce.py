import functools
letter = ["H",'E','L','L','O']

word = functools.reduce(lambda x,y:x+y,letter)
print(word)

factorial = list(range(5,0,-1))
ans = functools.reduce(lambda x,y:x*y,factorial)
print(ans)
