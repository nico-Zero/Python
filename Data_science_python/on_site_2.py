from functools import reduce

inp = [1,2,3,4]

def cal_p(inp:list):
    result = []
    for i in range(len(inp)):
        result.append(reduce(lambda x,y : x * y ,inp[:i] + inp[i+1:] ))
    return result

print(cal_p(inp))
