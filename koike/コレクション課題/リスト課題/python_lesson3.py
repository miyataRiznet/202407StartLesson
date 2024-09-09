numbers = input("数字>>")

for i in numbers: 
    if int(i) % 2 != 0:
        print("NG")
        break
else:
    print("OK")