import random

dice = [1, 2, 3, 4, 5, 6]
count = 0
throw = set()  

print('サイコロを繰り返しふります')


while len(throw) < 6:
    result = random.choice(dice)
    throw.add(result)
    print(result)
    count += 1

print(f'{count}回で揃いました')
