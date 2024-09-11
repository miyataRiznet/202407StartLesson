# Gameスライムアタックに関連するモジュール

import random as rnd # ランダムでHPやATKを決定するために使用
import time

## ユーザー入力値でスライムを生成するクラス
### ランダムに　HP　と　ATK　を決定
class Slime:
    # Const
    def __init__(self, num):
        self.set_name(num)
        self.set_hp()
        self.set_atk()

    # Setter
    def set_name(self,i):
        self.name=f'{i+1}匹目のスライム'
    
    def set_hp(self):
        self.hp=rnd.randint(30,100)

    def set_atk(self):
        self.atk=rnd.randint(1,10) * 3

    # Getter
    def get_name(self):
        return self.name
    
    def get_hp(self):
        return self.hp
    
    def get_atk(self):
        return self.atk
    
    # ATKmethod
    # slimehp:  現在のスライムのHPを表示
    # bosshp:   現在のボスのHPを表示
    # 戻り値:   スライムの攻撃によって減ったボスのHP    
    def slime_attack(self,boss,slimehp,bosshp):
        print('--------------------')
        print(f'{self.get_name()}の攻撃!')
        time.sleep(1)

        # criticalメソッドにより攻撃力が増えるか判定
        if self.critical():
            bosshp = bosshp - int(self.get_atk() * 1.5)
            print('会心の一撃!!!')
            time.sleep(1)
            print(f'{boss.get_name()}へ{int(self.get_atk() * 1.5)}のダメージ',flush=True)
            time.sleep(1)
        else: # 通常ダメージ
            bosshp = bosshp - self.get_atk()
            print(f'{boss.get_name()}へ{self.get_atk()}のダメージ')
            time.sleep(1)
        
        # HPの変化を表示
        print(f'{boss.get_name()}のHP:{bosshp}/{self.get_name()}のHP:{slimehp}',flush=True)
        print('--------------------\n')
        time.sleep(1)

        return bosshp
    
    # スライムのHPが無くなった時の表示を行う
    def down(self):
        print('--------------------')
        print(f'{self.get_name()}が気絶!')
        print('--------------------\n')
        time.sleep(1)

    # 約30%で、Trueを返す
    # 会心の一撃を表現したい時に使用
    def critical(self):
        # 0.0 ~ 1.0の値をランダムに取得し代入
        crit = rnd.random()
        if crit >= 0.7:
            return True
        else:
            return False