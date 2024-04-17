import time

epc =time.time()

print(epc)  # time passed from 1970

localtime = time.localtime(epc)
print(localtime)  # time struct output

print(localtime.tm_year)  # year

print(time.ctime(epc))  # current time
