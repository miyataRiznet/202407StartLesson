"""
課題1
要件：ジョーカーを引いたら負けというシンプルなゲームを作成すること。

〜ルール〜
ジョーカー1枚を含む５３枚のシャッフルされたトランプをn人に１枚ずつ配っていき、
ジョーカーが配られた時点でその人を脱落としてまた初めからやり直す。
最後の１人になったときそれまでに配られたカードの総枚数×１万円を優勝賞金とする。

〜問題〜
脱落者がでたときのそれまでに配られたカードの総枚数と、優勝者の賞金を出力
"""

import random

def trump_game(i):
    card_list = ["normal"] * 52 + ["joker"]                                   # 53枚(内1枚ジョーカー)の山札を作成
    random.shuffle(card_list)                                                 # 山札をシャッフル
    joker_num = (card_list.index("joker")) + 1                                # (joker_num)枚目がジョーカー
    drop_player = player_list.pop(int(((joker_num - 1) % i)))                 # 脱落者を算出
    print(f'{total_card + joker_num}枚目でplayer{drop_player}が脱落しました')

    if len(player_list) > 1:                                                  # ゲーム継続可能が人数が残っている場合
        print('<カードをシャッフルしました>')
    else:                                                                     # 人数が残り1人となった場合
        print(f'Player{player_list[0]}の優勝')

    return joker_num

player_num = int(input("何人?>>>"))
game_times = player_num - 1                                                   # ゲームの回数は人数-1
total_card = 0
player_list = [i + 1 for i in range(player_num)]

for i in range(game_times + 1, 1, -1):
    total_card += trump_game(i)

print(f'優勝賞金{total_card}万円')
