r1 = {
        "x":2,
        "y":4,
        "w":5,
        "h":12,
        }
r2 = {
        "x":2,
        "y":2,
        "w":7,
        "h":14,
        }
def is_overlap(r1, r2):
    result = {
            "x":None,
            "y":None,
            "w":None,
            "h":None,
            }
    left = max(r1["x"], r2["x"])
    right = min(r1["x"]+r1["w"], r2["x"]+r2["w"])
    top = max(r1["y"], r2["y"])
    bottom = min(r1["y"]+r1["h"], r2["y"]+r2["h"])
    if left >= right or top >= bottom:
        return result

    result["x"],result["w"] = left, right - left
    result["y"],result["h"] = top, bottom - top

    return result
    
print(is_overlap(r1, r2))

