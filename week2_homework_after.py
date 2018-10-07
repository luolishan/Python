#1.编写一个函数输出乘法口诀表，执行结果如图所示（提示：print 默认输出后会换行，可以通过 print 参数控制是否换行）
for i in range(1,10):
    for j in range(1,i+1):
        print('{}*{}={}\t'.format(j,i,i*j),end='')
    print()


#2.编写一个函数遍历并打印 1 到 100，如果数字能被3整除，显示 Fizz；如果数字能被 5 整除，显示 Buzz；如果能同时被 3 和 5 整除，就显示 FizzBuzz
def traverse(a,b):
    for x in range(a,b):
        if x%3==0 and x%5 == 0:
            print('FizzBuzz')
        elif x%3 == 0:
            print('Fizz')
        elif x%5 == 0:
            print('Bizz')
        else:
            print(x)

traverse(1,101)

#3.编写一个函数，输出 100 以内的斐波那契数列
i, j = 0, 1
while i < 100:
    print(i)
    i, j = j, i+j