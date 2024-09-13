"""
haniwa_barrage

# ゲーム概要
- Enterキーを連打して敵を倒すバトルゲームです。pygameというライブラリを使用して表現しています。
- プログラム起動後、すぐに始まります。

# ゲーム説明
- 敵のHPは [999,999]です。プレイヤーのHPは、[10,000]です。
- プログラムを実行すると、コマンドが表示されますので、矢印キーの上下でコマンドを選び、Enter押下でコマンドが実行されます。

- コマンドは、「たたかう」、「じゅもん」、「にげる」があります。
- 「たたかう」 は、[10,000~20,000] のランダムダメージを与えます。
- 「じゅもん」 は、15%の確率で[60,000~100,000]のランダムダメージを与えますが、失敗すると、[1,000~5,000]のランダムダメージしか与えられません。
- 「にげる」 は、  敵とのバトルをやめて逃走し、プログラムが終了します。

- 敵は1秒経過で攻撃をしてきます、1回で[500~2,000]の攻撃をしてくるので、平均値は1,250です。約8回の攻撃=約8秒経過すると敗北する計算になります。
- 敗北すると、「でなおしてきな」と表示され5秒経過後アプリケーションが終了します。
- 勝利すると、「ハニワを倒した！ プレイヤーの勝利！！ 」と表示され5秒経過後アプリケーションが終了します。

# 難易度
- 難易度は高めに設定されています。
- 必死にEnterキーを押す必要がある難易度です。
- 「たたかう」か「じゅもん」か、どちらを選んで戦うかはセンスです。どちらでも勝利できます。

# 未実装
- 音楽
- スタート画面
- ダメージ時、画面点滅

"""
import pygame
from pygame.locals import *
import sys
import time
import random
import os

"""
# キー入力を待っている状態
def wait_for_key():
        waiting = True
        while waiting:
            pygame.time.Clock().tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    running = False
                if event.type == pygame.KEYUP:
                    waiting = False

# スタート画面の表示
def show_start_screen():
    screen = pygame.display.set_mode((800, 600))
    # ゲームスタート画面
    screen.fill((0, 0, 0))
    # タイトルテキスト
    title = "HANIWA QUEST"
    titlecap = "ハニワを倒せ!"
    # タイトルテキストの表示設定
    font = pygame.font.Font("font/PixelMplus12-Regular.ttf", 20)
    title_text = font.render(title, True, (255, 255, 255))
    title_rect = title_text.get_rect(center=(200, 100))
    titlecap_text = font.render(titlecap, True, (255, 255, 255))
    titlecap_rect = titlecap_text.get_rect(center=(200,200))
    screen.blit(title_text,title_rect)
    screen.blit(titlecap_text,titlecap_rect)
""" 

# 効果音
## errorはかないけど機能しない
def sound_effect(sound):
    se = pygame.mixer.Sound(sound)
    se.play()
    se.set_volume(10)


# 半角文字やintの数値を全角文字にする
def font_wide(number):
    return str(number).translate(str.maketrans({chr(0x0021 + i): chr(0xFF01 + i) for i in range(94)}))

