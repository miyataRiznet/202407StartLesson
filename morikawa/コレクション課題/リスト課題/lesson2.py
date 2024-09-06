"""
要件：画像を参考にメンバーをランダムで2チームに分割して、
そのチームの中から1人のリーダーを選出して出力すること
"""
# randommモジュールをimport
import random
# 配列の宣言と初期化
members = ['久保', '酒井', '吉田', '富安', '伊藤', '田中', '堂安', '南野', '大迫', '遠藤', '古橋', '長友']
# 配列の要素シャッフル
random.shuffle(members)

# 配列の要素数上限を取得し2分割した値をスライス用変数slに代入
sl=int(len(members) / 2)
# slを使用しmembers配列を2分割
team_a = members[:sl]
team_b = members[sl:]

# 2分割した配列を表示、配列の先頭をリーダーに指定
print(f'チームA{team_a}リーダーは{team_a[0]}')
print(f'チームB{team_b}リーダーは{team_b[0]}')