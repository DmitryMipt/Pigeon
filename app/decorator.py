import random
import time

def timer ( func):
    def wrapper(*args, **kwargs):
        srat_ts = time.time()
        result = func(*args, **kwargs)
        end_ts = time.time()
        print("Time '{}' is {} ms.".format(func.__name__, end_ts-srat_ts)*1000)
        return result
    return wrapper
#ЭТО чтобы добавить параметры from and to к декоратору  sleeper_
def sleeper (from_,to_):
    def sleeper_ (func):
        def wrapper (*args, **kwargs):
            time.sleep(random.randint(from_,to_))
            result = func(*args, **kwargs)
            return result
        return wrapper
    return sleeper_

@timer
@sleeper(1,3)
def foo(a,b):
    return a+b

if __name__=="__main__":
    print(foo(10,5))