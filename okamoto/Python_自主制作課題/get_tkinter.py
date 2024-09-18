"""
Tkinterインスタンスを生成するモジュール
"""

import tkinter as tk
import isbn_input

class ReadingRecordApp:
    def __init__(self, root, label = None, entry = None, button = None):
        self.root = root
        self.root.title("Reading Record App")
        self.root.geometry("1280x800")
        self.isbn = 0

        if not label is None:
            self.label1 = tk.Label(text = label, font = ('', '30'))
            self.label1.pack(pady = (100, 0))

        if not entry is None:
            self.entry1 = tk.Entry(font =('', '20'))
            self.entry1.pack(padx = 100, pady = 50, ipadx = 100, ipady = 20)

        if not button is None:
            self.button1 = tk.Button(text = button, width = 10, height = 2, font = ('', '20'), command = self.get_isbn)
            self.button1.pack()

    def get_isbn(self):
        self.isbn = isbn_input.input_isbn(self.entry1.get())
        self.root.destroy()