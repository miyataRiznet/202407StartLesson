# LMS_pythonリファクタリングの課題

"""
合格要件
1.新たにメソッドを定義し、処理が分割されていること
2.メソッド名は処理と関係のある命名がなされていること
3.実施する処理の選択で1から3以外を入力した際、”1から3で入力してください”というメッセージが表示され、再度選択させる処理が実行されること
4.評価ポイントの入力で1から5以外を入力した場合、”1から5で入力してください”というメッセージが表示され、再度評価ポイントを入力させる処理が実行されること
5.評価ポイントとコメントが入力できること
6.今までの結果を確認できること
7.処理を終了できること
"""

# 評価値とコメントを入力するメソッド
def review_comment():
    while True:
        print('1から5で評価を入力してください')
        point = input()
        if point.isdecimal():
            point = int(point)
            if  point <= 0 or point > 5: # 0以下または5より大きいという条件式
                print('1から5で入力してください')
            else:
                print('コメントを入力してください')
                comment = input()
                post = f'ポイント: {point} コメント: {comment}'
                file_pc = open("data.txt", 'a')
                file_pc.write(f'{ post } \n')
                file_pc.close()
                break
        else:
            print('評価ポイントは数字で入力してください')

# 評価とコメントの入力履歴を参照するメソッド
def show_review():
    print('これまでの結果')
    read_file = open("data.txt", "r")
    print( read_file.read() )
    read_file.close()

# Main
while True:
    print('実施したい処理を選択してください')
    print('1:評価ポイントとコメントを入力する')
    print('2:今までの結果を確認する')
    print('3:終了する')
    num = input()

    if num.isdecimal():
        num = int(num)
        if num == 1:
            review_comment()
        elif num == 2:
            show_review()
        elif num == 3:
          print('終了します')
          break
        else:
            print('1から3で入力してください')
    else:
        print('1から3で入力してください')