"""
API取得機能を備えたモジュール
"""

import json
import urllib
import urllib.request

def get_api(isbn):
    # 入力されたISBNを基にURLを生成
    url = f'https://api.openbd.jp/v1/get?isbn={isbn}'

    # API取得の処理
    req = urllib.request.Request(url)  # URLからRequestオブジェクトを作成
    urlopen = urllib.request.urlopen(url)  # Requestをurlopenに渡し、URLの内容を取得
    bookdata = json.loads(urlopen.read())  # 取得した情報をリストに変換
    return bookdata