def reverse(string, helper = ""):
    if isinstance( string, str):
        string = list(string)
    if len(string) == 0:
        return helper
    else:
        helper += string.pop()
        return reverse(string,helper)

print(reverse("helkafljasd"))
