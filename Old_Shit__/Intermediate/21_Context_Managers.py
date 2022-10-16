from contextlib import contextmanager

with open("/media/zero/Software/__/Python/Intermediate/notes.txt", "w") as fi:
    fi.write("some to dooo....")

# with class
# with lock 

#custom context managesr is created within classes

@contextmanager
def open_m(file):
    f = open(file,"w")
    try:
        yield f
    finally:
        f.close()

with open_m("/media/zero/Software/__/Python/Intermediate/notes.txt") as f:
    f.write("some things to do...")
    