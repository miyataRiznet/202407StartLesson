""" 
スライムとボスで戦わせるゲームを作成する。
ボスのHPやスライムの攻撃力等のゲームバランスは自身でカスタマイズしてよい。
あくまでこのようなゲームを作る事が課題である。
条件：
1.	スライムの生成数はユーザーが入力した数字を使用
2.	ボスが死ぬまで、スライムの1匹目~n匹目まで攻撃を続ける
3.	最後にボスが生きていたらボスの勝ち。スライムが生きていた場合はスライムの勝ち
4.	SlimeクラスとBossクラスを作成すること
"""

import slime
import boss
import time

# 生成したスライムとボスで戦わせるメソッド
def battle (slimes,theboss):
    # スライムが１体以上いる事を確認する
    slime_check(slimes)

    # ボスの初期HPを取得
    bosshp = theboss.get_hp()

    # スライムの個数分、繰り返し戦わせる
    for sl in list(slimes):
        slimehp = sl.get_hp() # 各スライムの初期HP
        print(f'~{sl.get_name()}召喚~')
        time.sleep(1)

        # スライムのHPが0以下にならない時、繰り返す
        while not slimehp <= 0:
            bosshp = sl.slime_attack(theboss,slimehp,bosshp) # スライムの攻撃を行い、減少したボスのHPを代入
            
            # ボスのHPが0以下ではない時、ボスの攻撃
            if not bosshp <= 0:
                slimehp = theboss.attack(sl,slimehp,bosshp) # ボスの攻撃を行い、減少したスライムのHPを代入
                
            else: # ボスHPが0以下の時、whileループを抜ける
                break

        else: # スライムのHPが0以下の時
            sl.down() # スライムが気絶したメッセージを表示
            slimes.remove(sl) # 戦っていたスライムを消去する
            

        # ボスのHPが0以下の時、勝利メッセージを表示    
        if bosshp <= 0:
            print('ボスを倒した!')
            print('*****スライムチームの勝ち!*****')
            break
        
        # slimesリストが空になった時、敗北メッセージを表示
        if not slimes:
            print('戦えるスライムがいなくなった...目の前が真っ白になった!')
            print('*****スライムチームの負け*****')
            break


# スライムが生成されているかチェックする
def slime_check(slimes):

    # listに格納しているslimeが、生成時のユーザー入力値が'0'だとlistが空になるためFalseになる
    if slimes:
        print('Battle開始!')
        
    else:
        print('slimeがいないよ!戦えないからやり直して!')
        exit()


# Main
## Slimeオブジェクトを格納するlist
slimes = []

#生成数を標準入力より決定
summon_num = int(input('召喚したいスライム数を入力してください>>>'))
# 入力された数、スライムを生成
for num in range(summon_num):
    slimes.append(slime.Slime(num))
    print(f'名前:{slimes[num].get_name()},HP:{slimes[num].get_hp()},攻撃力:{slimes[num].get_atk()}')

# ボス生成
theboss = boss.Boss()

# 戦わせる
battle(slimes,theboss)
