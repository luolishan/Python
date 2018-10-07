# 1.编写一个Animal类，属性有name，方法有call()；现有Dog类和Cat类继承Animal类，请根据实际情况重写call() （比如，狗叫可以打印汪汪，猫叫可以打印喵喵）
class Animal():
    def __init__(self, name):
        self.name = name
        print("Animal name: %s" % (self.name))

    def call():
        print("")

class Dog(Animal):
    def call():
        print("汪汪")

class Cat(Animal):
    def call():
        print("喵喵")

if __name__ == '__main__':
    dog = Dog('dog')
    Dog.call()
    cat = Cat('cat')
    Cat.call()

#2、使用递归实现10以内的斐波那契数列
def fib(n):
    if n <= 1:
        return n
    else:
        a = int(fib(n - 1) + fib(n - 2))
        if a < 10:
            return a

for i in range(10):
    print(fib(i))

#3、使用列表推导获取100以内的奇数
y=[x for x in range(1,101,1) if x%2==1]

#4、使用异常处理结构实现 add(x,y) / sub(x,y) / mul(x,y) / div(x,y)
class count:
	@staticmethod
	def add(x,y):
		try:
			return x+y
		except Exception as e:
			print(e)
			print("有异常将返回None")
			return None
	@staticmethod
	def sub(x,y):
		try:
			return x-y
		except Exception as e:
			print(e)
			print("有异常将返回None")
			return None
	@staticmethod
	def mul(x,y):
		try:
			return x*y
		except Exception as e:
			print(e)
			print("有异常将返回None")
			return None
	@staticmethod
	def div(x,y):
		try:
			return x/y
		except Exception as e:
			print(e)
			print("有异常将返回None")
			return None

#5、将Python之禅（import this）写入文件，并统计有多少单词及其出现的次数，将统计结果序列化至文件中保存
