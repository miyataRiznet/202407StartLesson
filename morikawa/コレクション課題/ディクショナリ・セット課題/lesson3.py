"""
要件：下記の二つの配列を使ってディクショナリを作成し、実行例の通りに出力されること
riz_member=['社長','東さん','岩切さん','谷口さん']
age_member=[35,39,35,20]
"""

riz_member=['社長','東さん','岩切さん','谷口さん']
age_member=[35,39,35,20]

riz_dictionary = dict(zip(riz_member, age_member))

print('リズメンバーの辞書↓')
print(riz_dictionary)
print(f'メンバー数:{len(riz_dictionary)}　平均年齢:{sum(riz_dictionary.values()) / len(riz_dictionary)}')