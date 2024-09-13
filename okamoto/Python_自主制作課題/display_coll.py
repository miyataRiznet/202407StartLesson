"""
コレクションの中身をprintする関数を備えたモジュール
"""

def display_dict(dict):
    for k, v in dict.items():
        print(f'{k}：{v}')