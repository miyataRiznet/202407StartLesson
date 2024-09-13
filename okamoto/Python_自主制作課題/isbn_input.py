"""
ISBNの入力機能を備えたモジュール
"""

def input_isbn(isbn):
    # isbn = input('ISBNを入力してください>>>')
    isbn = isbn.replace('-', '')
    return isbn