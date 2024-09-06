import math

height = int(input("身長を入力してください(cm)>>>"))
weight = int(input("体重を入力してください(kg)>>>"))

BMI = weight / (height * 0.01) ** 2
BMI = math.floor((BMI)*10) / 10
BMI = str(BMI)

print("あなたのBMIは" + BMI + "です")