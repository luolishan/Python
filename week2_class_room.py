#1.将字符串’hello, world’中的 l 替换为 *
'hello,world'.replace('l','*')

#2.现有字符串 ’Good’ ，期望结果 ‘good!good!good!’，至少用两种方法实现
('Good'+'!').lower()*3
###################################
('Good'+'!').replace('G','g')*3
###################################
string = 'Good'.lower()
lst = [string] * 3
'!'.join(lst) + '!'

#3.将字符串 ’Fh1qoWe92QbvC’ 中的大写替换为小写，小写替换为大写（提示：Python 字符串有内置方法支持，请找到这个方法来实现）
'Fh190We92QbuC'.swapcase()

#4.请将字符串 ’Fh1qoWe92QbvC’ 中的数字按序取出，组成新的字符串并打印出来（提示：Python 字符串有内置方法可判断字符串是否为纯数字）
oldS='Fh1qoWe92QbvC'
newS=''
for s in oldS:
    if s.isdigit():
        newS+=s

print(newS)

#5.现有列表 lst = [2, 0, 3, 6, 9]，请打印出从小到大排列的列表 lst（不改变列表元素的原有顺序）
lst = [2, 0, 3, 6, 9]
sorted(lst)

#6.现有一个列表 l = [2, 3, 1, 2, 4, 3]，请实现 l = [2, 3, 1, 4]
l = [2, 3, 1, 2, 4, 3]
l1= list(set(l))
l1.sort(key=l.index)
print("l=",l1)

#7.现有字符串 ‘aasdebbcaa’，请统计字符串中每个字符出现的次数，将统计结果存储在一个字典里
string = 'aasdebbcaa'
{ a:string.count(a) for a in set(string.replace(' ','')) }

#8.完成一个函数，计算传入的字符串中的【数字】、【字母】、【空格】和【其他】的个数后返回
def count(str):
    number_num = char_num = space_num = other_num = 0
    for char in str:
        if char.isdigit():
            number_num += 1
        elif char.isalpha():
            char_num += 1
        elif char == ' ':
            space_num += 1
        else:
            other_num += 1
    print('数字有:%d个,字母有:%d个,空格有:%d个,其他有:%d个' % (
        number_num, char_num, space_num, other_num))

str=input('请输入一串字符串:')
count(str)

#9.完成一个函数，检查传入的字符串是否含有空格，如果有空格则删去字符串中的空格并返回结果
import re
def space(str):
    if str  == ''.join(str.split()):
        return 'no'
    else:
        str1=re.sub('\s','',str)
        return str1

print(space('hellowor ld'))

print(space('helloworld'))

#10.完成一个函数：随机产生一个数，让用户来猜，猜中则屏幕打印“恭喜你猜对了”并结束，若猜错，则提示用户是猜大了还是猜小了（提示：内置的 random 模块有产生随机数的方法）
import random
n = random.randint(1, 100)
guess = int(input("Enter an integer from 1 to 100: "))
while n != "guess":
    if guess < n:
        print ("guess is low")
        guess = int(input("Enter an integer from 1 to 100: "))
    elif guess > n:
        print ("guess is high")
        guess = int(input("Enter an integer from 1 to 100: "))
    else:
        print ("you guessed it!" )
        break