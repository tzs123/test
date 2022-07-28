# _*_ coding:utf-8 _*_
import multiprocessing
import time
from threading import Thread


def aa(box_index):
    time.sleep(10)
    print('move box {} from a to b'.format(box_index))
    return

def test1():
    time1= time.time()
    for index in range (0,10):
        aa(index)
    time2= time.time()
    print('time consume {} s'.format(time2-time1))

def test2():
    time1=time.time()
    _processes = []
    for index in range(0,10):
        _process= multiprocessing.Process(target=aa,args=(index,))
        # _process = Thread(target=aa,args=(index,))
        _process.start()
        _processes.append(_process)
    for _process in _processes:
        _process.join()
    time2 = time.time()
    print('time consume {} s'.format(time2-time1))