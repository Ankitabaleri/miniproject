from tkinter import *
import tkinter.messagebox
root=Tk()
root.title("Tic-Tac-Toe")
root.resizable(0,0)
b=[]
#c=count 
c=0
def checkwinx():
    global c
    w=0
    if((b[0])['text']=='X' and (b[1])['text']=='X' and b[2]['text']=='X'):
      w=1
    elif(b[3]['text']=='X' and b[4]['text']=='X' and b[5]['text']=='X'):
      w=1
    elif(b[6]['text']=='X' and b[7]['text']=='X' and b[8]['text']=='X'):
      w=1
    elif(b[0]['text']=='X' and b[3]['text']=='X' and b[6]['text']=='X'):
      w=1
    elif(b[1]['text']=='X' and b[4]['text']=='X' and b[7]['text']=='X'):
      w=1
    elif(b[2]['text']=='X' and b[5]['text']=='X' and b[8]['text']=='X'):
      w=1
    elif(b[0]['text']=='X' and b[4]['text']=='X' and b[8]['text']=='X'):
      w=1
    elif(b[2]['text']=='X' and b[4]['text']=='X' and b[6]['text']=='X'):
      w=1
    if(w==0 and c==8):
      tkinter.messagebox.showinfo("Draw","Draw!!!!")
      root.destroy()
      exit(0)
    if(w==1):
      tkinter.messagebox.showinfo("Player1","Player1 won!")
      root.destroy()
      exit(0)
def checkwiny():
    global c
    w=0
    if((b[0])['text']=='O' and (b[1])['text']=='O' and b[2]['text']=='O'):
      w=1
    elif(b[3]['text']=='O' and b[4]['text']=='O' and b[5]['text']=='O'):
      w=1
    elif(b[6]['text']=='O' and b[7]['text']=='O' and b[8]['text']=='O'):
      w=1
    elif(b[0]['text']=='O' and b[3]['text']=='O' and b[6]['text']=='O'):
      w=1
    elif(b[1]['text']=='O' and b[4]['text']=='O' and b[7]['text']=='O'):
      w=1
    elif(b[2]['text']=='O' and b[5]['text']=='O' and b[8]['text']=='O'):
      w=1
    elif(b[0]['text']=='O' and b[4]['text']=='O' and b[8]['text']=='O'):
      w=1
    elif(b[2]['text']=='O' and b[4]['text']=='O' and b[6]['text']=='O'):
      w=1
    if(w==1):
      tkinter.messagebox.showinfo("Player2","Player2 won!")
      root.destroy()
      exit(0)
  
def click(num):
    global b
    global c
    if(c%2==0):
     if((b[num])['text']!="X" and (b[num])['text']!="O"):
      b[num].configure(text="X")
      checkwinx()
      c=c+1
    else:
     if((b[num])['text']!="X" and (b[num])['text']!="O"):
      b[num].configure(text="O")
      checkwiny()
      c=c+1
b1=Button(root,command=lambda:click(0))
b1.configure(height=5,width=5)
b1.grid(row=0,column=0)
b2=Button(root,command=lambda:click(1))
b2.configure(height=5,width=5)
b2.grid(row=0,column=1)
b3=Button(root,command=lambda:click(2))
b3.configure(height=5,width=5)
b3.grid(row=0,column=2)
b4=Button(root,command=lambda:click(3))
b4.configure(height=5,width=5)
b4.grid(row=1,column=0,sticky=W)
b5=Button(root,command=lambda:click(4))
b5.configure(height=5,width=5)
b5.grid(row=1,column=1)
b6=Button(root,command=lambda:click(5))
b6.configure(height=5,width=5)
b6.grid(row=1,column=2)
b7=Button(root,command=lambda:click(6))
b7.configure(height=5,width=5)
b7.grid(row=2,column=0)
b8=Button(root,command=lambda:click(7))
b8.configure(height=5,width=5)
b8.grid(row=2,column=1)
b9=Button(root,command=lambda:click(8))
b9.configure(height=5,width=5)
b9.grid(row=2,column=2)
b=[b1,b2,b3,b4,b5,b6,b7,b8,b9]
root.mainloop()
