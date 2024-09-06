plan=int(input("計算方法を選択[1.足し算/2.引き算/3.掛け算](数字で入力)>>>"))
num1=int(input("数字1を入力>>>"))
num2=int(input("数字2を入力>>>"))

def add(num1,num2):
    return num1 + num2
def subtract(num1,num2):
    return num1 - num2
def multiply(num1,num2):
    return num1 * num2

if plan==1:
    result=add(num1,num2)
elif plan==2:
    result=subtract(num1,num2)
elif plan==3:
    result=multiply(num1,num2)

print(result)