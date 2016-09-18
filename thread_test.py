#!/usr/bin/python
# -*- coding: UTF-8 -*-


# import threading, time, random
#
# count = 0
# lock = threading.Lock()
#
#
# def doAdd():
#     global count, lock
#     lock.acquire()
#     for i in range(1000):
#         count = count + 1
#     lock.release()
#
#
# for i in range(5):
#     threading.Thread(target=doAdd, args=(), name='thread-' + str(i)).start()
# time.sleep(2)  # 確保線程都執行完畢
# print("Count={0}!".format(count))


import threading, time

lock = threading.Lock()
cmd = ""

def setCarCmd(s):
    global cmd, lock
    lock.acquire()
    cmd = s
    lock.release()

def controlCarThread():
    global cmd, lock
    while True:
        lock.acquire()
        tmp = cmd
        lock.release()
        print(tmp)
        time.sleep(1)
        if tmp == "END":
            break


if __name__ == '__main__':
    threading.Thread(target=controlCarThread, args=(), name='ControlCarThread').start()
    time.sleep(5)
    print("Job Done")
