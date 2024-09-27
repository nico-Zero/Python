def run(num:int)->None:
    with open("hehe.txt","a",newline="\n",encoding="utf-8") as file:
        for i in range(num):
            file.write("\nHello, world! ")

run(10)
