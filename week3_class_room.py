#1、写一个函数：获取用户输入的名字（name）和年龄（age），计算一下该用户到哪一年（返回值）为100岁，并打印结果”{用户名字}在XXXX年为100岁”
def user():
    name=input('your name:')
    age=int(input('your age:'))
    year=2018+100-age
    r=f'{name}在{year}年为100岁'
    print(r)
    return year

user()


#2、写一个函数：获取用户输入的整数，如果它是奇数则打印”您输入的是奇数”，如果是偶数则打印”您输入的是偶数”
def get():
    num=int(input("请输入一个整数："))
    if num % 2 == 0:
        print("你输入的是偶数")
    else:
        print("你输入的是奇数")

get()

#3、写一个函数：输入参数是一个list，判断该list中是否有空对象（至少用三种方法实现）
def three1(lst):
    if lst == []:
        print("列表中没有元素")
    for a in lst:
        if not bool(a):
            print("有空对象")
            return True
        else:
            pass
    print("没有空对象")
    return False

three1([0, 1, 2, 3])
three1([1, 2, 3])

def three2(lst):
    y = lambda x: bool(x)
    for x in lst:
        b = y(x)
        if not b:
            print("有空对象")
            return True
        else:
            pass
    print("没有空对象")
    return False

three2([0, 1, 2, 3])
three2([1, 2, 3])

def three3(lst1):
    all(lst1) == True
    if all(lst1):
        print("没有空对象")
        return False
    else:
        print("有空对象")
        return True

three3([0, 1, 2, 3])
three3([1, 2, 3])

#4、写一个函数：输入参数是一个整数列表，把该列表中每个整数都平方后返回新的列表（至少用两种方法实现）

def double(lst):
    lst1=[x*x for x in lst]
    return lst1

double([2,4,3])

def double1(lst):
    lst1=map(lambda x:x*x,lst)
    return list(lst1)

double1([2,4,3])

#5、写一个函数：输入参数是一个整数列表，使用 reduce 函数实现求和后返回结果
from functools import reduce
reduce(lambda x,y:x+y,[1,2,3])


#6、写一个函数：请用列表推导式实现开方
def cube(lst):
    return  [x*x*x for x in lst]

cube([1,2,3])

#7、写一个函数：输入参数是两个 list，请返回它们的共同元素所组成的新列表
def new(lst1,lst2):
    lst3=list(set(lst1).intersection(set(lst2)))
    return lst3

lst1=['a','b','l']
lst2=['a','b','c']
new(['a','b','l'],['a','b','c'])

#8、写一个函数：找出三个整数中的最大数（至少用两种方法实现）
def Max(a,b,c):
    return max(a,b,c)

Max(2,3,5)

def Max1(a,b,c):
    if a>b:
        max=a
    else:
        max=b
    if c>max:
        max=c
    return max

Max1(5,7,6)