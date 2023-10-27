import tkinter as tk
import random
import numpy as np

F = ("Times New Roman", 50)

masu = np.zeros((5, 5), dtype=int)
frame1 = None
frame2 = None
chosen_numbers2 = []

def make():
    global frame1, frame2
    
    if frame2:
        frame2.destroy()
    
    frame1 = tk.Frame(root, width=1050, height=1150, borderwidth=4, relief="groove")
    frame1.pack()
    
    button1 = tk.Button(frame1, text="ビンゴカード作成", width=10, height=2, bg="cyan", command=create_bingo)
    button1.pack()
    
def create_bingo():
    global frame1, frame2, masu, canvas
    
    if frame1:
        frame1.destroy()
    
    frame2 = tk.Frame(root, width=1050, height=1150, borderwidth=4, relief="groove")
    frame2.pack()

    canvas = tk.Canvas(frame2, width=1000, height=1000, borderwidth=0, bg="white")
    canvas.pack()
    
    keisan1()

    masume()

    button2 = tk.Button(frame2, text="戻る", width=10, height=2, bg="red", command=make)
    button2.pack()

def keisan1():            
    for x in range(5):
        a = 1 + x * 15
        b = (x + 1) * 15
        chosen_numbers = []  
        for kai in range(5):
            while True:
                chose = random.randint(a, b)
                if chose not in chosen_numbers:
                    chosen_numbers.append(chose)
                    masu[x][kai] = chose
                    break
                
def masume():
    for x in range(1, 7):
        canvas.create_line(150 * x, 150, 150 * x, 900, fill="gray", width=8)
        canvas.create_line(150, 150 * x, 900, 150 * x, fill="gray", width=8)

    for y in range(5):
        yoko = 375 + (150 * (y - 1))
        for z in range(5):
            n = masu[z][y]
            if y == 2 and z == 2:
                canvas.create_oval(150 * z + 150, yoko-75, 150 * z + 300, yoko+75, fill="blue", width=0)
            else:
                canvas.create_text(150 * z + 225, yoko, text=n, font=F, fill="blue")                    

root = tk.Tk()
root.title("ビンゴカード作成")
root.geometry("1050x1200")
make()
root.mainloop()                