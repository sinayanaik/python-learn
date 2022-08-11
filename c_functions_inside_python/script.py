from ctypes import *

shared_c_lib = CDLL("./math.so")

print(shared_c_lib)

print(shared_c_lib.add(1, 2))
print(shared_c_lib.square(2))
print(shared_c_lib.factorial(5))