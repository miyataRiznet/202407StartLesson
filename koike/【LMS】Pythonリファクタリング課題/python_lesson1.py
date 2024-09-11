def main_menu():

    while True:
        print('実施したい処理を選択してください')
        print('1:評価ポイントとコメントを入力する')
        print('2:今までの結果を確認する')
        print('3:終了する')
        num = input()

        if num.isdecimal():
            num = int(num)
            if num == 1:
                add_evaluation()
            elif num == 2:
                show_results()
            elif num == 3:
                print('終了します')
                break
            else:
                print('1から3で入力してください')
        else:
            print('1から3で入力してください')

def add_evaluation():
    while True:
        print('1から5で評価を入力してください')
        point = input()
        if point.isdecimal():
            point = int(point)
            if 1 <= point <= 5:
                print('コメントを入力してください')
                comment = input()
                post = f'ポイント: {point} コメント: {comment}'
                with open("data.txt", 'a') as file_pc:
                    file_pc.write(f'{post}\n')
                print('評価を保存しました')
                break
            else:
                print('1から5で入力してください')
        else:
            print('評価ポイントは数字で入力してください')

def show_results():
    print('これまでの結果')
    try:
        with open("data.txt", "r") as read_file:
            print(read_file.read())
    except FileNotFoundError:
        print("結果がまだありません")
        
# プログラム実行
main_menu()