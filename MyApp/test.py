
#goto MyApp folder and create test.py and run

from mypackage import greet
greet.SayHello("CDAC")


from mypackage import functions
print(functions.power(3,2))

from mypackage.functions import sum
print(sum(10,20))


from mypackage.functions import average
print(average(10,20))