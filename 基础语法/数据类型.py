'''
1.基本数据类型：
    不可变数据类型：Number(数字)、String(字符串)、Tuple(元组)
    可变数据类型：List(列表)、Set(集合)、Dictionary(字典)

    数据类型转换：
        int(x [,base])将x转换为一个整数
        float(x)将x转换到一个浮点数
        complex(real [,imag])创建一个复数
        str(x)将对象 x 转换为字符串
        tuple(s)将序列 s 转换为一个元组
        list(s)将序列 s 转换为一个列表
        set(s)转换为可变集合
        dict(d)创建一个字典。d 必须是一个 (key, value)元组序列。
        frozenset(s)转换为不可变集合
        chr(x)将一个整数转换为一个字符
        ord(x)将一个字符转换为它的整数值
        hex(x)将一个整数转换为一个十六进制字符串
        oct(x)将一个整数转换为一个八进制字符串

python中基础数据类型也是对象，万物皆对象(变量都是指向对象的指针)，可以使用del var1[,var2[,var3[....,varN]]]显式删除

'''


def basic_data_type():
    # 不可变数据类型
    num = 2.3
    string = "string"
    tuple = (2, 3, 4.5)

    # 可变数据类型
    list = [2.3, "string"]  # 可嵌套
    set = {1, 2, 3.3}
    dic = {"1": 1.1, "2": 2.2}
    print(dic)

    # 多变量赋值
    a = b = c = 1
    a, b, c = 1, 2, "string"

    # 检查数据类型
    '''
    type()不会认为子类是一种父类类型。
    isinstance()会认为子类是一种父类类型。
    bool 是 int 的子类，True 和 False 可以和数字相加 True==1，False==0 是会返回 Ture，但可以通过 is 来判断类型。
    '''
    print(type(1 + 2j))
    print(isinstance(1 + 2j, complex))


def number_demo():
    # 支持 int、float、bool、complex
    # 运算见  运算逻辑.py
    a, b, c, d = 1, 1.0, True, 1 + 2j
    print(a, b, c, d)


def string_demo():
    '''
    1. 定义：字符串用单引号 ' 或双引号 " 括起来或str()函数转型，使用反斜杠 \ 转义特殊字符
    2. 运算：+拼接  * 复制  len(str)计算长度
    3. 索引：前索引0-(N-1) 后索引(-N)-(-1)  截取保前不保后
    '''

    s1 = "this is a demo"
    s2 = str("ssss")

    print(s1 + s2)
    print(s1 * 2)
    print(len(s1))

    print(s1[0:5])


def tuple_demo():
    '''
    1. 定义：写在小括号 () 里逗号隔开，不可修改，除非某个元素是list，元组与列表和string都是sequence，不同之处在于元组的元素不能修改。
    2. 运算：+拼接  * 复制  len(str)计算长度
    3. 索引：前索引0-(N-1) 后索引(-N)-(-1)  截取保前不保后
    元组就是升级版的string，string只能序列化存储字符，tuple啥都能存（基础数据类型，对象）
    '''
    tuple1 = ('a', 2)
    tuple2 = ('b', 4)

    print(tuple1 + tuple2)
    print(tuple1 * 2)
    print(len(tuple1))


def list_demo():
    '''
    1.定义：写在小括号[]里逗号隔开，可修改，啥都能存（基础数据类型，对象），支持嵌套
    2.运算：+拼接  * 复制  len(str)计算长度
         增删改查 ：
            增：list.append(对象)   list.inser(索引，对象)   list.extend(string)
            删：del list[索引]  list.pop()  list.remove(元素) list.clear()
            改：list[索引] = 新对象
            查：list[索引]
    3.索引：前索引0-(N-1) 后索引(-N)-(-1)  截取保前不保后
    '''
    list1 = ['abcd', 786, 2.23, 'runoob', 70.2]
    list2 = [1]

    print(list1 + list2)
    print(list1 * 2)
    print(len(list1))

    list1[2] = 22


def set_demo():
    '''
    1.定义：使用大括号 { } 或者 set() 函数创建，元素不可重复
    2.运算：& | - ^ 交 并 差 异或
        增删改查：
            增：set.add(对象)
            删：set.pop()    set.discard(对象)
            改：set.update(原对象，新对象)
            查：for set in sets
    '''
    set1 = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
    set2 = {'Google', 'Taobao', 'Runoob'}
    set3 = {1, 2}

    print(set1 | set3)
    for t in set3:
        print(t)


def dic_demo():
    '''
    1.定义：使用大括号 { } 或者 dict() 函数创建，存储key:value，key不可重复不可修改
    2.运算：增删改查：
                增：dict[key] = value     dict.setdefault(key, value)
                删：dict.pop(key)     dict.popitem()删除键值对并作为tuple
                改：dict[key] = value
                查：dict[key]    dict.get(key)     dict.keys()    dict.values()
    '''
    dict1 = {"a": 1, "b": 2}
    dict2 = {x: x ** 2 for x in (2, 4, 6)}
    dict3 = dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
    dict4 = dict(Runoob=1, Google=2, Taobao=3)

    print(dict1['a'])  # 输出键为 'one' 的值
    print(dict4)  # 输出完整的字典
    print(dict2.keys())  # 输出所有键
    print(dict2.values())  # 输出所有值


if __name__ == '__main__':
    basic_data_type()
    # number_demo()
    # string_demo()
    # tuple_demo()
    # set_demo()
    # dic_demo()
