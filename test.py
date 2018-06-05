# _*_ coding: utf-8 _*_
import functools, time
from enum import Enum,unique
import os, time

import os

# print('Process (%s) start...' % os.getpid())
sss = {}
# print(dir(sss))
print(sss.__dir__())
# Only works on Unix/Linux/Mac:
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

# def metric(fn):
#     @functools.wraps(fn)
#     def wrapper(*args, **kw):
#         start = time.time()
#         results = fn(*args, **kw)
#         end = time.time()
#         print('%s executed in %s ms' % (fn.__name__, (end - start) * 1000))
#         return results
#
#     return wrapper
#
#
# # 测试
# @metric
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y
#
#
# @metric
# def slow(x, y, z):
#     time.sleep(0.1234)
#     return x * y * z
#
#
# f = fast(11, 22)
# s = slow(11, 22, 33)
# print(fast.__name__)
# print(slow.__name__)
# if f != 33:
#     print('测试失败!')
# elif s != 7986:
#     print('测试失败!')
# @unique
# class Weekday(Enum):
#     Sun = 0 # Sun的value被设定为0
#     Mon = 1
#     Tue = 2
#     Wed = 3
#     Thu = 4
#     Fri = 5
#     Sat = 6
# print(Weekday(1))
# print(Weekday.Tue.value)

# tuple1 = (1,2,3)
# tuple2 = (1,[2,3])
#
# print('tuple1:',tuple1)
# print('tuple2:',tuple2)
#
# dict1 = dict(tuple1)
# # print(dict1[tuple1])
# print(dict1)
# attrs =dict(add=222)
# print(attrs)
# attrs['add'] = 'kkk'
# print(attrs)
# print(type(attrs))

# dict2 = {tuple2:'kkks'}
# print(dict1[tuple2])
