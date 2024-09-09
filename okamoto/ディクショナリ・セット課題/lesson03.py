"""
要件：下記の二つの配列を使ってディクショナリを作成し、実行例の通りに出力されること
riz_member=['社長','東さん','岩切さん','谷口さん']
age_member=[35,39,35,20]
"""

riz_member = ['社長', '東さん', '岩切さん', '谷口さん']
age_member = [35, 39, 35, 20]

result_dict = dict(zip(riz_member, age_member))  # riz_memberリストがキー、age_memberリストがバリューの辞書を作成

print(result_dict)
print(f'メンバー数:{len(riz_member)}  平均年齢{sum(age_member) / len(age_member)}')