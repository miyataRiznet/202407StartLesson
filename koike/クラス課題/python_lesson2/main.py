import calc

#メインの処理
num1=int(input('値1>>>'))
num2=int(input('値2>>>'))

#クラスを呼び出す
cal=calc.Calculation()
add_num=cal.add(num1,num2)
sub_num=cal.sub(num1,num2)

#答えを表示
print(f'足すと{add_num}')
print(f'引くと{sub_num}')