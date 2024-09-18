"""
メインモジュール
"""

import tkinter as tk
import api_handler
import data_processor
import get_tkinter
import read_csv
import write_border


if __name__ == "__main__":
    ans1 = input('マイ本棚に追加なら「1」、マイ本棚の確認なら「2」を入力してください>>>')
    while True:
        if ans1 == '1':
            root = tk.Tk()
            # インスタンスを生成
            app = get_tkinter.ReadingRecordApp(root, label = 'ISBNを入力してください', entry = True, button = '決定')
            root.mainloop()
            # appのインスタンス変数を代入
            isbn = app.isbn
            # API(書籍情報)を取得
            bookdata = api_handler.get_api(isbn)
            # 取得したデータを辞書として格納
            bookdata_dict = data_processor.assign_data(bookdata)
            # レビューと感想を入力させ、それも格納
            bookdata_dict = data_processor.input_info(bookdata_dict)
            # 登録した内容を表示
            data_processor.display_data(bookdata_dict)
            # csvにデータを追記
            data_processor.append_data(bookdata_dict)
            write_border.write_border()
        elif ans1 != '2':
            print('最初からやり直してください')
            exit()

        ans2 = input('さらに本棚へ追加するなら「1」、本棚を確認するなら「2」、終了するなら「3」を入力してください>>>')
        while True:
            if ans2 == '1':
                break
            elif ans2 == '2':
                # csvを読み込み、過去の登録内容を確認する
                read_csv.read_csv()

            else:
                exit()