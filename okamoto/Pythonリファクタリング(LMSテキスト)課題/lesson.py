def review():
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


def display_result():
    print('これまでの結果')
    read_file = open("data.txt", "r")
    print( read_file.read() )
    read_file.close()


while True:
    print('実施したい処理を選択してください')
    print('1:評価ポイントとコメントを入力する')
    print('2:今までの結果を確認する')
    print('3:終了する')
    num = input()
    
    if num.isdecimal():
        num = int(num)
        if num == 1:
            review()
        elif num == 2:
            display_result()
        elif num == 3:
            print('終了します')
            break
        else:
            print('1から3で入力してください')