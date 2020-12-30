print('第一章-第二章------------------------------------------------------')

message = 'heLlo wOrLd'
print(message)
#开头只可以用_或者字母不可以用数字 并且不能包含空格 (1_message = 'dog')

print(message.title())
#首字母大写

print(message.upper())
#全部大写

print(message.lower())
#全部小写

first_name = 'ada'
last_name = 'wong'
full_name = first_name + ' ' + last_name
message = 'hello' + ' ' + full_name
print(message.title())
message = 'hello' + full_name
print(message.title())
#title会检测每一个空格后面的单词
#字符串可以用加号拼接

print('language:\n\tpython\n\tC++\n\tjava')
#\n换行 \t制表（TABLE）

language = ' py tho n '
print(language.rstrip() + '1')
print(language.lstrip() + '1')
print(language.strip() + '1')
print(language)
#暂时去掉左右空格

print(3**3)
#**等于乘方运算

age = 23
message = 'the age is ' + str(age)
print(message.title())
#强制类型转换str，不同类型变量不可以相加
# Ctrl+. 可以添加和取消折叠

print('第三章 列表------------------------------------------------------------')

bicycles = ['terk', 'annondale', 'red', 'spec', 1]
#列表包含的元素可以是不同类型

print(bicycles)
print(bicycles[-2].upper())
#输入负数可以访问倒数元素

bicycles[0] = 'giant'
print(bicycles)
#直接赋值可以替换列表元素

bicycles.append('ducati')
print(bicycles)
#列表末尾添加元素

bicycles.insert(1, 'suzuki')
print(bicycles)
#插入元素 需要索引和值

del bicycles[5]
print(bicycles)
#del 是永久删除 并需要知道索引

popped_bicycles = bicycles.pop()
print(popped_bicycles)
print(bicycles.pop(2).upper())
print(bicycles)
#弹出需要知道索引 或者默认-1

too_expensive = 'suzuki'
bicycles.remove(too_expensive)
print(bicycles)
#已知 值 但是索引 未知 可用remove

bicycles.sort(reverse = 1)
print(bicycles)
#永久按字母顺序排序 reverse可以让顺序反过来

numbers = [number for number in range(1,10)]
print(numbers)
numbers.sort(reverse=1)
print(numbers)
#sort 不止可以按字母顺序排序 也可以按数字大小排序

numbers.append('yamaha')
print(numbers)
#numbers.sort()
print(numbers)
#sort在int和str混合列表中作用不明

print('123')
print(sorted(bicycles, reverse = 0))
print(bicycles)
#暂时改变列表顺序

bicycles.reverse()
print(bicycles)
#永久改变顺序 不能在print里面调用reverse

length = str(len(bicycles))
print('The length of the list is ' + length + '.')
#len 可以返回列表元素个数

print('第四章 数字列表和元组----------------------------------------------------')

bicycles.append('yamaha')
bicycles.append('sakura')
bicycles.append('bike')
bicycles.append('honda')
print(bicycles)

for bike in bicycles:
    print(bike + ', is good one！')
print('but i am not decided yet')
#for会执行缩进的语句

print('==数字列表==')

numbers = []
#for循环中的列表必须先定义
for value in range(1,5):
    numbers.append(value)
    print(numbers)

numbers = list(range(2,11,1))
print(numbers)
#range(开始,结束,步长)
#切片也有步长[开始：结束：步长]

sqs = []
for value in numbers:
    sq = value**3
    sqs.append(sq)
print(sqs)
#输出三次方数列实例

print(str(min(sqs)) + ' ' + str(max(sqs)) + ' ' + str(sum(sqs)))
#简单数列值返回

sqs = [value+1 for value in range(1,11)]
print(sqs)
#简洁代码实例

print(bicycles)
print(bicycles[2:4])
print(bicycles[:4])
print(bicycles[2:])
print(bicycles[-3:])
print(bicycles[:-3])
#[会被包含:不会被包含]

for bike in bicycles[:3]:
    print(bike)
#遍历切片

bicycles_1 = bicycles[:]
bicycles.append('yamato')
print(bicycles)
print(bicycles_1)
#生成未关联的两个相同列表

print('==元组==')
dimensions = (100, 120, 50)
print(dimensions[0])
print(dimensions[1])
#元组元素和列表元素调用格式相同 但是定义需要用圆括号 且定义后不能单独修改元素

dimensions = (120, 80)
print(dimensions)
#但是可以重新定义整个元组

print('第五章 逻辑运算---------------------------------------------------------')

print(bicycles)
for bicycle in bicycles:
    if bicycle == 'yamaha':
        print(bicycle.upper())
    else:
        print(bicycle.title())
#for if else 后面都要加冒号缩进表示包含

