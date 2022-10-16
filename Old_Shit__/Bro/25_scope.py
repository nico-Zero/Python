name = "jack"
def d_name():
    name= "Code" # local variable
    global g_name
    g_name = "g_name"
    print(name)

d_name()
print(name)
print(g_name) # global variable
