import time

def display_time(func):
    def wrapper():
        t1=time.time()
        func()
        t2=time.time()
        print(t2-t1)
    return wrapper

def is_prime(num):
    if num<2:
        return False
    elif num==2:
        return True
    else:
        for i in range(2,num):
            if num % i ==0:
                return False
            return True
def prime_nums():
    t1=time.time()
    for i in range(2,10000):
        if is_prime(i):
            print(i)
    t2=time.time()
    print(t2-t1)

@display_time
def prime_nums2():
    # t1=time.time()
    for i in range(2,10000):
        if is_prime(i):
            print(i)
    # t2=time.time()
    # print(t2-t1)

# prime_nums()

prime_nums2()