age = 19
print(age == 19)
print(age != 19)
#!= = ! + =
print(age < 19)
print(age > 19)
print(age <= 21)
print(age >= 21)
#>= = > + =

print('==逻辑运算==')

logic = False
logic = age == 19 and age >=21
print(logic)
logic = age == 19 or age >= 31
print(logic)
#逻辑运算符

logic = 'yamaha' in bicycles
print(logic)
logic = 'yamaha' not in bicycles
print(logic)
#判断值是否在列表中

age = 12
if age <= 4:
    print('Free of charge')
elif age <= 18:
    print('Half price')
elif age <= 65:
    print('Adult price')
else:
    print('Elderly')
#if-else语句判断完成后会跳出整个if-else语句块， 最后的else可以省略
#如果想逐个检查的话可以连用if语句

requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(requested_topping + ' is added in your menu!')
    print('Order finished!')
else:
    print('Are you sure u want a plain pizza?')
#判断空列表（披萨点单实例）

available_toppings = ['vege', 'meat', 'olives', 'green paper']
requested_toppings = ['vege', 'meat', 'fart', 'olives']
print('--------Uni restrount---------')
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(requested_topping + 'is added in your menu!')
    else:
        print('Sorry, but we dont have ' + requested_topping + '.')
print('--------End of your menu---------')
#使用多个列表（披萨点单实例2）

print('第六章 字典------------------------------------------------------------')

alien_0 = {'color': 'green', 'point': 5}
print(alien_0['color'])
print(alien_0['point'])
#字典是 键-值 对应的列表 值 可以是 数字 字符 列表 字典

print(alien_0)
alien_0['X_position'] = 1
alien_0['Y_position'] = 20
print(alien_0)
alien_0['X_position'] = 100
print(alien_0)
#向字典 添加 和 修改 键-值 对

del alien_0['Y_position']
print(alien_0)
#删除的键-值对永远的消失了

favourate_language = {
    'jen': 'python',
    'sam': 'java',
    'bron': 'C',
    'charly': 'R',
}
print('==.items()的用法==')
print(favourate_language)
for name, item in favourate_language.items():
# .items()返回的是键值对
    print('\n' + name)
    print(item)
#字典中更重要的是键-值关系而不是顺序

#要在整个字典上使用items才能返回键值对
unit = {'a': 12, 'b': 13}
unit_1, unit_2 = unit.items()
key, value = unit_1
print(str(key) + str(value))

print('==.keys()的用法==')
for name in favourate_language.keys():
    print(name)
#.keys()用于需要 键 不需要 值 的时候

for name in favourate_language:
    print(name)
#遍历字典时默认遍历键

friends = ['sam', 'bron', 'jim']
for name in sorted(favourate_language.keys()):
#sorted() 可以按顺序查找
    print('Hi, ' + name)
    if name in friends:
        print('I see your favourate language is ' + favourate_language[name].title() + '!')
#遍历实例

print('\nlanguages have bmentioned:')
for name in favourate_language.values():
    print(name)
#遍历值

print('==嵌套==')

alien_0 = {'color': 'green', 'point': 5}
alien_1 = {'color': 'red', 'point': 10}
alien_2 = {'color': 'yellow', 'point': 20}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
#列表套字典实例

print('==自动生成外星人实例==')
aliens = []
for new_alian in range(30):
    new_alian = {'color': 'green', 'point': 5}
    aliens.append(new_alian)
print('There are ' + str(len(aliens)) + ' aliens in total!')
for alien in aliens[:5]:
    print(alien)
#自动生成30个外星人并显示前五个

print('第七章 用户输入--------------------------------------------------------')


# message = input('Tell me:')
# print(message)
# #复读机程序实例（input函数实例 ）

# message = 'Tell me'
# message += '\nwhy: '
# user = input(message)
# print('hello! ' + user)
# # += 可以拼接字符串

print('类型转换实例')
# print('\n==类型转换 str 到 int==')
# #age = input('how old are you? ')
# age = int(age)
# if age >= 18:
#     print('you are safe to drink!')
# else:
#     print('you are not allow to drink!')


print('复读机程序实例')
# current_number = 1
# active = True
# #使用标志可以让程序更加简洁
#
# message = ''
# # 比较的时候需要提前定义 否则无法运行
#
# while active and current_number <= 5:
#     message = input('\nplease input something: ')
#     if message != 'quit':
#         print(message)
#     else:
#         active = False
#     current_number += 1
# print('\nEnd of the program!')


print('第八章 函数-----------------------------------------------------------')


def greeting_uers(username):
    """xianshijiandandewenhouyu"""
    print(username+' Hello!')
greeting_uers('Sam')
#定义和使用函数

