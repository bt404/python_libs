from threading import Lock

class Singleton(object):
    lock = Lock()
    
    def __new__(cls, *args, **kw):
        if not hasattr(cls, "_instance"):
            if(lock.acquire()):
                if not hasattr(cls, "_instance"):
                    orig = super(Singleton, cls)
                    cls._instance = orig.__new__(cls, *args, **kw)
            lock.release()
        return cls._instance
