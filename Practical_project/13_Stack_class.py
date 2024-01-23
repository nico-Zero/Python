from os import system


class Stack:
    def __init__(self, size=10):
        self.size = size
        self.body = []

    def is_empty(self):
        return len(self.body) == 0

    def push(self, value):
        if len(self.body) < self.size:
            self.body.append(value)
        else:
            print("Stack is full!!!")

    def pop(self):
        self.body.pop()

    def is_full(self):
        return len(self.body) == self.size

    def peek(self):
        return self.body[-1]

    def empty_stack(self):
        self.body.clear()


def run_stack(stack: Stack):
    command_list = [
        "exit",
        "push",
        "pop",
        "peek",
        "is_empty",
        "is_full",
        "empty_stack",
        "clear",
    ]
    while True:
        print(command_list)
        command = input("Enter a command to execute:- ")
        if command in ["Exit", "exit", "Quit", "quit", "/q", ":q"]:
            break
        elif command == "push":
            stack.push(input("Enter something to push:- "))
        elif command == "pop":
            stack.pop()
        elif command == "peek":
            top_value = stack.peek()
            print("The Top Value in stack is", top_value)
        elif command in ["is_empty", "isEmpty"]:
            is_empty = stack.is_empty()
            if is_empty:
                print("YES")
            else:
                print("NO")
        elif command in ["is_full", "isFull"]:
            is_full = stack.is_full()
            if is_full:
                print("YES")
            else:
                print("NO")
        elif command in ["empty", "empty_stack"]:
            stack.empty_stack()
        elif command in ["clear", "/c"]:
            system("cls")
        print()


def main():
    while True:
        str_size = input("Enter a stack size:- ")
        if str_size == "":
            size = ""
            break
        elif str_size.isnumeric():
            size = int(str_size)
            break
        else:
            print("There is a error in the input!!!")
    system("cls")
    stack = Stack(size=size) if size == "" else Stack()  # type: ignore
    run_stack(stack)


main()
