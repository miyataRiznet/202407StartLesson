import random

members = ['大迫','古橋','久保','堂安','南野','伊東','田中','遠藤','富安','吉田','長友','酒井']
random.shuffle(members) #配列をシャッフル
teamA = members[:6]
teamB = members[6:]

print(f"チームA{teamA}リーダーは{random.choice(teamA)}")
print(f"チームB{teamB}リーダーは{random.choice(teamB)}")