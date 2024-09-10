""" 要件：実行するファイルとは別にCalculationクラス配置したファイルを作成し実行例のとおりになること
条件：実行するファイル名はmain.py、Calculationクラス配置するファイル名はcalc.pyとする。 """

# __pycache__ディレクトリを作成しないようにする
import sys
sys.dont_write_bytecode = True

import Calculation as Calc  # モジュールとしてCalculation.pyを呼び出し、Calcと命名（＝エイリアスを割り当てる）

num1 = int(input('値1>>>'))
num2 = int(input('値2>>>'))

cal = Calc.Calculation()  # 別ファイルのクラスを呼び出す際は「モジュール.クラス()」

add_num = cal.add(num1, num2)
sub_num = cal.sub(num1, num2)

print(f'足すと{add_num}')
print(f'引くと{sub_num}')