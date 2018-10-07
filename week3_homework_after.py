# 1、编写一个函数完成密码生成器的功能，输入参数有密码长度和密码组成的内容，密码组成的内容可以有大写字母（A-Z）、小写字母（a-z）、数字（0-9）、特殊符号（~!@#$%^&*()），返回值为按照用户要求生成的随机密码
def make_password(p_len, lower_case=True, upper_case=True, number=True, special_char=True):
    import string, random
    lower_case_set = set(list(string.ascii_lowercase))
    upper_case_set = set(list(string.ascii_uppercase))
    number_set = set([x for x in range(10)])
    special_char_set = set(list('~!@#$%^&*()'))
    user_choice = set()
    if lower_case:
        user_choice = user_choice | lower_case_set
    if upper_case:
        user_choice = user_choice | upper_case_set
    if number:
        user_choice = user_choice | number_set
    if special_char:
        user_choice = user_choice | special_char_set
    passwd_lst = random.sample(user_choice, p_len)
    return ''.join(passwd_lst)

#2、编写一个函数：输入参数为一个整数列表和一个整数，判断该整数是否存在于该列表中。如果存在，是在列表的左半边还是右半边
def exist(lst, number):
    try:
        idx = lst.index(number)
        if idx <= len(lst) // 2:
            return 'left'
        else:
            return 'right'
    except ValueError:
        return False

#3、编写一个函数：过滤1 - 100中的素数
def prime(x):
    for num in range(1, x + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)
prime(100)

# 4、编写一个模块，要求里面有变量x和y，两数相加add(x, y)，两数相减sub(x, y)，两数相乘mul(x, y)，两数相除div(x, y)这四个方法的实现
def add(m, n):
    return m + n

def sub(m, n):
    return m - n

def mul(m, n):
    return m * n

def div(m, n):
    try:
        return m / n
    except ZeroDivisionError:
        print('除数不能为0')

# 5、编写一个函数：输入参数是一个整数列表，请找出该列表中最小的整数并返回
def minnumber(lst):
    from functools import reduce
    return reduce(lambda x, y: x if x < y else y, lst)