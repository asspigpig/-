def start():
    import pygame as pg
    import pygame as pg
    import screen as sc
    import popout as pop
    import tkinter as tk
    display=sc.screen
    clock=pg.time.Clock()
    screen=display.mode
    fps=60
    pg.init()
    pg.display.set_caption("豬豬大亂鬥")
    icon=pg.image.load(display.icon)
    pg.display.set_icon(icon)
    pg.mouse.set_visible(True)
    pg.display.update()
    class ruc():
        running=True
        def setfa():
            ruc.running=False
            win.destroy()
    while ruc.running:
        clock.tick(fps)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                    win = tk.Tk()
                    win.title('離開')
                    win.geometry('140x130')
                    win.iconbitmap('data/icon/pig.ico')
                    label=tk.Label(win,text="離開")
                    label.grid(row=0,column=0)
                    button=tk.Button(win, text = '取消', command=win.destroy)
                    button.grid(row=1,column=1)
                    btn=tk.Button(win, text = '確定', command=ruc.setfa)
                    btn.grid(row=1,column=0)
                    win.mainloop()
    pg.quit()