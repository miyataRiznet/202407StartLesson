"""
要件：サイコロを繰り返し振って、１～６の目すべてが出揃うまでの回数を出力せよ
"""
import random as rnd
# サイコロのリストの中からランダムに値を抽出し返すメソッド
# 引数 N :  取り出したいリスト(サイコロのリスト)
# 戻り値：  取り出したサイコロの出目(type:int)
def throw_dice(N):
    result = rnd.choice(N)
    return result

# サイコロのリストを作成
dice = [1, 2, 3, 4, 5, 6]
# サイコロの出目が全て出現したか確認する集合
result_set = set()
# サイコロを振った回数をカウントする変数
count = 0

print('サイコロを繰り返しふります')

# 繰り返しサイコロを振り、
# 集合が6より小さければ出目が全て出現していないと判断し繰り返す
while len(result_set) < 6:
    result = throw_dice(dice)
    print(result) # サイコロの出目を表示
    count += 1 # サイコロ振った回数をインクリメント
    result_set.add(result) # 集合にサイコロの出目を追加(重複しない)

# 何回振って出目が全て出現したかを表示
print(f'{count}回で揃いました')