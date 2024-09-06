"""
要件：下記のディクショナリ型を使用し実行例と同じように出力すること
条件：for文を使用すること
data = {"first": "Naomi", "family": "Osaka", "country": "Japan"}
"""
# dictionaryでデータ宣言・初期化
data = {"first": "Naomi", "family": "Osaka", "country": "Japan"}
# for文を使用し、タプルで取得・表示
for key,value in data.items():
    print(f'{key}:{value}')