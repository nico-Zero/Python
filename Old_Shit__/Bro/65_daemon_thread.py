import threading
import time


def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("\nlogged in for: ",count,"seconds.",end="")

x = threading.Thread(target = timer,args=(),daemon=True)
x.setDaemon(True)
x.start()
print(x.isDaemon())

answer = input("Do you wish to exit? ")

