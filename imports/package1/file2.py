# import file1
# from file1 import fun1


# file1.fun2()
# print(file1.a)
# fun1()


'''Comment Above before uncommenting and running below piece'''
#### We should not do wildcard import (*) as it imports unnecessary things too
from file1 import *
fun1()
fun2()
print("Print from file 2: ", a, b)