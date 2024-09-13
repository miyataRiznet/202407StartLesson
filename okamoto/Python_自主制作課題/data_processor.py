"""
データを処理する関数を備えたモジュール
"""

import csv
import display_coll
import write_border

def assign_data(bookdata):
    # 取得した情報を変数に格納
    bookdata_dict = {}
    bookdata_dict['タイトル'] = bookdata[0]['summary']['title']
    bookdata_dict['著者'] = bookdata[0]['summary']['author']
    bookdata_dict['出版社'] = bookdata[0]['summary']['publisher']
    bookdata_dict['シリーズ'] = bookdata[0]['summary']['series']
    bookdata_dict['ISBN'] = bookdata[0]['summary']['isbn']

    while True:
        print('該当の書籍は以下で間違いないですか?(YES/NO)')
        display_coll.display_dict(bookdata_dict)
        ans = input().upper()
        if ans == 'YES':
            break
        elif ans == 'NO':
            print('最初からやり直してください')
            exit()
        else:
            ('YESかNOを入力してください')

    write_border.write_border()
    return bookdata_dict


def input_info(bookdata_dict):
    # レビュー入力
    while True:
        print('1から5で評価を入力してください>>>')
        point = input()
        if point.isdecimal():
            point = int(point)
            if not 1 <= point <= 5:
                ('入力された値が範囲外です！')
            else:
                write_border.write_border()
                break
        else:
            print('評価ポイントは数字で入力してください')

    # 感想の入力
    thoughts = input('感想を入力してください>>>')
    write_border.write_border()

    # 書籍情報とレビュー、感想を辞書に格納
    bookdata_dict['レビュー'] = f'{"☆" * point}'
    bookdata_dict['感想'] = thoughts
    return bookdata_dict

# 登録内容の出力
def display_data(bookdata_dict):
    print('以下の内容で登録しました。')
    for k, v in bookdata_dict.items():
        print(f'{k}：{v}')

# data.csvに追記（data.csvが無ければ新規に作成し、書き込み）
def append_data(bookdata_dict):
    bookdata_list = list(bookdata_dict.values())

    with open('data.csv', 'a')as f:
        writer = csv.writer(f)  # ファイルオブジェクト渡し、writerオブジェクトを取得
        writer.writerow(bookdata_list)  # 登録内容を書き込み