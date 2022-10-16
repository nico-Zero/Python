import os
# try:
#     path = "/media/zero/Software/__/Python/Bro/text.txt"
#     os.remove(path)
# except FileNotFoundError:
#     print("File Not Found... ):")

# this doesn't delete wmpty folders

try:
    path = "/media/zero/Software/__/Python/Bro/delete"
    # os.remove(path) # so use this instad
    os.rmdir(path)
except FileNotFoundError:
    print("File Not Found... ):")
else:
    print(f"{path} was deleted...(:")
