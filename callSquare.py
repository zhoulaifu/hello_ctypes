#!/usr/bin/env python2
import ctypes
from ctypes import cdll

lib=cdll.LoadLibrary("./square.so")
lib.square.restype = ctypes.c_double
lib.square.argstype = [ctypes.c_double]

print "square 3.1 =", lib.square(ctypes.c_double(3.3))
