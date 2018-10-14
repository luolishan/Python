#1.实现一个装饰器：检查被装饰的函数所传入的参数，如果是字符串类型，且含有小写字母，则将小写字母全部转为大写字母
def four(func):
	def Wrapper(*args,**akg):
		print(type(args))
		new_args=[]
		for i in range(len(args)):
			print(type(args[i]))
			if type(args[i])==type("aa"):
			    if not args[i].isupper():
				    print(args[i])
				    new_args.append(args[i].upper())
			    else:
				    print(args[i])
				    new_args.append(args[i])
		print(new_args)
		x=func(*new_args,**akg)
		return x
	return Wrapper

@four
def add2(x,y):
	return x+y

add2("asdsad","ASDSADSA")

#2.实现一个生成器函数：读取文件时每次只返回固定的长度，此长度可由用户调用时设置
def t1(path):
	def t2(zijie):
		path1=path
		with open(path,'r') as f:
			while True:
				try:
					t=f.read(zijie)
				except Exception as e:
					print(e)
					break
				yield t
		print("结束了!")
	return t2

path="C:/new1.txt"
z=t1(path)
x=z(2)
x.send(None)

#3.实现一个生成器函数：模拟数据库中的主键自增，即生成的值为主键自增的结果
def t3():
	sumkey=0
	while True:
		sumkey=sumkey+1
		yield sumkey

x=t3()
next(x)

#4.实现一个生成器表达式：生成 50 以内的偶数，并用 for 循环打印出每个值
x=(i for i in range(1,51,1) if not i%2)
for i in x:
	print(i)

#5.实现一个生成器函数：读取操作系统 C 盘中的所有文件的名字
import os
from os.path import join,getsize
def x(path):
	for root,dirs,files in os.walk(path):
		for name in files:
			fname=join(root,name)
			yield fname


z=x("c:\\")
next(z)