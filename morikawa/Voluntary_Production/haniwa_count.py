# ドラクエ風の紙芝居を作成
## space押下で画面遷移していくような動きをします。
### pygameというライブラリを使用して制御している

import pygame as pg
from pygame.locals import *
import sys
import random

import time

def main():
    pg.init()                                   # pgの初期化
    screen = pg.display.set_mode((800, 600))    # 400 x 300の大きさの画面を作る
    pg.display.set_caption("game")              # 画面上部に表示するタイトルを設定


    rect_x = 20 #長方形左上のｘ座標
    rect_y = 400  #長方形左上のy座標
    rect_width = 800 - (rect_x * 2)  #長方形の幅
    rect_height = 600 - (rect_y + 20) #長方形の高さ

    run = False  # 逃げる
    enemy_info = "enemy  HP"
    enemy_HP = 20000  # ハニワのHP
    player_info = "player HP"
    player_HP = 10000
    #action_number = 0  # 選択肢の番号
    damage = 0
    damageY = 0  # ダメージ量表示のY座標

    # 色
    white = (255, 255, 255)
    yellow = (255, 255, 0)
    red = (255, 0, 0)

    # 色リスト
    colors = [white, white, white]
    #colors[action_number] = yellow # 選択肢を黄色に

    # ゲーム開始画面

    # キャラクター追加
    alian = pg.image.load("images/alian.png")
    # alian = pg.transform.scale(alian, (100, 100))
    # alian = pg.transform.flip(alian, True, False)
    # alian_rect = pg.rect.Rect(200, 400, 15, 15)

    # 敵キャラクター追加
    enemy = pg.image.load("images/ハニワ.png")
    enemy = pg.transform.scale(enemy, (400, 400))
    enemy = pg.transform.flip(enemy, True, False)
    enemy_rect = pg.rect.Rect(200, 200, 100, 100)

    # fontの指定
    font = pg.font.Font("font/PixelMplus12-Regular.ttf", 60)
    # タイトルテキストの用意（フォントサイズ60）
    titletext = font.render("ハニワクエスト", True, (255, 255, 255))
    
    # startテキスト
    font = pg.font.Font("font/PixelMplus12-Regular.ttf", 30)
    startinfo = font.render("Spaceを押下してゲームスタート", True, (255, 255, 255))

    # その他テキスト一覧
    font = pg.font.Font("font/PixelMplus12-Regular.ttf", 25)
    text00 = font.render("Space押下で次に進む、選択", True, (255,255,255))
    font = pg.font.Font("font/PixelMplus12-Regular.ttf", 30)
    text01 = font.render("エンカウント！", True, (255,255,255))
    bossinfo = font.render("ハニワが現れた！", True, (255, 255, 255))
    text02 = font.render("ハニワへ攻撃!", True, (255, 255, 255))
    text03 = font.render(f"ハニワへ{damage}のダメージ", True, (colors[0]))
    x, y = 0, 0
    count = 0

    while (1):
        pg.init()
        screen.fill((0,0,0))        # 画面を黒色に塗りつぶし RGB値

        # ゲームスタート画面の表示
        if count==0:
            screen.blit(titletext, (200, (200 /2)))
            screen.blit(startinfo, (200, (400 /2)))
            #pg.draw.rect(screen,(255, 255, 255),pg.Rect(rect_x, rect_y, rect_width, rect_height), 10)
            pg.display.update()

        # 枠線の表示
        # 下部テキスト枠
        pg.draw.rect(screen,(255, 255, 255),pg.Rect(rect_x, rect_y, rect_width, rect_height), 10)
        # 敵HP枠
        pg.draw.rect(screen,(255, 255, 255),pg.Rect(640, 35, 150, 80), 5)
        # プレイヤーHP枠
        pg.draw.rect(screen,(255, 255, 255),pg.Rect(640, 165, 150, 80), 5)

        # キー情報の入力を取得

        # HP表示
        enemy_info_text = font.render(enemy_info, True, colors[0])
        enemy_HP_text = font.render(str(enemy_HP), True, colors[0])
        player_info_text = font.render(player_info, True, colors[0])
        player_HP_text = font.render(str(player_HP), True, colors[0])
        
        screen.blit(enemy_info_text, (650, 40))
        screen.blit(enemy_HP_text, (700, 70))
        screen.blit(player_info_text, (650, 170))
        screen.blit(player_HP_text, (700, 200))
        

        pg.time.Clock().tick(60) # 画面の更新速度(FPS)

         # イベント処理
        for event in pg.event.get():
            if event.type == QUIT:  # 閉じるボタンが押されたら終了
                pg.quit()       # pgの終了(画面閉じられる)
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key==K_ESCAPE:
                    pg.quit()       # pgの終了(画面閉じられる)
                    sys.exit()
                elif event.key==K_SPACE:
                    count += 1
                    if count == 1: # エンカウント
                        screen.fill((0,0,0))
                        pg.draw.rect(screen,(255, 255, 255),pg.Rect(20, 400, 760, 180), 10)
                        screen.blit(text01,(40,420))
                        screen.blit(text00,(460,360))
                        pg.display.update()
                    if count == 2: # ハニワがあらわれた！
                        screen.blit(enemy, (400-(400 / 2),0))
                        screen.blit(bossinfo,(40, (420)))
                        screen.blit(text00,(460,360))
                        pg.display.flip()
                    if count == 3: # ハニワへ攻撃
                        screen.blit(enemy, (400-(400 / 2),0))
                        screen.blit(text02,(40, 420)) # ハニワへ攻撃!
                        screen.blit(text00,(460,360)) # help
                        pg.display.update()
                    if count == 4:
                        screen.blit(enemy, (400-(400 / 2),0))
                        damage = random.randint(3000,10000)
                        enemy_HP -= damage
                        text03 = font.render(f"ハニワへ{damage}のダメージ", True, (colors[0]))
                        screen.blit(text03,(40, 420)) # ハニワへdamege
                        screen.blit(text00,(460,360)) # help
                        pg.display.update()



if __name__ == "__main__":
    main()