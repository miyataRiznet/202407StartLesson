"""
要件：下記のディクショナリ型を使用し実行例と同じように出力すること
条件：for文を使用すること
data = {"first": "Naomi", "family": "Osaka", "country": "Japan"}
"""

data = {"first":"Naomi", "family":"Osaka", "country": "Japan"}

for k, v in data.items():
    print(f'{k}:{v}')