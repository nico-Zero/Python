def remDupKey(st):
    cuch = ""
    for c in st:
        if c == " ":
            cuch += " "
        elif c in cuch:
            continue
        else:
            cuch += c
    return cuch

print(remDupKey("yuvraj iijjkk mahilange, iijj"))

