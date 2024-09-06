"""
要件：下記のセットを使用し実行例と同じになるようにコードを作成すること
player1={'読書','昼寝','映画鑑賞','散歩','料理'}
player2={'テニス','将棋','料理','読書','旅行'} 
"""

player1 = {'読書', '昼寝', '映画鑑賞', '散歩', '料理'}
player2 = {'テニス', '将棋', '料理', '読書', '旅行'}

union_elem_count = len(player1 | player2)  # 和集合の要素数
intersection_elem_count = len(player1 & player2)  # 積集合の要素数
answer = 100 / (union_elem_count / intersection_elem_count)  # 和集合に対する積集合の割合(%)を算出

input('心の準備が出来たらEnterキーを押してください>>>')

print(f'相性度は{answer}%でした♡')