# Gameスライムアタックに関連するモジュール

import random as rnd 
import time

## 決められた強さのBossを生成するクラス
class Boss:
    # Const
    def __init__(self):
        self.set_name()
        self.set_hp()
        self.set_atk()

    # Setter
    def set_name(self):
        self.name='ドラゴン'
    
    def set_hp(self):
        self.hp=300

    def set_atk(self):
        self.atk=30

    # Getter
    def get_name(self):
        return self.name
    
    def get_hp(self):
        return self.hp
    
    def get_atk(self):
        return self.atk

    # ATKmethod
    # slime:    スライムのインスタンス
    # slimehp:  現在のスライムのHP
    # bosshp:   現在のボスのHP
    # 戻り値:   ボスの攻撃によって減ったスライムのHP
    def attack(self,slime,slimehp,bosshp):
        print('--------------------')
        print(f'{self.get_name()}の攻撃!')
        time.sleep(1)

        slimehp = slimehp - self.get_atk()
        print(f'{slime.get_name()}へ{self.get_atk()}のダメージ')
        time.sleep(1)

        print(f'{self.get_name()}のHP:{bosshp}/{slime.get_name()}のHP:{slimehp}')
        print('--------------------\n')
        time.sleep(1)

        return slimehp