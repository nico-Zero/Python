from threading import Thread, Lock, current_thread
from queue import Queue
import time
from webob import second

data = 0
def increase(lock):
    global data

    with lock:
        local_c = data

        #processing
        local_c += 1
        time.sleep(3)
        data = local_c

if __name__ == "__main__":
    lock = Lock()
    print("start value", data)

    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("End value", data)

# ###################################

# data = 0
# def increase(lock):
#     global data

#     with lock:
#         local_c = data

#         #processing
#         local_c += 1
#         time.sleep(3)
#         data = local_c

# if __name__ == "__main__":
#     q = Queue()
#     q.put(1)
#     q.put(2)
#     q.put(3)

#     # 3 2 1 -->
#     first = q.get()
#     print(first)
#     second = q.get()
#     print(second)
#     third = q.get()
#     print(third)

#     q.task_done()

#     q.join()

#     print("End main")
    
###################################

# print("Start main")

# def worker(q,lock):
    
#     while True:
#         with lock:
#             value = q.get()
#             # processing...
#             time.sleep(0.4)
#             print(f"in {current_thread().name} got {value}")
#             q.task_done()


# if __name__ == "__main__":
#     lock = Lock()
#     q = Queue()

#     num_t = 10
#     for i in range(num_t):
#         thread = Thread(target=worker , args=(q,lock))
#         thread.daemon = True
#         thread.start()

#     for i in range(1, 21):
#         q.put(i * i)

#     q.join()

#     print("End main")
 