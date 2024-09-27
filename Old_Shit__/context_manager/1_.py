from contextlib import contextmanager

# with open("/media/zero/Software/__/Python/Bro/alex.txt","w") as file :
#     file.write("Some Todo...")

# class ManagedFile:
#     def __init__(self, filename):
#         self.filename = filename

#     def __enter__(self):
#         print("Enter")
#         self.file = open(self.filename,"w")
#         return self.file

#     def __exit__(self,exc_type,exc_value,exc_teaceback):
#         if self.file:
#             self.file.close()
#         if exc_type is not None:
#             print("exception has occered.")
#         print("Exit.")
#         return True
    
# with ManagedFile('/media/zero/Software/__/Python/Bro/alex.txt') as file:
#     print("open")
#     file.write("Software mark_2")
#     file.some()

# print('continuing')

@contextmanager
def open_manage_file(filename : str):
    f = open(filename,"r+")
    try:
        yield f
    finally:
        f.close()

with open_manage_file('/media/zero/Software/__/Python/Bro/alex.txt') as f:
    print(f.read())