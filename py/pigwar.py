import tkinter as tk
import game
i="\n"*40
w="."*30
o=(w+"\n")*10
gameinfo="西元後20年,豬豬星遭到敵人的攻擊,這個攻擊非常猛烈。就在豬豬星快要滅絕的時候\n出現了一個英雄-[獨眼泰迪熊]。他用他的法力控制了敵人的攻擊。過了十年, 獨眼泰迪熊的法力慢慢地減少。就在他的法力用完的那一刻,他,也遭到了封印"+o+"\n現在你就是豬豬均團的將軍,你得救出獨眼泰迪熊,並且打敗敵人。\n遊戲!\n現在開始！"

root = tk.Tk()
class cmd():
    def strt():
        root.destroy()
        game.start()
    def about():
        win = tk.Tk()
        win.title('豬豬大亂鬥')
        win.geometry('1280x800')
        win.iconbitmap('data/icon/pig.ico')
        label = tk.Label(win,text = gameinfo)  # 顯示文字
        label.pack()
        button4=tk.Button(win, text = '關閉', command=win.destroy)
        button4.pack()
        win.mainloop()
    def tour():
        pass
    def full():
        root.attributes('-fullscreen', True)
        set.button5.configure(text = "取消全螢幕", command=cmd.fuli) 
    def fuli():
        root.attributes('-fullscreen', False)
        set.button5.configure(text = "全螢幕", command=cmd.full)
class set():
        root.title('豬豬大亂鬥')
        root.geometry('1280x800')
        root.iconbitmap('data/icon/pig.ico')
        button = tk.Button(root, text = '開始遊戲', command=cmd.strt)
        button.pack()
        button2 = tk.Button(root, text = '遊戲玩法', command=cmd.tour)
        button2.pack()
        button3 = tk.Button(root, text = '遊戲簡介', command=cmd.about)
        button3.pack()
        button4=tk.Button(root, text = '關閉遊戲', command=root.destroy)
        button4.pack()
        button5=tk.Button(root, text = '全螢幕', command=cmd.full)
        button5.pack()
set
root.mainloop()