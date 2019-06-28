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
