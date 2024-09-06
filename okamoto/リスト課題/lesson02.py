"""
要件：画像を参考にメンバーをランダムで2チームに分割して、
      そのチームの中から1人のリーダーを選出して出力すること
"""

import random

members = ['大迫', '古橋', '久保', '堂安', '南野', '伊東', '田中', '遠藤', '富安', '吉田', '長友', '酒井']
random.shuffle(members)  # 配列の中身をシャッフル

# シャッフル後の前半分と後半分をリスト化し、それぞれチームAとチームBに代入
team_a, team_b = members[:int(len(members) / 2)], members[int(len(members) / 2):]

print(f'チームA{team_a}リーダーは{team_a[0]}\nチームB{team_b}リーダーは{team_b[0]}')