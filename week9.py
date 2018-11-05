##1、使用 ThreadPoolExecutor 和多线程搭配，要求：a). 用一个线程监视当然已完成的进度；b). 用 ThreadPoolExecutor 创建3个线程执行 fib 函数；c). 用另外一个线程作为生产者（提示：使用submit方法提交新的任务）
##输出如下：
##fib(26) = 121393
##fib(28) = 317811
##fib(27) = 196418
##…
import time
import asyncio
from concurrent.futures import ThreadPoolExecutor
from queue import Queue
import threading

def fib(n):
    if n <= 2:
        return 1
    return fib(n - 2) + fib(n - 1)

def produce(queue):
    for num in range(10):
        queue.put(num)
        print(f"produce put{num} to queue")

def jianshi(queue):
    while queue.qsize():
        r = queue.qsize()
        print(f'queue.qsize={r}')
        time.sleep(1)

def consumer(queue):
    with ThreadPoolExecutor(max_workers=3) as executor:
        while queue.qsize() > 0:
            r = queue.get()
            z = executor.submit(fib, r)
            z1 = z.result()
            print(f'fib({r})={z1}')

if __name__ == '__main__':
    queue = Queue()
    t1 = threading.Thread(target=produce, args=(queue,))
    t1.start()
    t2 = threading.Thread(target=jianshi, args=(queue,))
    t2.start()
    t3 = threading.Thread(target=consumer, args=(queue,))
    t3.start()

##2.写一个异步生成器，要求：a). 用到 async for，b). 抓取10个”http://httpbin.org/get?a=X"这样的url (X为0-9这十个数字)，并打印a的值
import asyncio
async def a():
    for i in range(10):
        yield i

async def a1():
    async for v in a():
        print(v)
    return [v * 2 async for v in a()]


loop = asyncio.get_event_loop()
try:
    result = loop.run_until_complete(a1())
    print(f'Result is {result}')
finally:
    loop.close()
