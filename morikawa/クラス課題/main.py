"""
要件：実行するファイルとは別にCalculationクラス配置したファイルを作成し実行例のとおりになること
条件：実行するファイル名はmain.py、Calculationクラス配置するファイル名はcalc.pyとする。
"""
## main.py

import calc

num1=int(input('値1>>>'))
num2=int(input('値2>>>'))
cal=calc.Calculation()
add_num=cal.add(num1,num2)
sub_num=cal.sub(num1,num2)
print(f'足すと{add_num}')
print(f'引くと{sub_num}')