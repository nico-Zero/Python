def solution(lis):
    high_3 = lis[0] * lis[1] * lis[2]

    high_2 = lis[0] * lis[1]
    low_2 = lis[0] * lis[1]

    high = max(lis[0], lis[1])
    low = min(lis[0], lis[1])

    for num in lis[2:]:
        high_3 = max(high_3, num * low_2, num* high_2)
        high_2 = max(high_2, num * high, num * low)
        low_2 = min(low_2, num * high, num * low)
        high = max(high, num)
        low = min(low, num)
    return high_3

print(solution([1,2,3,4,5,6,7,-1,-3,-23,-9,-10,23,34,23,0,3,1]))
