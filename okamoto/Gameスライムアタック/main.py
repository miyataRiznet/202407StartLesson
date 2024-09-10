import sys
import tkinter as tk
import random

class Slime():
    def __init__(self):
        self.slime_level = 1
        self.slime_life = 1
        self.slime_atk = 1

    def get_level(self):
        self.slime_level = random.randint(1, 100)
        return self.slime_level
    
    def get_life(self):
        self.slime_life = self.get_level() * 10 + random.randint(-9, 10)
        return self.slime_life

    def get_atk(self):
        self.slime_atk = round(self.get_level() * 1.5)
        return self.slime_atk


def start_game():
    slime_num = int(entry_slime_num.get())
    if slime_num > 10:
        print('Please enter a number from 1 to 10！')
        exit()

    slime_dict = {}
    status_dict = {}
    # slime = []

    for i in range(1, slime_num + 1):
        
        slime = Slime()  # インスタンスを生成
        print(slime)
        status_dict['level'] = slime.get_level()
        status_dict['life'] = slime.get_life()
        status_dict['atk'] = slime.get_atk()
        
        slime_dict[f'スライム{i}'] = status_dict
        # f'slime{i}' = Slime()
        # f'slime{i}'.get_level()
        # f'slime{i}'.get_life()
        # f'slime{i}'.get_atk()
    print(slime_dict)
    



# def main(self):
root = tk.Tk()
root.title('Game Slime Attack')
root.geometry('1280x720')

label_slime_num = tk.Label(text = 'How many slimes do you call up (1~10) ?', anchor = tk.CENTER)
label_slime_num.pack()

entry_slime_num = tk.Entry()
entry_slime_num.pack()

button_determining = tk.Button(text = 'OK！', command = start_game)
button_determining.pack()

root.mainloop()

# root.destroy()


# if __name__ == '__main__':
#     main()