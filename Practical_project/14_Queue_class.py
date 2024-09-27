from os import system


class Queue:
    def __init__(self, size=10):
        self.size = size
        self.body = []

    def enqueue(self, value):
        if len(self.body) < self.size:
            self.body.append(value)
        else:
            print("Queue is full!!!")

    def dequeue(self):
        self.body.pop(0)

    def peek(self):
        return self.body[0]

    def is_empty(self):
        return len(self.body) == 0

    def is_full(self):
        return len(self.body) == self.size

    def empty_queue(self):
        self.body.clear()


def run_queue(queue: Queue):
    command_list = [
        "exit",
        "clear",
        "enqueue",
        "dequeue",
        "peek",
        "is_empty",
        "is_full",
        "empty_queue",
    ]
    while True:
        print(command_list)
        command = input("Enter a command to execute:- ")
        if command in ["exit", "Exit", "quit", "Quit", "/q", ":q", "/Q", ":Q"]:
            break
        elif command in ["clear", "cls", "/c", ":c"]:
            system("cls")
        elif command == "enqueue":
            queue.enqueue(input("Enter a enqueue value:- "))
        elif command == "dequeue":
            queue.dequeue()
        elif command == "peek":
            first_item = queue.peek()
            print("The First item in Queue is", first_item)
        elif command in ["is_empty", "isEmpty"]:
            is_empty = queue.is_empty()
            if is_empty:
                print("YES")
            else:
                print("NO")
        elif command in ["is_full", "isFull"]:
            is_full = queue.is_full()
            if is_full:
                print("YES")
            else:
                print("NO")
        elif command in ["empty_queue", "empty"]:
            queue.empty_queue()
        print()


def main():
    while True:
        str_size = input("Enter a size for Queue:- ")
        if str_size == "":
            size = ""
            break
        elif str_size.isnumeric():
            size = int(str_size)
            break
        else:
            print("There is an error in the input!!!")

    system("cls")
    queue = Queue(size=size) if size == "" else Queue()  # type: ignore
    run_queue(queue)


main()
