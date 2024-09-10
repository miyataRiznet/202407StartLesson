"""
要件：2024というのはすべての桁が偶数の数字です。
では、任意の数を入力してもらいすべての桁が
偶数の場合は[OK]そうでない場合は[NG]と出力する処理を作成してください。(入力される数字はn >= 0 )
"""

import sys
# 数字を入力
n = input('数字>>>')
# 入力値nを１桁ごとに配列で宣言、初期化
#nlist = [int(num) for num in list(str(n))]

# 奇数であれば 'NG' と出力し処理を終了
for i in list(n):
    if int(i) % 2 == 1:
        print('NG')
        sys.exit()

# 偶数であれば 'OK' と出力
print("OK")