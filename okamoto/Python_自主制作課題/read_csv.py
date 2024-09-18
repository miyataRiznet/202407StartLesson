"""
csvの内容を読み込み、表示させる機能を備えたモジュール
"""

import csv

def read_csv():
    while True:
        with open('data.csv')as f:
            reader = csv.reader(f)
            mybook_title_list = [i[0] for i in reader]
            for i in mybook_title_list:
                print(f'{mybook_title_list.index(i) + 1}.{i}')
        with open('data.csv')as f:
            reader = csv.reader(f)
            book_num = int(input('何番の本を確認しますか？>>>'))
            mybook_list = list(reader)
            for i in mybook_list[book_num - 1]:
                print(i)
        ans3 = input('他にも見ますか？(YES/NO)>>>').upper()
        if ans3 != 'YES':
            exit()