from multiprocessing import Process, cpu_count

from responses import target
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():
    x = time.time()
    print(cpu_count())

    a = Process(target= counter,args=(125000000,))
    b = Process(target= counter,args=(125000000,))
    c = Process(target= counter,args=(125000000,))
    d = Process(target= counter,args=(125000000,))
    e = Process(target= counter,args=(125000000,))
    f = Process(target= counter,args=(125000000,))
    g = Process(target= counter,args=(125000000,))
    h = Process(target= counter,args=(125000000,))
    
    a.start()
    b.start()
    c.start()
    d.start()
    e.start()
    f.start()
    g.start()
    h.start()
    
    a.join()
    b.join()
    c.join()
    d.join()    
    e.join()
    f.join()
    g.join()
    h.join()

    u = time.time()
    print(f"finished in : {(u-x):.2f} seconds.")

if __name__ == "__main__":
    main()
