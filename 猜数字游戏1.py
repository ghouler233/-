# 猜数字游戏

while(1):
    x="y"
    if x==input("play? y or n:"):
        print("good luck")

        import random
        random.seed(int(input("请输入种子:")))
        a=int(input("请输入范围起点"))
        b=int(input("请输入范围终点"))+1
        c=random.randint(a,b)
        d=int(input("请输入次数"))
        e=1
        f=int(input("请输入一个整数:"))

        while f!=c and e<d and a<f<b:
            if f>c:
                f=int(input("大了请输入:"))

            elif f<c:
                f=int(input("小了请输入:"))
            e=e+1

        if a>f:
            f=int(input("小过范围请输入:"))
        elif f>b:
            f=int(input("大过范围请输入:"))

        if f==c:
            print("win")
            x=input("again？ y or n:")
            if x=="n":
                print("out")
                break

        elif e==d:
            print("gg")
            x=input("again？ y or n:")
            if x=="n":
                print("out")
                break

    else:
        print("out")
        break