# 猜数字游戏
h=input("开始游戏 y or n:")
i="y"
j="n"
if h==i:
    print(f"{"祝你好运":^145}")
    z=1
elif h==j:
    z=0
    print("拜拜")
while(z):
    import random
    random.seed(int(input("输入种子:")))
    x=int(input("范围起点:"))
    y=int(input("范围终点:"))
    a=random.randint(x,y)
    b=1
    c=int(input("次数"))
    d=int(input("输入一个整数:"))
    while a!=d and b<c:
        if a>d and x<d<y:
            d=int(input("小了重试:"))
            b=b+1
        elif a<d and x<d<y:
            d=int(input("大了重试:"))
            b=b+1
        if d>y:
            d=int(input("大过范围重试:"))
        elif d<x:
            d=int(input("小过范围重试:"))
    if a==d:
        print(f"win,用了{b}次")
        e="y"
        f="n"
        g=input("重新游戏输入 y or n:")
        if g==e:
            print(f"{"祝你好运":^145}")
        elif g==f:
            print(f"{"菜":^145}")
            z=0
    elif b==c:
        print(f"{"gg":^145}")
        e="y"
        f="n"
        g=input("重新游戏输入 y or n:")
        if g==e:
            print(f"{"祝你好运":^145}")
        elif g==f:
            print(f"{"菜":^145}")
            z=0