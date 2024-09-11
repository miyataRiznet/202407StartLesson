import random

class Slime:
    def __init__(self, number):
        self.number = number
        self.level = random.randint(1, 15)  # ランダムにレベルを設定
        self.hp = random.randint(50, 200)  # ランダムにHPを設定
        self.attack_power = self.level * 1.5  # 攻撃力はレベル×1.5

    def attack(self, boss):
        damage = self.attack_power
        boss.hp -= damage
        print(f"{self.number}匹目のスライムのこうげき(Lv:{self.level})!")
        print(f"{damage}のダメージ")
        print(f"ボスのHP {boss.hp:.1f} / スライムのHP {self.hp}")
        return boss.hp <= 0  # ボスのHPが0以下になったか判定
    
class Boss:
    def __init__(self):
        self.hp = 500  # ボスのHP
        self.attack_power = 20  # ボスの攻撃力

    def attack(self, slime):
        damage = self.attack_power
        slime.hp -= damage
        print(f"ボスのこうげき")
        print(f"{damage}のダメージ")
        print(f"ボスのHP {self.hp:.1f} / スライムのHP {slime.hp}")
        return slime.hp <= 0  # スライムのHPが0以下になったか判定
    
def game_start():
    # プレイヤーにスライムの数を入力させる
    num_slimes = int(input("何体のスライムでたたかう？>>> "))

    # クランを作成
    slimes = [Slime(i + 1) for i in range(num_slimes)]
    boss = Boss()
    print(f"{num_slimes}匹のスライムが誕生 ボスがあらわれた！")

    # ゲームループ
    slime_index = 0  # 現在攻撃中のスライムのインデックス
    while True:

        # スライムの攻撃
        current_slime = slimes[slime_index]
        if current_slime.hp > 0:
            if current_slime.attack(boss):
                print("****やったね！ボスをやっつけました！****")
                break

        # ボスの攻撃
        if boss.attack(current_slime):
            print(f"{current_slime.number}匹目のスライムがやられた")

        # 全てのスライムがやられたらボスの勝利
        if all(slime.hp <= 0 for slime in slimes):
            print("****スライムたちは負けました・・・(TωT)****")
            break

        # 次のスライムに移動
        slime_index = (slime_index + 1) % num_slimes

# ゲームスタート
game_start()
