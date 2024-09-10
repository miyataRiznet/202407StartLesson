import random

def joker_game(n_players):
    deck = ['normal'] * 52 + ['joker']  # 52枚の普通のカードと1枚のジョーカー
    total_cards = 0  # 配られたカードの総数
    players = list(range(1, n_players + 1))  # プレイヤーリスト

    while len(players) > 1:
        random.shuffle(deck)  # デッキをシャッフル
        for i, card in enumerate(deck):
            total_cards += 1
            current_player = players[i % len(players)]  # 現在のプレイヤー
            if card == 'joker':  # ジョーカーを引いた場合
                print(f"{total_cards}枚目でPlayer{current_player}が脱落しました")
                players.remove(current_player)  # プレイヤーを脱落させる
                print("<カードをシャッフルしました>")
                break  # 新しいラウンドを開始

    # 優勝者と賞金の出力
    winner = players[0]
    prize = total_cards * 1  # 1枚あたり1万円
    print(f"Player{winner}の優勝")
    print(f"優勝賞金 {prize}万円")

# 人数入力
n_players = int(input("何人?>>>: "))
joker_game(n_players)