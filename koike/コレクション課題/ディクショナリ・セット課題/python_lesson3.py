riz_member=['社長','東さん','岩切さん','谷口さん']
age_member=[35,39,35,20]

combined_list=dict(zip(riz_member, age_member))

print("リズメンバーの辞書↓")
print(combined_list)
print(f'メンバー数:{len(riz_member)} 平均年齢{sum(age_member) / len(age_member)}')
