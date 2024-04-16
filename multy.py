import time
from threading import *

class Demo:
    def num(self):
        for i in range(1, 11):
            print(f'the number is {i}')
            time.sleep(1)
    
    def double(self):
        for i in range(1, 11):
            print(f'the double of the number {i} is {i * 2}')
            time.sleep(1)
    def square(self):
        for i in range(1, 11):
            print(f'The square of the number {i} is {i * i}')
            time.sleep(1)

# we want one iteration of every function to happen one by one
obj = Demo()
t1 = Thread(target=obj.num)
t2 = Thread(target=obj.double)
t3 = Thread(target=obj.square)

t1.start()
time.sleep(0.2)
t2.start()
time.sleep(0.2)
t3.start()

t1.join()
t2.join()
t3.join()

print('This is the main thread.')