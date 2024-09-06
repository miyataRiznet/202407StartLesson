import math    #数学の機能を呼び出す宣言

height = int(input("身長を入力してください(cm)>>>"))
weight = int(input("体重を入力してください(kg)>>>"))

BMI = weight / (height * 0.01) ** 2
BMI = math.floor((BMI)*10) / 10     #小数点以下を切り捨てるメソッドのため、先に*10して209.・・・とすることで本来切り捨てたい箇所を合わせている

if (BMI < 18.5):    #BMIが18.5未満の場合は「低体重」
    result = "低体重"
elif (BMI < 25.0):  #BMIが18.5以上25.0未満の場合は「普通体重」
    result = "普通体重"
else:               #BMIが25以上の場合は「肥満体重」
    result = "肥満体重"

print(f"あなたのBMIは{BMI}で{result}です")  #文字列内で変数をキャストする必要なく使用できる、フォーマットリテラルを使用