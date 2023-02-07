#Q1. Convert the list [1, 2, 3, 4, 5] to [2, 4, 6, 8, 10] with list comprehension.

#1st way

list = [2*i for i in [1,2,3,4,5]]
print(list)

#2nd way

list = [2*i for i in range(1,6)]
print(list)



#Q2. Build a retry decorator with retry time and retry interval to run a function 3 time with interval of 3 sec.

import time

def retry(retry_time=3, retry_interval=3):

    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(retry_time):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    if i < retry_time - 1:
                        time.sleep(retry_interval)
                    else:
                        raise e
        return wrapper
    return decorator

@retry(retry_time=3, retry_interval=3)
def my_function():
    #function
    pass



#Q3. Build a counter generator
def counter_generator():
    count = 0
    while True:
        count += 1
        yield count
counter = counter_generator()
for i in range(10):
    print(next(counter))
