"""
要件：ジョーカーを引いたら負けというシンプルなゲームを作成すること。

〜ルール〜
ジョーカー1枚を含む５３枚のシャッフルされたトランプをn人に１枚ずつ配っていき、
ジョーカーが配られた時点でその人を脱落としてまた初めからやり直す。
最後の１人になったときそれまでに配られたカードの総枚数×１万円を優勝賞金とする。

〜問題〜
脱落者がでたときのそれまでに配られたカードの総枚数と、優勝者の賞金を出力
"""
import random
# 乱数固定関数（検証時に使用）
# random.seed() 


# cardの生成：全53枚、うち1枚jokerが入る
# 生成したcardの配列を戻す
def card_system():
    card = []

    # 52枚の 'n' カードをcard配列で作成
    for i in range(52):
        card.append('normal')
    # card配列に 'joker' カードを1枚追加
    card.append('joker')
    return card

"""
# cardをシャッフルする
def card_shuffle(card):
    random.shuffle(card)
    return card
"""

# プレイヤー人数を決定しプレイヤー番号の配列を戻す
def playerchoice():
    player_list = []
    pcount = int(input('何人?>>>'))
    for i in range(pcount):
        player_list.append(f'player{i+1}')
    return player_list

# playerの情報と、カードの情報でゲーム開始
def game(player,card):
    # 変数の宣言、初期化
    money = 0
    joker_flug = False

    # (参加プレイヤー数 - 1)　の数 ゲームを行う
    for game in range(len(player)-1): #while not len(player) == 1:
        # 変数の宣言、初期化
        joker_flug = False
        count = 0
        
        # cardの枚数分繰り返す
        for draw in range(len(card)-1): # while not joker_flug:
            # cardから1つランダムに選択する
            # random.randint = 現在のcardの要素数を取得し、
            # インデックス0からmaxまでの大きさでランダムにインデックス番号を取得する
            draw_num = random.randint(0, len(card)-1)

            # 上記draw_numにて取得したインデックス番号のカードを引く
            popvalue = card.pop(draw_num)

            # 引いた数をカウント
            count += 1
            # 優勝賞金をカウント
            money += 1

            # 引いたカードが'normal'ではない時
            if popvalue != 'normal':
                dropout = int( (count-1) % len(player) ) # 脱落したプレイヤーの計算
                print(f'{count}枚目で{player[dropout]}が脱落しました')
                card = card_system() # カードの再生成
                print('<カードをシャッフルしました>') # カードの選択時にランダムに選択しているためcardlistのシャッフルは行わない
                player.remove(player[dropout]) # プレイヤーの削除
                break

    # 優勝者の表示、優勝賞金の表示
    print(f'{player[0]}の優勝') # mainに戻ってもremoveしているのでplayer[0]で優勝者を表示できる
    print(f'優勝賞金は{money}万円') # return moneyでmainで表示しても良い


# main
card = card_system() # カードの初期生成
player = playerchoice() # プレイヤー数の決定
game(player, card) # ゲームの開始