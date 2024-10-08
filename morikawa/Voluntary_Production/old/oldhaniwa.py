import pygame
from pygame.locals import *
import sys
import time
import random

"""
# 効果音
def sound_effect(sound):
    se = pygame.mixer.Sound(sound)
    se.play()
"""

# 半角文字を全角にし、DragonQuestFC.tffに対応させる
def dq_font(number):
    return str(number).translate(str.maketrans({chr(0x0021 + i): chr(0xFF01 + i) for i in range(94)}))

def main():
    pygame.init()  # Pygameの初期化
    screen = pygame.display.set_mode((800, 600))  # 400 x 300の大きさの画面を作る
    pygame.display.set_caption("HANIWA-QUEST")  # 画面上部に表示するタイトルを設定

    # 選択肢ボックスの引数
    rectX_select = 20  # 長方形左上のｘ座標
    rectY_select = 400  # 長方形左上のｘ座標
    rectW_select = 800 - (rectX_select * 2)  # 長方形の幅
    rectH_select = 600 - (rectY_select + 20)  # 長方形の高さ

    # 選択ボックス内テキスト
    message = "ハニワが あらわれた！"
    # HPボックスの引数
    rectX_enemyHP = 550
    rectY_enemyHP = 20
    rectX_playerHP = 600
    rectY_playerHP = 200
    rectY_enemyHP = 20
    rectW_HP = 180
    rectH_HP = 100

    enemy_image = pygame.image.load("images/ハニワ.png")  # ボスの画像
    enemyX = 100  # ボスのx座標

    font = pygame.font.Font("font/PixelMplus12-Regular.ttf", 20)

    # 色
    white = (255, 255, 255)
    yellow = (255, 255, 0)
    red = (255, 0, 0)

    # 効果音
    pygame.mixer.init()

    run = False  # 逃げる
    enemy_HP = 530000  # ハニワのHP
    player_HP = 10000
    action_number = 0  # 選択肢の番号
    damage = 0
    damageY = 0  # ダメージ量表示のY座標

    # タイムスタート計測
    time_start = time.time()

    # メインの繰り返し処理開始
    while (1):
        time_end = time.time()
        if enemy_HP > 0 and time_end - time_start > 10.0:
            player_damage = random.randint(8000, 10000)
            player_HP -= player_damage
            ##sound_effect("sound/battle.mp3")
            if player_HP <= 0:
                player_HP = 0
                ##sound_effect("sound/gameover.mp3")
                message = "ハニワ:でなおしてきな！"

            else:
                message = "ハニワの こうげき プレイヤーに " + dq_font(player_damage) + "のダメージ"

            time_start = time.time()

        # リスト:
        colors = [white, white, white]
        colors[action_number] = yellow

        screen.fill((0, 0, 0))  # 画面を黒色に塗りつぶし
        screen.blit(enemy_image, (enemyX, 0))  # スライムの画像表示

        # HPテキスト表示の枠を表示
        pygame.draw.rect(screen, white, Rect(rectX_enemyHP, rectY_enemyHP, rectW_HP, rectH_HP), 10)
        pygame.draw.rect(screen, white, Rect(rectX_playerHP, rectY_playerHP, rectW_HP, rectH_HP), 10)

        # スライムのHP表示
        enemyHP_text = font.render("ＨＰ：" + dq_font(enemy_HP), True, white)
        enemyHP_rect = enemyHP_text.get_rect(center=(640, 70))
        screen.blit(enemyHP_text, enemyHP_rect)

        # プレイヤーのHP表示
        playerHP_text = font.render("ＨＰ：" + dq_font(player_HP), True, white)
        playerHP_rect = playerHP_text.get_rect(center=(690, 250))
        screen.blit(playerHP_text, playerHP_rect)

        # attackのアニメーション表示
        text_damage = font.render(dq_font(damage), True, red)
        damage_rect = enemyHP_text.get_rect(center=(400, damageY))

        if damageY > 50:
            screen.blit(text_damage, damage_rect)
            damageY -= 1

        # 選択しのウィンドウを表示
        pygame.draw.rect(screen, white, Rect(rectX_select, rectY_select, rectW_select, rectH_select), 10)
        message_text = font.render(message, True, (255, 255, 255))
        battle_text = font.render("たたかう", True, colors[0])
        spell_text = font.render("じゅもん", True, colors[1])
        run_text = font.render("にげる", True, colors[2])

        screen.blit(message_text, (40, 420))
        screen.blit(battle_text, (45, 450))
        screen.blit(spell_text, (45, 480))
        screen.blit(run_text, (45, 510))

        pygame.display.update()  # 画面を更新

        # HP0のときの終了処理
        if message in ("ハニワ:でなおしてきな！", "ハニワをたおした！ プレイヤーの勝利！！"):
            time.sleep(6)
            sys.exit()

        if run == True:
            enemyX -= 2
            if enemyX < -400:
                pygame.quit()
        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  # 閉じるボタンが押されたら終了
                pygame.quit()  # Pygameの終了(画面閉じられる)
                sys.exit()

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()  # Pygameの終了(画面閉じられる)
                    sys.exit()
                if event.key == K_DOWN:
                    if action_number == 2:
                        action_number = 0
                    else:
                        action_number += 1
                    #sound_effect("sound/select_se.mp3")
                elif event.key == K_UP:
                    if action_number == 0:
                        action_number = 2
                    else:
                        action_number -= 1
                    #sound_effect("sound/select_se.mp3")

                # エンターキーが押されたとき
                elif event.key == K_RETURN:
                    # 「にげる」
                    if action_number == 2:
                        #sound_effect("sound/run.mp3")
                        run = True
                        continue

                    # 「たたかう」
                    elif action_number == 0:
                        #sound_effect("sound/battle.mp3")
                        # hit_pointの計算
                        damage = random.randint(10000, 30000)

                    # 「じゅもん」
                    elif action_number == 1:
                        #sound_effect("sound/spell.mp3")
                        # hit_pointの計算
                        damage = random.randint(30000, 50000)

                    enemy_HP -= damage
                    damageY = 200
                    if enemy_HP <= 0:
                        enemy_HP = 0
                        message = "ハニワを倒した！ プレイヤーの勝利！！"
                        #sound_effect("sound/victory.mp3")
                    else:
                        message = "ハニワに " + dq_font(damage) + "の ダメージ"

if __name__ == "__main__":
    main()

