from multiprocessing import Process
from threading import Thread
import os 
import time

# def s():
#     for i in range(100):
#         i*i
#         time.sleep(0.1)
# proc = []
# num_p = os.cpu_count()

# # create processes

# for i in range(num_p):
#     p = Process(target=s )
#     proc.append(p)

# # start
# for p in proc:
#     p.start()

# #join
# for j in proc:
#     j.join()

# print("End main")

def s():
    for i in range(100):
        i*i
        time.sleep(0.1)
threads = []
num_t = 10

# create processes

for i in range(num_t):
    t = Thread(target=s )
    threads.append(t)

# start
for t in threads:
    t.start()

#join
for j in threads:
    j.join()

print("End main")