def discribe_pets(name, type):
    print('I have a ' + type + ', we called it ' + name + '!\n')
discribe_pets('harry', 'dog')
#位置实参 位置很重要

def discribe_animals(name, type):
    print('I have a ' + type + ', we called it ' + name + '!\n')
discribe_pets(type='dog', name='harry')
#关键字实参 位置并不重要

def discribe_animals(name='hurry', type='dog'):
    print('I have a ' + type + ', we called it ' + name + '!\n')
discribe_pets(name='harry',type='cat')
discribe_animals('wille')
discribe_animals()
#定义函数默认值

def return_full_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()
name = return_full_name('sam', 'lee')
print(name)

print('====传递列表====')

def greet_users(names):
    """向用户问好"""
    for name in names:
        print('Hi! ' + name.title())

users = ['sam', 'jir', 'charly']
greet_users(users)
#遍历列表

def make_pizza(number, *toppings):
    print('\nHi! customer!\n' + ' U ordered ' + str(number) + 'pizzas with ')
    for topping in toppings:
        print(topping + '!')

make_pizza(16, 'meat', 'beef', 'apple')
make_pizza(500, 'beer')
#传递任意数量的实参, *生成元组 并必须放在最后面

def users_info(f_name, l_name, **info):
    full_name = f_name + ' ' + l_name
    info['name'] = full_name
    print(info)

users_info('sam', 'charly', color='blue', position='beijing')
#注意键值对的形式

print('====模块====')

import pizza as p
p.making_pizza(15, 'meat', 'beer', 'apple')
#先导入模块 再引用模块中的函数

from pizza import making_pizza as mp
mp(15, 'meat')
#从模块中导入单独函数, 使用 as 设定别名避免冲突


print('第九章 类-----------------------------------------------------------')


