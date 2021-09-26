import pygame as pg


def get(text):
    import tkinter as tk
    root = tk.Tk()
    root.geometry("400x240")
    root.title('得到')
    root.attributes('-topmost', True)
    root.iconbitmap('data/icon/pig.ico')
    label = tk.Label(root,text = f'得到{text}')  # 顯示文字
    label.pack()

    button2=tk.Button(root, text = '關閉', command=root.destroy)
    button2.pack()
    root.mainloop()
def getcoin(money):
    import tkinter as tk
    root = tk.Tk()
    root.geometry("400x240")
    root.title('得到')
    root.attributes('-topmost', True)
    root.iconbitmap('data/icon/pig.ico')
    label = tk.Label(root,text = f'得到豬幣x{money}')  # 顯示文字
    label.pack()

    button2=tk.Button(root, text = '關閉', command=root.destroy)
    button2.pack()
    root.mainloop()
