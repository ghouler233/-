#判断质数和合数
n=int(input("请输入一个正整数:"))
s=1
if n==2 or n==3:
        print(f"{n}是质数")
elif n==1:
        print((f"{n}不是质数,不是合数"))
else:
        for i in range(2,4):
                s=n%i*s
        if s==0:
                print(f"{n}是合数")
        if s!=0:
                print(f"{n}是质数")