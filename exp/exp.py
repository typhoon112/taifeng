import ctypes
import json
import numpy as np
import os
import struct

def tanh(x, k=np.e):
    lnk = np.log(k)
    A = np.exp(x * lnk)
    B = np.exp(-x * lnk)
    return (A - B) / (A + B)

class Point(ctypes.Structure):
    _fields_ = [
        ("lon", ctypes.c_double),
        ("lat", ctypes.c_double),
        ("pressure", ctypes.c_double),
        ("power", ctypes.c_double),
        ("movespeed", ctypes.c_double)
    ]
os.add_dll_directory("C:\\MinGW\\bin")
Cdtw = ctypes.CDLL("./dtwdis.dll")
Cdtw.dtwdis.restype = ctypes.c_double

with open("zjwater2018_2021.json") as f:
    d = json.load(f)
sp = 1.005

def exp1():
    res = []
    cf = [0.26, 0.26, 0.22, 0.14, 0.12]
    # cf = [0.5, 0.5, 0, 0, 0]
    b = [Point(*x) for x in d["202018"]]
    for k, c in d.items():
        c = [Point(*x) for x in c]
        dis = Cdtw.dtwdis(len(b), (Point * len(b))(*b), len(c), (Point * len(c))(*c), (ctypes.c_double * 5)(*cf), 0)
        res.append((k, dis))
    for i, x in enumerate(sorted(res, key=lambda k: k[1])):
        if x[0] in ("202018", "202022", "202007", "202004", "202008", "201909"):
            print(x[0], x[1], 1 - tanh(x[1], sp))

def exp2():
    res = []
    cf = [0.16, 0.16, 0.26, 0.28, 0.14]
    b = [Point(*x) for x in d["201909"]]
    for k, c in d.items():
        c = [Point(*x) for x in c]
        dis = Cdtw.dtwdis(len(b), (Point * len(b))(*b), len(c), (Point * len(c))(*c), (ctypes.c_double * 5)(*cf), 0)
        res.append((k, dis))
    for i, x in enumerate(sorted(res, key=lambda k: k[1])):
        if i > 3:
            break
        print(x[0], x[1], 1 - tanh(x[1], sp))

def exp3():
    res = []
    cf = [0.5, 0.5, 0, 0, 0]
    b = [Point(*x) for x in d["202106"]]
    for k, c in d.items():
        c = [Point(*x) for x in c]
        cutoff = ctypes.c_int(1)
        dis = Cdtw.dtwdis(len(b), (Point * len(b))(*b), len(c), (Point * len(c))(*c), (ctypes.c_double * 5)(*cf), ctypes.pointer(cutoff))
        res.append((k, dis, struct.unpack("l", cutoff)[0]))
    for i, x in enumerate(sorted(res, key=lambda k: k[1])):
        if i > 5:
            break
        print(x[0], x[1], 1 - tanh(x[1], sp), x[2])

exp3()