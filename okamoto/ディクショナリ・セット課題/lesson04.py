"""
要件：サイコロを繰り返し振って、１～６の目すべてが出揃うまでの回数を出力せよ
"""

import random

dice_list = [1, 2, 3, 4, 5, 6]
count = 0
check_set = set()  # 空のセットを作成

print('サイコロを繰り返しふります')

#セットに出た目を追加していく。セットは要素が重複しないため、「要素数が6になる=全ての目が出揃う」となる
while len(check_set) < 6:
    result = random.choice(dice_list)
    check_set.add(result)
    print(result)
    count += 1

print(f'{count}回で揃いました')