curry = 1

print("カレーを召し上がれ")

while True:
    print(f"{curry}皿のカレーをたべました")
    refill = input("おかわりはいかがですか？(y/n)>>>")
    if refill == "y":
        curry = curry + 1
    else:
        print("ごちそうさまでした！")
        break

