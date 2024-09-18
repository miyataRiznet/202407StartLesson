## 指定した範囲内で物体を動かせるゲーム

import pygame as pg
from pygame.locals import *
import sys
import random

def main():
    pg.init()                                   # pygameの初期化
    screen = pg.display.set_mode((800, 600))    # 400 x 300の大きさの画面を作る
    pg.display.set_caption("game")              # 画面上部に表示するタイトルを設定

    # キャラクター追加
    alian = pg.image.load("images/alian.png")
    alian = pg.transform.scale(alian, (50, 50))
    alian = pg.transform.flip(alian, True, False)
    alian_rect = pg.rect.Rect(10, 10, 10, 10)

    # 敵キャラクター追加
    ufo = pg.image.load("images/ufo.png")
    ufo = pg.transform.scale(ufo, (100, 100))
    ufo = pg.transform.flip(ufo, True, False)
    ufo_rect = pg.rect.Rect(200, 200, 100, 100)

    while (1):
        screen.fill((0,0,0))        # 画面を黒色に塗りつぶし RGB値

        # キー情報の入力を取得
        pressed_keys =pg.key.get_pressed()
        if pressed_keys[pg.K_LEFT]:
            if alian_rect.x - 5 > 0:
                alian_rect.x -= 5
        elif pressed_keys[pg.K_RIGHT]:
            if alian_rect.x + 5 < 750:  # 画面のY幅 - 動かしたい物体の数値
                alian_rect.x += 5
        elif pressed_keys[pg.K_UP]:
            if alian_rect.y - 5 > 0:
                alian_rect.y -= 5
        elif pressed_keys[pg.K_DOWN]:
            if alian_rect.y + 5 < 550: # 画面のX幅 - 動かしたい物体の数値
                alian_rect.y += 5


        # キャラクター表示
        screen.blit(alian, (alian_rect.x,alian_rect.y))
        #screen.blit(ufo,ufo_rect)

        pg.display.update()     # 画面を更新

        pg.time.Clock().tick(60) # 画面の更新速度(FPS)

         # イベント処理
        for event in pg.event.get():
            if event.type == QUIT:  # 閉じるボタンが押されたら終了
                pg.quit()       # pygamegの終了(画面閉じられる)
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key==K_ESCAPE:
                    pg.quit()       # pgの終了(画面閉じられる)
                    sys.exit()

if __name__ == "__main__":
    main()