def main():
    pygame.init()  # Pygameの初期化
    
    # カレントディレクトリの取得
    current_dir = os.getcwd()
    # サウンドディレクトリの取得
    sound_folder = os.path.join(current_dir, "sound")
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
    rectX_enemyHP = 540 #550
    rectY_enemyHP = 20
    rectX_playerHP = 600
    rectY_playerHP = 200
    rectY_enemyHP = 20
    rectW_HP = 200 #180
    rectH_HP = 100

    # enemyの表示画像、表示位置
    enemy_image = pygame.image.load("images/ハニワ.png")  # ボスの画像
    enemyX = 100  # ボスのx座標

    # fontの指定とフォントサイズ指示
    font = pygame.font.Font("font/PixelMplus12-Regular.ttf", 20)

    # 色
    white = (255, 255, 255)
    yellow = (255, 255, 0)
    red = (255, 0, 0)
    black = (0, 0, 0)

    # 効果音を出すための初期設定
    #pygame.mixer.quit()
    pygame.mixer.init()

    run = False  # 逃げる
    enemy_HP = 999999   # ハニワのHP
    player_HP = 10000   # プレイヤーのHP
    action_number = 0  # 選択肢の番号
    damage = 0  # ダメージ量表記
    damageY = 0  # ダメージ量表示のY座標

    """
    # fontの指定
    font = pygame.font.Font("font/PixelMplus12-Regular.ttf", 60)
    # タイトルテキストの用意（フォントサイズ60）
    titletext = font.render("ハニワクエスト", True, (255, 255, 255))
    # startテキスト
    font = pygame.font.Font("font/PixelMplus12-Regular.ttf", 30)
    startinfo = font.render("Spaceを押下してゲームスタート", True, (255, 255, 255))
    font = pygame.font.Font("font/PixelMplus12-Regular.ttf", 20)
    """
    time_start = time.time()    # タイムスタンプ

    # メインの繰り返し処理開始
    while (1):
        time_end = time.time()  # タイムスタンプ
        # enemyのHPが0より大きく、タイム計測が10秒を経過していたら
        if enemy_HP > 0 and time_end - time_start > 1.0:
            player_damage = random.randint(500, 2000)
            player_HP -= player_damage
            #sound_effect("") # ダメージ音

            # プレイヤーのHPが0以下の時
            if player_HP <= 0:
                player_HP = 0
                #sound_effect("") # gameover音を流したい
                message = "ハニワ:「でなおしてきな！」 プレイヤーの敗北"

            else:
                message = "ハニワの こうげき プレイヤーに " + font_wide(player_damage) + "のダメージ"

            # タイム計測をリセット
            time_start = time.time()

        # リスト
        colors = [white, white, white]
        colors[action_number] = yellow # 選択肢を黄色に

        screen.fill((0, 0, 0))  # 画面を黒色に塗りつぶし
        screen.blit(enemy_image, (enemyX, 0))  # ハニワの画像表示

        # HPテキスト表示の枠を表示（enemy,player)
        pygame.draw.rect(screen, white, Rect(rectX_enemyHP, rectY_enemyHP, rectW_HP, rectH_HP), 0) # 最後の数値は枠の太さ
        pygame.draw.rect(screen, white, Rect(rectX_playerHP, rectY_playerHP, rectW_HP, rectH_HP), 0)

        # ハニワのHP表示・設定(enemy)
        enemyHP_text = font.render("HP:" + font_wide(enemy_HP), True, black)
        enemyHP_rect = enemyHP_text.get_rect(center=(640, 70))
        screen.blit(enemyHP_text, enemyHP_rect)

        # プレイヤーのHP表示・設定(player)
        playerHP_text = font.render("HP:" + font_wide(player_HP), True, black)
        playerHP_rect = playerHP_text.get_rect(center=(690, 250))
        screen.blit(playerHP_text, playerHP_rect)

        # attackのアニメーション表示
        text_damage = font.render(font_wide(damage), True, red)
        damage_rect = enemyHP_text.get_rect(center=(400, damageY))

        # attack時のダメージアニメーション
        ## ダメージ表記がボスのアイコン上に表示されY座標が時間経過で変化
        if damageY > 50:
            screen.blit(text_damage, damage_rect)
            damageY -= 1

        # 選択肢のウィンドウを表示
        pygame.draw.rect(screen, white, pygame.Rect(rectX_select, rectY_select, rectW_select, rectH_select), 10)

        # 文字描写設定　font.render(text, antialias, color, background=None)
        message_text = font.render(message, True, (255, 255, 255))
        battle_text = font.render("たたかう", True, colors[0])
        spell_text = font.render("じゅもん", True, colors[1])
        run_text = font.render("にげる", True, colors[2])

        screen.blit(message_text, (40, 420))
        screen.blit(battle_text, (45, 450))
        screen.blit(spell_text, (45, 480))
        screen.blit(run_text, (45, 510))

        pygame.display.update()  # 画面を更新

        # 勝敗がついた時= どちらかがHP0のときの終了処理
        if message in ("ハニワ:「でなおしてきな！」 プレイヤーの敗北", "ハニワを倒した！ プレイヤーの勝利！！"):
            time.sleep(5)
            sys.exit()

        # 「にげる」選択時の処理
        if run == True:
            enemyX -= 2 # enemyのx座標が左にズレる
            if enemyX < -400:
                pygame.quit() # pygameの終了
                sys.exit() # プログラムの終了

        pygame.time.Clock().tick(60)    # 60FPS

        # イベント処理
        for event in pygame.event.get():
            # イベント処理
            if event.type == pygame.QUIT:  # 閉じるボタンが押されたら終了
                pygame.quit()  # Pygameの終了(画面閉じられる)
                sys.exit()  # プログラムの終了

            # キー押下された時
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:    # escapeキーか
                    pygame.quit()  # Pygameの終了(画面閉じられる)
                    sys.exit()
                if event.key == pygame.K_DOWN:
                    if action_number == 2:
                        action_number = 0
                    else:
                        action_number += 1
                    sound_effect(os.path.join(sound_folder,"select_se.mp3"))
                elif event.key == pygame.K_UP:
                    if action_number == 0:
                        action_number = 2
                    else:
                        action_number -= 1
                    sound_effect(os.path.join(sound_folder,"select_se.mp3"))

                # エンターキーが押されたとき
                elif event.key == pygame.K_RETURN:
                    # 「にげる」
                    if action_number == 2:
                        #sound_effect("sound/escape.mp3")
                        run = True
                        continue

                    # 「たたかう」
                    elif action_number == 0:
                        sound_effect(os.path.join(sound_folder,"damaged1.mp3"))
                        # hit_pointの計算
                        screen.fill((255,255,255))
                        damage = random.randint(10000, 20000)
                        screen.blit(enemy_image, (enemyX, 0))
                    # 「じゅもん」
                    elif action_number == 1:
                        sound_effect(os.path.join(sound_folder,"magic.mp3"))
                        # hit_pointの計算
                        chant = random.randint(0,100)
                        if chant <= 15 :
                            damage = random.randint(60000, 100000)
                        else:
                            damage = random.randint(1000,5000)
                    enemy_HP -= damage
                    damageY = 200
                    if enemy_HP <= 0:
                        enemy_HP = 0
                        message = "ハニワを倒した！ プレイヤーの勝利！！"
                        #sound_effect("sound/victory.mp3") # 勝利音
                    else:
                        message = "ハニワに " + font_wide(damage) + "の ダメージ"

if __name__ == "__main__":
    main()

