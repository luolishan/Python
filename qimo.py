# 1、写一个函数：请用列表推导式实现求整数列表的立方
def triple(lst):
    return [x**3 for x in lst]

if __name__ == '__main__':
    print(triple([1,2,3]))

# 2、写一个函数：输入参数是一个整数列表，使用 reduce 函数和lambda表达式实现求和
def sum(lst):
    from functools import reduce
    return reduce(lambda x,y : x + y, lst)

if __name__=='__main__':
    print(sum([1,3,5,7]))

# 3、实现一个生成器函数：读取文件时每次只返回固定的长度，此长度可由用户调用时设置


# 4、写一个函数：输入参数是一个 list，判断该 list 中是否有空对象（用两种方法实现）
def has_null_value(lst):
    return list(filter(None,lst))==lst

def has_null_value(lst):
    return all(lst)

if __name__=='__main__':
    print(has_null_value([0,4, 'hello']))

# 5、使用递归实现10以内的斐波那契数列
def fib_number(n):
    if n < 2:
        return n
    return fib_number(n-2) + fib_number(n-1)

def fib(n):
    result = []
    for i in range(n):
        value = fib_number(i)
        if value > n:
            break
        result.append(value)
    return result

if __name__=='__main__':
    print(fib(10))

# 6、编写一个函数完成密码生成器的功能，输入参数有密码长度和密码组成的内容，密码组成的内容可以有
# 大写字母（A-Z）、小写字母（a-z）、数字（0-9）、特殊符号（~!@#$%^&*()），返回值为按照用户要求生成的随机密码
def passwd(len, lower=True, upper=True, number=True, special_char=True):
    import string, random
    lower_set = set(list(string.ascii_lowercase))
    upper_set = set(list(string.ascii_uppercase))
    number_set = set([x for x in range(10)])
    special_char_set = set(list('~!@#$%^&*()'))
    user_choice = set()
    if lower:
        user_choice = user_choice | lower_set
    if upper:
        user_choice = user_choice | upper_set
    if number:
        user_choice = user_choice | number_set
    if special_char:
        user_choice = user_choice | special_char_set
    passwd_lst = random.sample(user_choice, len)
    return ''.join(passwd_lst)

#if __name__=='__main__':
    #print(passwd(10))


# 7、使用偏应用函数实现一个函数求2和其他整数的积
from functools import partial
def mul(n):
    result = partial(lambda x, y: x * y, 2)
    return result(n)

if __name__=='__main__':
    print(mul(10))


# 8、实现一个装饰器：计时函数从执行开始到执行完毕所花费的时间
from functools import wraps
import time
def time_counter(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        f = func(*args, **kwargs)
        print('Consume time:', time.time() - start_time)
        return f
    return wrapper

