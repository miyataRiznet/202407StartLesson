"""
要件：以下の配列を使用し、下記の画像の通り出力すること
"""

score_list = [81, 92, 100]

total = 0

for i in score_list:
    total += i

average = total / len(score_list)

print(f'合計{total}点、平均{average}点')