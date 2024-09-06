"""
要件：画像を参考にメンバーをランダムで2チームに分割して、
      そのチームの中から1人のリーダーを選出して出力すること
"""

import random

members = ['大迫', '古橋', '久保', '堂安', '南野', '伊東', '田中', '遠藤', '富安', '吉田', '長友', '酒井']
random.shuffle(members)  # 配列の中身をシャッフル

# チームAとチームBのリストを作成
team_a = [members.pop(i) for i in range(int(len(members) / 2))]
team_b = members

# それぞれのチームからランダムなメンバーを選択し、リーダーとする
team_a_leader, team_b_leader = random.choice(team_a), random.choice(team_b)

print(f'チームA{team_a}リーダーは{team_a_leader}\nチームB{team_b}リーダーは{team_b_leader}')