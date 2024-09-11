"""条件：
1.	スライムの生成数はユーザーが入力した数字を使用
2.	ボスが死ぬまで、スライムの1匹目~n匹目まで攻撃を続ける
3.	最後にボスが生きていたらボスの勝ち。スライムが生きていた場合はスライムの勝ち
4.	SlimeクラスとBossクラスを作成すること
"""

import random

# Bossクラスの設定
class Boss():
    def __init__(self):
        self.boss_life = 1000
        self.boss_atk = 300

# Slimeクラスの設定
class Slime():
    def __init__(self, i):
        self.slime_name = f'スライム{i}'  # スライムの名前を決定
        self.slime_level = random.randint(1, 100)  # スライムのレベルを決定
        self.slime_life = self.slime_level * 10 + random.randint(-9, 10)  # レベルを基にHPを決定
        self.slime_atk = round(self.slime_level * 1.5)  # レベルを基に攻撃力を決定

# 罫線を引く関数
def write_line():
    print('-----------------------------')
    print('-----------------------------')

# バトル(HPの変動やメッセージの表示など)に関する処理
def battle(slime_list, boss):
    for slime in slime_list:
        if boss.boss_life <= 0:
            print('スライムの勝ちです！')
            break
        for i in range(4):  # ボスの攻撃は多くて4回食らえば必ず負けるためrange(4)
            boss.boss_life -= slime.slime_atk  # ボスのHPをスライムの攻撃力分削る
            print(f'{slime.slime_name}(level:{slime.slime_level})の攻撃！')
            print(f'ボスに{slime.slime_atk}のダメージ！')
            print(f'ボスのHP：{max(0, boss.boss_life)} | {slime.slime_name}のHP：{max(0, slime.slime_life)}')
            write_line()
            if boss.boss_life <= 0:
                break
            slime.slime_life -= boss.boss_atk  # スライムのHPをボスの攻撃力分削る
            print('ボスの攻撃！')
            print(f'{slime.slime_name}に{boss.boss_atk}のダメージ！')
            print(f'{slime.slime_name}のHP：{max(0, slime.slime_life)}')
            if slime.slime_life <= 0:
                print(f'{slime.slime_name}が死亡しました')
                write_line()
                break
            write_line()
    else:
        print('スライムの負けです・・・')

# ボスのインスタンス生成
def get_boss_status():
    boss = Boss()
    print('ボスがあらわれた！')
    return boss

# スライムインスタンス生成
def get_slime_status(slime_num):
    slime_list = []

    for i in range(1, slime_num + 1):
        slime = Slime(i)  # インスタンスを生成してリストに保持
        print(f'{slime.slime_name}　レベル：{slime.slime_level}, HP：{slime.slime_life}, 攻撃力：{slime.slime_atk}')
        slime_list.append(slime)

    return slime_list

# メイン
def main():
    slime_num = int(input('戦わせるスライムの匹数を決めてください(1~10)>>>'))

    if not slime_num in range(1, 11):
        print('1から10までの数を入力してください！')
        exit()

    slime_list = get_slime_status(slime_num)
    boss = get_boss_status()
    battle(slime_list, boss)


main()