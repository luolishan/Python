#1.使用偏应用函数实现一个函数求2和其他整数的积
from functools import partial
def mul(x,y):
	return x*y

a=partial(mul,2)

#2.将柯里化的例子用偏应用函数 partial 实现
def add(x,y,z):
    return x+y+z

from functools import partial
addA=partial(add,1,2,3)
addA()

#3.实现一个装饰器：计时函数从执行开始到执行完毕所花费的时间
def one(func):
	def Wrapper(*args,**akg):
		start=time.time()
		x=func(*args,**akg)
		end=time.time()
		print(end-start)
		return x
	return Wrapper

@one
def add1(x,y):
	return x+y

#4.实现一个装饰器：检查除法函数传入的参数，避免除法函数抛 ZeroDivisionError 异常
def two(func):
	def Wrapper(*args,**akg):
		try:
			x=func(*args,**akg)
		except Exception as e:
			print(e)
			return None
		return x
	return Wrapper

@two
def chu(*args,**akg):
	sum1=args[0]**2
	print(args)
	for i in args:
		sum1=sum1/i
	return sum1

#5.实现一个装饰器：使被装饰的函数在每次执行完毕后打印’Done’和当前时间（精确到秒）
def three(func):
	def Wrapper(*args,**akg):
		start=time.time()
		x=func(*args,**akg)
		end=time.time()
		thiss=end-start
		print(f'Done {thiss}')
		return x
	return Wrapper

@three
def chu(*args,**akg):
	sum1=args[0]**2
	print(args)
	for i in args:
		sum1=sum1/i
	return sum1



