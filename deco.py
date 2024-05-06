import time
 
 
def timer(func):
 
    def wrapper(sleep_time):
        t1 = time.time()
        func(sleep_time)
        t2 = time.time()
        cost_time = t2 - t1 
        print(f"花费时间：{cost_time}秒")
 
    return wrapper
 
 
@timer  # 这个装饰器就是函数
def function(sleep_time):
    time.sleep(sleep_time)

function(3)