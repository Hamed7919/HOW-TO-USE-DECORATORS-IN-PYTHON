from functools import wraps
from time import perf_counter, sleep


def get_time(func):
    """times any function"""
    @ wraps(func)
    def wrapper(*args,**kwargs):
        start_time = perf_counter()   

        result = func(*args, **kwargs)  # Call the decorated function

        end_time = perf_counter()
        totlal_time = round(end_time - start_time)

        print('time' , totlal_time, 'seconeds')
        return result

    return wrapper

@ get_time
def do_somtting(param = str ):
    """does something important"""

    sleep(1)
    return param 


one = do_somtting("sport")
print(one)

# why from functools import wraps:
# without @ wraps(func)
print(do_somtting.__name__)    
#  wrapper
print(do_somtting.__doc__)
# None
