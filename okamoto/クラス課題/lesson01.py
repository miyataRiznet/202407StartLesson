""" 要件：下記のコードを実行すると実行例のようになるようCalculationクラスを作成すること
※同ファイル内にCalculationクラスを作成してよい """

class Calculation:
    def add(self, num1, num2):
        return (num1 + num2)

    def sub(self, num1, num2):
        return (num1 - num2)

num1 = int(input('値1>>>'))
num2 = int(input('値2>>>'))

cal = Calculation()

add_num = cal.add(num1, num2)
sub_num = cal.sub(num1, num2)

print(f'足すと{add_num}')
print(f'引くと{sub_num}')