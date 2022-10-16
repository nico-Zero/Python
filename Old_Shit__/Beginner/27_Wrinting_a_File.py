def append_line():
    employee_file = open("/media/nonesuch/Software/__/Python/employees.txt", "a")

    employee_file.write("\nJhon - Human Resources")
    
    employee_file.close()


def overwrite_line():
    employee_file = open("/media/nonesuch/Software/__/Python/employees.txt", "w")

    employee_file.write("\nJhon - Human Resources")

    employee_file.close()


# append_line()
# overwrite_line()