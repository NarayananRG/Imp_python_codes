"""
import pandas as pd
import os
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

os.chdir("C:/Users/laksrgan/OneDrive - Keysight Technologies/Downloads/archive (2)")

train = pd.read_csv("train_and_test2.csv")


def number(*args, **kwargs):
    print(args)
    print(kwargs)


lst = 2
even_odd = lambda lst: lst % 2 == 0
print(even_odd(lst))

eo = lambda lst: 'Even' if lst % 2 == 0 else 'Odd'
print(eo(lst))

a=[1,2,3,4,5,6]


p=filter(lambda a : a%2==0,a)
print(list(p))

val=[i*i for i in a if i%2==0]
print(val)

dict={'a':1,'b':2,'c':3}

for i in dict:
    print(i,dict[i])


x=iter(a)
next(x)
for i in x:
    print(i)

class car:
    def __init__(self,window,door,engtype):
        self.win=window
        self.doors=door
        self.enginetype=engtype
    def self_drive(self,wheel):
        self.wheels=wheel
        print('This is a self driving {} wheel {} car'.format(self.wheels,self.enginetype))

audi=car(2,4,'petrol')

print(audi.enginetype)
audi.self_drive(4)


try:
    a=int(input("enter a number "))
    b = int(input("enter a number "))
    c=a/b
except ZeroDivisionError:
    print("Please provide a number greater than 0")
except Exception as ex:
    print(ex)
else:
    print(c)
finally:
    print("Finally the operation is completed.offff...")


class error(Exception):
    pass
class age_exception(error):
    pass
try:
    a = int(input("enter a number "))
    if a<=30 & a>=20 :
        print('valid age')
    else:
        raise age_exception
except age_exception:
    print('age not in range of 20 to 30')

"""
class car():
    def __init__(self,window,enginetype):
        self._windows=window
        self._engtype=enginetype

audi=car(4,'petrol')
print(audi._engtype)
print(dir(audi))

class truck(car):
    def __init__(self,_windows,_engtype,horsepower):
        super().__init__(_windows,_engtype)
        self.horsepow=horsepower

swaraj=truck(4,'diesel',4000)
print(swaraj._engtype)
audi._windows=6
print(swaraj._windows)
print(dir(swaraj))