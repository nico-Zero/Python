import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("You ate breakfast.")


def drink_coffee():
    time.sleep(4)
    print("You drank our coffee.")


def Study():
    time.sleep(5)
    print("You did your study.")

eat = threading.Thread(target=eat_breakfast,args=())
drink = threading.Thread(target=drink_coffee,args=())
study = threading.Thread(target=Study,args=())
eat.start()
drink.start()
study.start()

eat.join()
drink.join()
study.join()

# eat_breakfast()
# drink_coffee()
# Study()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())
