"""
要件：画像を参考にメンバーをランダムで2チームに分割して、
そのチームの中から1人のリーダーを選出して出力すること
"""

import random

members =['大迫', '古橋', '久保', '堂安', '南野', '伊東', '田中', '遠藤', '富安', '吉田', '長友', '酒井']
random.shuffle(members)

team_a = []
team_b = []

for index,data in enumerate(members):
    if index % 2 == 1:
        team_a.append(data)
    else:
        team_b.append(data)

print(f'チームA{team_a}リーダーは{team_a[0]}')
print(f'チームB{team_b}リーダーは{team_b[0]}')