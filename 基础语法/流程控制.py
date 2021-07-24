'''
0.程序默认按 顺序语句执行
1.条件语句
    1.1 if cond:
            statement
    1.2 if cond:
            statement1
        else:
            statement2
    1.3 if cond1:
            statement1
        elif cond2:
            statement2
        ...
        else:
            statement3
    1.4 statement也可以使用switch语句嵌套
    python没有switch语句
2.循环语句
    2.1 while cond:
            statement
    2.2 for 迭代遍历 in 迭代对象:
            statement
3. 补充：
    continue 跳过本次循环
    break   结束当前循环
    pass 只占位不起作用
'''


#---------------手动实现switch模式，注意括号位置-------------#
def case1():
    print("case 1")

def case2():
    print("case 2")

def default():
    print("case 0")

def switch_demo():
    switch = {"1": case1,
              "2": case2}
    switch.get("1", default)()#输入选择并设置默认函数
#---------------——————————————————————————-------------#

if __name__ == '__main__':
    switch_demo()