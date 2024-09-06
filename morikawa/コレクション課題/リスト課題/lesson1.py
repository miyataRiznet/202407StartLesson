"""
要件：以下の配列を使用し、下記の画像の通り出力すること
[81,92,100]
"""

# listの要素を足した合計を出力する関数
def list_add(data):
    ans = 0
    for i in data:
        ans += i
    return ans

# main

point = [81, 92, 100]

# 配列の合計値を取得、配列の合計値/配列の要素数
print(f'合計{list_add(point)}点、平均{list_add(point) / len(point)}点')