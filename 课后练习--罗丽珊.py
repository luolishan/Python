Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def exist(lst,integer):
    flag=0
    b=-1
    d=[]
    for a in lst:
        if a==integer:
            print("该整数存在于该列表中")
            flag=1
            break
    if flag==0:
        print("该整数不存在于该列表中")
    else:
        try:
            while True:
                b=lst.index(integer,b+1)
                d.append(b)
        except:
                pass
        finally:
            for a in d:
                if (len(lst)-1)/2>a:
                    print("左半边有一个")
                elif (len(lst)-1)/2<a:
                    print("右半边有一个")
                else:
                    print("正好在中间有一个")

                    
>>> exist([1,2,3],1)
该整数存在于该列表中
左半边有一个
>>> def prime(x):
    for num in range(1,x + 1):
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
            else:
                print(num)

                
>>> print(100)
100
>>> prime(100)
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
>>> def minnumber(lst):
    lst1=min(lst)
    return lst1

>>> minnumber([1,2,4,6])
1
>>> 
