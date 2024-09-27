from multiprocessing import Process, Value, Array, Lock, Queue , Pool
import os 
import time

# def add_100(num,lock):
#     for i in range(100):
#         time.sleep(0.05)
#         with lock: 
#             num.value += 1
            
   
# if __name__ == "__main__":
#     lock = Lock()    
#     s_value = Value("i",0)
#     print("Number at beginning is", s_value.value)

#     p1 = Process(target= add_100, args=(s_value,lock))
#     p2 = Process(target= add_100, args=(s_value,lock))

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

#     print("Number st end is", s_value.value) 

###################################################
# def add_100(arr,lock):
#     for i in range(100):
#         time.sleep(0.05)
#         for i in range(len(arr)):
            
#             with lock: 
#                 arr[i]+= 1
            
   
# if __name__ == "__main__":
#     lock = Lock()    
#     s_value = Array("d",range(0,11))
#     print("Array at beginning is", s_value[:])

#     p1 = Process(target= add_100, args=(s_value,lock))
#     p2 = Process(target= add_100, args=(s_value,lock))

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

#     print("Array at end is", s_value[:]) 
###################################################

def square(n,q,lock):
    for i in n:
        # time.sleep(0.5)
        with lock:
            q.put(i*i)

def m_negitave(n,q,lock):
    for i in n:
        # time.sleep(0.5)
        with lock:
            q.put(-abs(i))
   
if __name__ == "__main__":
    print("Start of Program...")
    q = Queue()
    lock =Lock()
    n = range(1,6)

    p1= Process(target=square, args=(n,q,lock))
    p2 =Process(target=m_negitave, args=(n,q,lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    
    while not q.empty():
        print(q.get())

    print("End of Program...")
    
###################################################
# def cube(n):
#     time.sleep(0.5)
#     return n**n

# if __name__ == "__main__":
#     pool = Pool()
#     lock =Lock()
#     number = range(10)

#     # map, apply, join, close
#     result = pool.map(cube,number)
#     # pool.apply(cube, number[0])

#     pool.close()
#     pool.join()

#     print(result)



 