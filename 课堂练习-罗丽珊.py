Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def user():
    name=input('your name:')
    age=int(input('your age:'))
    year=2018+100-age
    r=f'{name}在{year}年为100岁'
    print(r)
    return year

>>> user()
your name:LUO
your age:17
LUO在2101年为100岁
2101
>>> def get():
    num=int(input("请输入一个整数："))
    if num % 2 == 0:
        print("你输入的是偶数")
    else:
        print("你输入的是奇数")

        
>>> get()
请输入一个整数：50
你输入的是偶数
>>> get()
请输入一个整数：35
你输入的是奇数
>>> def three1(lst):
    if lst==[]:
        print("列表中没有元素")	
    for a in lst:	
        if not bool(a):	
            print("有空对象")	
            return True
        else:	
            pass
    print("没有空对象")		
    return False

>>> three1([0,1,2,3])
有空对象
True
>>> def three2(lst):
    y=lambda x: bool(x)
    for x in lst:  
        b=y(x)
        if not b:
            print("有空对象")
            return True
        else:
            pass
    print("没有空对象")
    return False

>>> three2([1,2,3])
没有空对象
False
>>> def three3(lst1):
    all(lst1) == True
    if  all(lst1):
        print("没有空对象")
        return False
    else:
        print("有空对象")
        return True

>>> three3([0,1,2,3])
有空对象
True
>>> def double(lst):
    lst1=[x*x for x in lst]
    return lst1

>>> double([2,4,3])
[4, 16, 9]
>>> def double1(lst):
    lst1=map(lambda x:x*x,lst)
    return list(lst1)

>>> double1([2,4,3])
[4, 16, 9]
>>> from functools import reduce
>>> reduce(lambda x,y:x+y,[1,2,3])
6
>>> def cube(lst):
    return  [x*x*x for x in lst]

>>> cube([1,2,3])
[1, 8, 27]
>>> def new(lst1,lst2):
    lst3=list(set(lst1).intersection(set(lst2)))
    return lst3

>>> new(['a','b','l'],['a','b','c'])
['a', 'b']
>>> def Max(a,b,c):
    return max(a,b,c)

>>> Max(2,3,5)
5
>>> def Max1(a,b,c):
    if a>b:
        max=a
    else:
        max=b
    if c>max:
        max=c
    return max

>>> Max1(5,7,6)
7
>>> 
