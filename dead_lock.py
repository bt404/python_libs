# -*- coding: utf-8 -*-
from threading import Thread, Lock, Condition

#
# 使用 Lock 来实现同时申请两个锁，会造成死锁现象。
#
#lock1 = Lock()
#lock2 = Lock()
#
#class One(Thread):
#    def run(self):
#        if(lock1.acquire()):
#            print self.getName(), "get lock1"
#            if(lock2.acquire()):
#                print self.getName(), "get lock2"
#            print self.getName(), "realease lock2"
#            lock2.release()
#        print self.getName(), "realease lock1"
#        lock1.release()
#
#
#class Two(Thread):
#    def run(self):
#        if(lock2.acquire()):
#            print self.getName(), "get lock2"
#            if(lock1.acquire()):
#                print self.getName(), "get lock1"
#            print self.getName(), "realease lock1"
#            lock1.release()
#        print self.getName(), "realease lock2"
#        lock2.release()
#
#pool = []
#for i in xrange(5):
#    pool.append(One())
#for i in xrange(5):
#    pool.append(Two())
#for i in xrange(10):
#    pool[i].start()


# 
# 改用 Condition 变量，配合 wait 和 notify 方法可以实现申请两个锁但不发生死锁。
#
cond1 = Condition()
cond2 = Condition()

class One(Thread):
    def run(self):
        if(cond1.acquire()):
            print self.getName()+"get cond1"
            # 非阻塞上锁
            while(not cond2.acquire(False)):
                # cond2 不可用时释放 cond1 并等待唤醒重新上锁 cond1，继而上锁 cond2。
                # 指定 timeout 是因为，当最后仅剩两个调用 cond1.wait() 方法的线程时，二者都阻塞在 wait
                # 上，但是没有其它线程再调用 notify，二者永远阻塞。设置 timeout，当过期时，二者会自动唤醒
                cond1.wait(2000)
            print self.getName()+"get cond2"
            print self.getName()+"realease cond2"
            cond2.notify()
            cond2.release()
        print self.getName()+"realease cond1"
        cond1.notify()
        cond1.release()


class Two(Thread):
    def run(self):
        if(cond2.acquire()):
            print self.getName()+"get cond2"
            while(not cond1.acquire(False)):
                cond2.wait(2000)
            print self.getName()+"get cond1"
            print self.getName()+"realease cond1"
            cond1.notify()
            cond1.release()
        print self.getName()+"realease cond2"
        cond2.notify()
        cond2.release()

pool = []
for i in xrange(5):
    pool.append(One())
for i in xrange(5):
    pool.append(Two())
for i in xrange(10):
    pool[i].start()
