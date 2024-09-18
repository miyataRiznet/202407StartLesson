import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import time

# アカウント認証処理
my_id = '7c558563229749db87eea2d3b95dc8b2'  # client ID
my_secret = 'b3b34a9e2cac42349b4cf9b2af773fa1'  # client secret
ccm = SpotifyClientCredentials(client_id=my_id, client_secret=my_secret)
spotify = spotipy.Spotify(client_credentials_manager=ccm, language='ja')

# 曲全体のキー(音階)のクラス ※ピッチクラス表記法に準拠
pitch_class = {0: 'C', 1: 'C#', 2: 'D', 3: 'D#', 4: 'E', 5: 'F',
               6: 'F#', 7: 'G', 8: 'G#', 9: 'A', 10: 'A#', 11: 'B'}
mode_dec = {0: 'Minor', 1: 'Major'}

while True:
    # 曲のURLを入力
    track_url = input("【Spotifyの共有リンクを入力で、練習やセッション等に役立つ楽曲の情報をお調べします】\n")

    # 楽曲情報の取得
    track_data = spotify.track(track_url)
    time.sleep(1)  # アクセス負荷軽減のため1秒停止
    results = spotify.audio_features(track_url)
    result = results[0]

    # 楽曲のキーとモード
    pitch = pitch_class[result['key']]
    mode_m = mode_dec[result['mode']]  # マイナーもしくはメジャー

    # 曲の長さ(ミリ秒→秒→分)
    track_ms = result['duration_ms']
    track_s = track_ms / 1000
    track_min = track_s // 60
    track_min_sec = track_s - 60 * track_min

    # 楽曲情報の出力
    print()  # 改行
    print('artist      :  ' + track_data['album']['artists'][0]['name'])  # アーティスト名
    print('track       :  ' + track_data['name'])  # 曲名
    print('album       :  ' + track_data['album']['name'])  # 収録作品名
    print(f'length      :  {int(track_min)} min {track_min_sec:.1f} sec')  # 曲の長さ(分：秒)
    print('key         :  ' + pitch + ' ' + mode_m)  # 曲全体のキー(音階)
    print('tempo(BPM)  :  ' + str(result['tempo']))  # 曲全体の推定テンポ数
    print('beat        :  ' + str(result['time_signature']))  # 1小節あたりの拍数
    print('volume(dB)  :  ' + str(result['loudness']))  # 今日の平均音量(-60～0dB)
    print('danceability:  ' + str(result['danceability']))  # 踊りやすさを0.0～1.0で表した指標(1に近いほど踊りやすい)
    print()  # 改行

    # 各項目の説明を表示するか確認
    explain = input("【各項目の説明を表示しますか？(y/n)】\n")

    if explain.lower() == 'y':
        # 項目と説明
        print("""
        artist      :  アーティスト名
        track       :  曲名
        album       :  収録作品名
        length      :  曲の長さ(分：秒)
        key         :  曲全体のキー(音階)
        tempo(BPM)  :  曲全体の推定テンポ数
        beat        :  1小節あたりの拍数
        volume(dB)  :  曲全体の平均音量(-60～0dB) 
                       ※ 楽曲ごとの音量差を緩和する際の目安などにご活用ください
        danceability:  テンポ・リズムの安定性・ビートの強さなどから計算された、
                       踊りやすさを0.0～1.0で表した指標(1に近いほど踊りやすい)
        """)

    # ほかの曲も調べるか確認
    again = input('【ほかの曲もお調べしますか？(y/n)】\n')
    if again.lower() != 'y':
        print("【それではまた…音楽を楽しみましょう！】")
        break