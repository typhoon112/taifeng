import ctypes
import json

class Point(ctypes.Structure):
    _fields_ = [
        ("lat", ctypes.c_double),
        ("lng", ctypes.c_double),
        ("pressure", ctypes.c_double),
        ("power", ctypes.c_double),
        ("movespeed", ctypes.c_double)
    ]
Cdtw = ctypes.CDLL("./dtwdis.dll")
Cdtw.dtwdis.restype = ctypes.c_double

with open("zjwater2010_2020.json") as f:
    d = json.load(f)
cf = [1.3, 1.3, 1.1, 0.8, 0.7]

with open("res.csv", "w") as f:
    f.write("b,n,c,m,dis\n")
    for kb, vb in d.items():
        b = [Point(*x) for x in vb]
        for kc, vc in d.items():
            c = [Point(*x) for x in vc]
            dis = Cdtw.dtwdis(len(b), (Point * len(b))(*b), len(c), (Point * len(c))(*c), (ctypes.c_double * 5)(*cf))
            f.write("{},{},{},{},{}\n".format(kb, len(vb), kc, len(vc), dis))