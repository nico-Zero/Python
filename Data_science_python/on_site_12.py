def unique(lis):
    cuch = {}
    for c in lis:
        if c not in cuch:
            cuch[c] = 1
        else:
            cuch[c] += 1
    for key in cuch:
        if cuch[key] == 1:
            return key
    return None

print(unique([2,3,2,3,4,4,3,43,4,53,45,3,45,34,53,4,3,4,3,4,4,5,34,34,4,31115,3,245,34,6456,475,8,678,568,56,78,45,673,45,4]))
