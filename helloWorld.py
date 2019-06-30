a = 1+2
print(a)
print("=====================")
list = "HelloWold"
for i in list:
    print(i)
print("=====================")
for i in range(5):
    print(i)
mumber = [1,2,3,45,7]
print(mumber)
mumber.append("小甲鱼")
print(mumber)
mumber.extend(['北北','静静'])
print(mumber)
mumber.insert(0,0)
print(mumber)
print(mumber[8])
mumber.remove('静静')
print(mumber)
del mumber[7]
print(mumber)
mumber.pop()
print(mumber)
mumber.pop()
print(mumber)
mumber.pop(0)
mumber.pop()
mumber.append("lgy")
print(mumber)
mumber2 = mumber[:]
print(mumber2)
list2 = [7,['小甲鱼','牡丹'], 'abc']
print('小甲鱼' in list2)
print(list2[1][1])
print(8 * (8))
print(8 * (8,))
temp = ('a','b','c','d','e')
print(temp)
temp = temp[:2] + ("haha",) + temp[:2]
print(temp)
def myFirstFunction(i):
    print("我的第" + str(i) + "个函数")
    print("试试输出两句话")
myFirstFunction(1)
myFirstFunction(2)
def add(num1,num2):
    return (num1 + num2)
print("加法操作:" + str(add(4,5)))
def MySecondFunction(name):
    '函数定义过程中的name是叫形参'
    #因为Ta只是一个形式,表示占据一个参数位置
    print('传递进来的' + name + '叫做实参,因为Ta是具体的参数值')
MySecondFunction('LGyyy')
help(MySecondFunction)
def test(*params):
    print("参数的长度是:", len(params))
    print("第二个参数是:", params[1])
test(1,4,5,64,35,315,53)
def test(*params, exp):
    print("参数的长度是:", len(params), ",exp的值:", exp)
    print("第二个参数是:", params[1])
    print("exp:", exp)
test(1,4,5,64,35,315,53,exp = 8)
print("=====================")
def getMoney(day):
    a = 0.01
    i = 1
    sum = 0.01
    while(i < day):
        a = a * 2
        sum = sum + a
        i = i + 1
    return sum
def soutGrandfather(day):
    a = 0.01
    i = 1
    while(i < day):
        a = a * 2
        i = i + 1
    print("第", i ,"天要给了岳父money:", a)
    print("一共给了岳父money:", getMoney(i))
soutGrandfather(1)
        
