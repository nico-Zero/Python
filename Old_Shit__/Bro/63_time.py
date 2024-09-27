import time

# # print(time.ctime(999999999))
# # print(time.time())
# # print(time.ctime())
# time_ob = time.localtime()
# # print(time_ob)
# time_utc = time.gmtime()
# print(time_utc)
# localtime_ob = time.strftime("%B %d %Y %H:%M:%S",time_ob)
# localtime_utc = time.strftime("%B %d %Y %H:%M:%S",time_utc)

# print(localtime_ob)
# print(localtime_utc)

# time_s = "20 April, 2020" 
# time_obx = time.strptime(time_s,"%d %B, %Y")
# print(time_obx)

time_tuple = (2200,4,23,4,20,9,5,32,9)
time_string = time.asctime(time_tuple)
print(time_string)

time_tuple2 = (2020,4,0,4,0,9,0,0,0)
time_string2 = time.mktime(time_tuple2)
print(time_string2)