class Dog():
    """小狗模拟器"""

    def __init__(self, name, age):
        """初始化属性 name 和 age """
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗蹲下"""
        print(self.name.title() + 'is now sitting!')

    def roll(self):
        """模拟小狗打滚"""
        print(self.name.title() + 'is now rolling!')
#可以根据 类 创建 实例

print('====访问属性====')
my_dog = Dog('Cleo', 3)
print(my_dog)
print(my_dog.name.title())
print(my_dog.age)
#调用并储存实例， 首字母大写是 类 ， 首字母小写是 实例

print('====调用方法====')
my_dog.roll()
my_dog.sit()

your_dog = Dog('wille', 59)
print(your_dog)
your_dog.roll()
your_dog.sit()
print(your_dog.name.title())

print('\n====餐馆类实例====')

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type, *flavours):
        """定义参数"""
        self.name = restaurant_name
        self.type = cuisine_type

    def describ_restaurant(self):
        """描述餐厅"""
        print("The restaurant's name is "  + self.name + '!\n')
        print('The cuisine type of the restaurant is ' + self.type.title() + '!\n')

    def open_restaurant(self):
        """表示餐厅营业状态"""
        print(self.name.title() + ' is now open!\n')

    def update_name(self, new_name):
        """修改餐厅名称"""
        self.name = new_name

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        # super() 继承时不能加 self
        self.flavours = ['barry', 'apple', 'pear']

    def list_all_ice_cream(self):
        for ices in self.flavours:
            print('They have ' + ices)
# self 是把 类 中的 方法 连接起来的东西 不同方法中只用 定义方法 中的 参数时需要加 self

restaurant_1 = IceCreamStand('1918', 'west')
restaurant_2 = IceCreamStand('Beijing', "chinese")
restaurant_3 = IceCreamStand('little chuan', 'fast food')
restaurant_1.describ_restaurant()
restaurant_1.open_restaurant()
restaurant_3.list_all_ice_cream()

restaurant_2.name = 'Shang hai'
restaurant_2.describ_restaurant()
#直接修改实例中的参数

restaurant_2.update_name('Huhhot')
restaurant_2.describ_restaurant()

from collections import OrderedDict
from random import randint
#返回范围内的随机数

class Die():
    """建立骰子的类"""
    def __init__(self, faces=6):
        """建立骰子面数的形参"""
        self.faces = faces

    def roll_die(self):
        """随机数"""
        point = randint(1,self.faces)
        print(point)

    def ten_times(self, time):
        count = time
        while count != 0:
            point = randint(1,self.faces)
            print(point)
            count -= 1

six_faces = Die(6)

print('\n====6个面的骰子十次====')

Die(6).ten_times(5)

print('\n====十个面的骰子十次====')

Die(10).ten_times(5)

print('\n====二十个面的骰子十次====\n')

Die(20).ten_times(5)

print('\n第十章 文件和异常----------------------------------------------------\n')

with open('pi_reader.txt') as file_obj:
    # open 在 主程序文件 目录中寻找 文件 并返回一个表示文件的 对象
    # with 会在不需要文件后将文件关掉 也可以用 close 但是 with可以让python自己确定什么时候关掉文件
    contents = file_obj.read()
    print(contents.rstrip())
    # rstrip 可以删掉 read（） 返回的空字符串

with open('D:\Python\pythonProject1\pi_reader.txt') as file_obj:
    #查找绝对位置文件
    contents = file_obj.read()
    print(contents.rstrip())

file_name = 'pi_reader.txt'
with open('D:\Python\pythonProject1\pi_reader.txt') as file_obj:
    contents = file_obj
    print('\n====直接输出文件====')
    print(contents)
    print('\n====逐行打印====')
    for line in contents:
        print(line)
        #可以加rsteip删掉留白

with open('pi_reader.txt') as file_obj:
    lines = file_obj.readlines()
for line in lines:
    print(line)
#可在with代码块外使用

with open('D:\Python\pythonProject1\python_appendix\chapter_10\pi_million_digits.txt') as pi_million:
    lines = pi_million.readlines()

pi_string = ''

for line in lines:
    pi_string += line.strip()

print(len(pi_string))

print(pi_string[:49])

print(len(pi_string[:20]))

print((0, 1, 2, 3, 4, 5)[:3])
#元组切片

print('ABCDEFG'[::2])
#字符串切片[开始:结束:步长]

birth_day = '1997'
if birth_day in pi_string:
    print('Your birth day is luckey!')
else:
    print('uhhhhhhhhh!')
#在字符串中查找字符

print('\n====写入文件====')
file_name = 'programing.txt'

number = 12345
with open(file_name, 'w') as file_object:
# 读取模式‘w’ 写入模式‘w’ 附加模式‘a’ 省略自动默认只读模式
    file_object.write('I love\n')
    file_object.write(str(number))
    #文件中只可以保存字符串变量

with open(file_name, 'a') as file_object:
    file_object.write('\naddaddaaddd')

print('\n====处理错误====')

print('give me two numbers, I will divide them\n press "q" to leave')

# while True:
#     firs_number = input('first number is: ')
#     if firs_number == 'q':
#         break
#     second_number = input('\nsecond number is: ')
#     if second_number == 'q':
#         break
#     try:
#         answer = int(firs_number) / int(second_number)
#         #别忘了类型转换
#     except ZeroDivisionError:
#         print('you cant input 0!')
#     else:
#         print(str(answer))

print('\n====分析文本====')

title = 'Alice in Wonderland'
print(title.split())
# split() 可以以空格分开字符串

file_name = "D:\Python\pythonProject1\python_appendix\chapter_10\ALice.txt"
try:
    with open(file_name) as book:
        #路径不区分大小写
        contents = book.read()

except FileNotFoundError:
    print('File not fond!')

else:
    print(len(contents.split()))

def count_words(file_name):
    """计算文件含有的单词数量"""
    try:
        with open(file_name) as book:
            # 路径不区分大小写
            contents = book.read()

    except FileNotFoundError:
        pass
        #让程序跳过错误
    else:
        print(len(contents.split()))

count_words('D:\Python\pythonProject1\python_appendix\chapter_10\little_women.txt')
count_words('alice')

print('\n====查找单词出现次数====')

file_path = 'D:\Python\pythonProject1\python_appendix\chapter_10\little_women.txt'

with open(file_path) as little_women:
    contents = little_women.read()

word_count = contents.split()
count = 0
for word in word_count:
    if word == 'women':
        count += 1
print(str(count))

print('\n====存储数据====')
import json

numbers = [1, 2, 3, 4, 5]

file_name = 'numbers.json'
with open(file_name, 'w') as f_obj:
    json.dump(numbers, f_obj)

# json 可以储存各种东西 列表 字典， txt只能储存字符串

with open(file_name) as f_obj:
    numbers = json.load(f_obj)

print(numbers)
test = {'abd': 123}
with open('testfile.json', 'w') as t:
    t.write(json.dumps(test))
test = {'abd': 234}
with open('testfile.json', 'a') as t:
    json.dump(test, t)
# dump 和 dumps 的用法区别

with open('testfile.json', 'a') as t:
    print(t)

print('\n第十一章 测试代码----------------------------------------------------\n')

def get_name(first='defult', last='defult'):
    full_name = first + ' ' + last
    return full_name.title()


import unittest

class NamesTestCase(unittest.TestCase):
    """测试文件"""

    def test_first_last_name(self):
        """是否能够正确处理"""
        formatted_name = get_name('Sam', 'Jack')
        self.assertEqual(formatted_name, 'Sam Jack')

unittest.main()
