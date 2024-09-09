player1={'読書','昼寝','映画鑑賞','散歩','料理'}
player2={'テニス','将棋','料理','読書','旅行'}

hobbys = len(player1 | player2) #趣味をカウント
common = len(player1 & player2) #共通項をカウント

input("心の準備が出来たらEnterキーを押してください>>>")
print(f'相性度は{common / hobbys * 100}%でした♡')