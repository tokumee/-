#簡単なペイントソフト

import tkinter as tk

color="black"   #デフォルトの色
size=5          #デフォルトサイズ

def myMotion(mouse):
    cv.create_oval(mouse.x - size, mouse.y - size, mouse.x + size, mouse.y + size, fill = color)

def fnc_size_up(event):
    global size
    size=size+1

def  fnc_size_down(event):
    global size
    size=size-1

def fnc_do_1(event):
    global color
    color="black"

def fnc_do_2(event):
    global color
    color="red"

def fnc_do_3(event):
    global color
    color="green"

def fnc_do_4(event):
    global color
    color="yellow"

def fnc_do_5(event):
    global color
    color="blue"

def fnc_do_6(event):
    global color
    color="purple"

def fnc_do_7(event):
    global color
    color="gray"

def fnc_do_8(event):
    global color
    color="pink"

app = tk.Tk()
app.title("Paint soft")
app.geometry("600x600")
cv = tk.Canvas(app, width = 600, height = 400)
cv.create_rectangle(0, 0, 600, 400, fill = "white")
cv.pack()

btn=tk.Button(app,text="☝")   
btn.place(x=10,y=410,width=30,height=30)   
btn.bind("<Button-1>",fnc_size_up)             

btn=tk.Button(app,text="☟")   
btn.place(x=10,y=450,width=30,height=30)   
btn.bind("<Button-1>",fnc_size_down) 

btn=tk.Button(app,text="BLACK",bg="black",fg="white")   #bg -> ボタンの色：fg -> 文字の色
btn.place(x=100,y=500,width=50,height=50)   #ボタンの場所
btn.bind("<Button-1>",fnc_do_1)             #Button-1 -> 右クリック

btn=tk.Button(app,text="RED",bg="red",fg="white")
btn.place(x=150,y=500,width=50,height=50)
btn.bind("<Button-1>",fnc_do_2)

btn=tk.Button(app,text="GREEN",bg="green")
btn.place(x=200,y=500,width=50,height=50)
btn.bind("<Button-1>",fnc_do_3)

btn=tk.Button(app,text="YELLOW",bg="yellow")
btn.place(x=250,y=500,width=50,height=50)
btn.bind("<Button-1>",fnc_do_4)

btn=tk.Button(app,text="BLUE",bg="blue",fg="white")
btn.place(x=300,y=500,width=50,height=50)
btn.bind("<Button-1>",fnc_do_5)

btn=tk.Button(app,text="PURPLE",bg="purple",fg="white")
btn.place(x=350,y=500,width=50,height=50)
btn.bind("<Button-1>",fnc_do_6)

btn=tk.Button(app,text="GRAY",bg="gray",fg="white")
btn.place(x=400,y=500,width=50,height=50)
btn.bind("<Button-1>",fnc_do_7)

btn=tk.Button(app,text="PINK",bg="pink",fg="white")
btn.place(x=450,y=500,width=50,height=50)
btn.bind("<Button-1>",fnc_do_8)

app.bind("<B1-Motion>", myMotion)

app.mainloop()