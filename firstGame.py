import random

secret = random.randint(0,9)
print("Fitst Game")
temp = input("猜猜我现在心里想的数字时多少:")
guess = int(temp)
num = 1
flag = 0

while (num < 3) :
    if guess == secret :
        print("你猜对了")
        flag = 1
        break
    else :
        error = str(num)
        if guess > secret :
            print("第" + error + "次机会,你猜大了")
        else :
            print("第" + error + "次机会,你猜小了")

        temp = input("你再试试:")
        guess = int(temp)
        num += 1;
if (flag != 1):
    print("你没猜对,你没机会咯,88")
str = r"好吧,I'm fine"
print(str)
print("Game Over")
