from tkinter import *
import tkinter.messagebox

#Screen Setup
wn=Tk()
wn.title('TIC-TAC-TOE v1.0')
wn.config(background='pale green',bd=5)

#Player Name
player1=Entry(wn,bd=5,bg='powder blue',fg='Red',disabledforeground="red",disabledbackground="powder blue",width=22)
player1.grid(sticky=W,row=1, column=1,columnspan=8)
player2=Entry(wn,bd=5,bg='powder blue',fg='Red',disabledforeground="red",disabledbackground="powder blue",width=22)
player2.grid(sticky=W,row=2, column=1,columnspan=8)
pa='Player 1'
pb='Player 2'

#Label for Player Screen
lab1=Label(wn,text='Player 1: ',font=("consolas",13,'bold'),bg='pale green', fg='blue')
lab1.grid(row=1,column=0)
lab2=Label(wn,text='Player 2: ',font=("consolas",13,'bold'),bg='pale green', fg='blue')
lab2.grid(row=2,column=0)

#Player Name Input
wn.bind('<Return>',lambda event:readme())

#Checker
click=True
flag=0

#Score
a=0
b=0
d=0

#Functions
#Funtion to Read Players
def readme():
    global player1, player2,pa,pb,a,b,d
    pa=player1.get()
    pb=player2.get()
    player1.configure(state=DISABLED)
    player2.configure(state=DISABLED)
    lab1=Label(wn,text=pa+':'+str(a),font=("consolas",13,'bold'),bg='pale green', fg='blue')
    lab1.grid(row=1,column=2)
    lab2=Label(wn,text=pb+':'+str(b),font=("consolas",13,'bold'),bg='pale green', fg='blue')
    lab2.grid(row=2,column=2)
    lab3=Label(wn,text='Draw:'+str(d),font=("consolas",13,'bold'),bg='pale green', fg='blue')
    lab3.grid(row=3,column=2)
#Function for Moves
def Move(buttons):
    global click,flag,pa,pb
    if buttons["text"] == " " and click == True:
        lab1=Label(wn,text=pa+':'+str(a),font=("consolas",13,'bold'),bg='pale green', fg='blue')
        lab1.grid(row=1,column=2)
        lab2=Label(wn,text=pb+':'+str(b),font=("consolas",13,'bold'),bg='pale green', fg='blue')
        lab2.grid(row=2,column=2)
        lab3=Label(wn,text='Draw:'+str(d),font=("consolas",13,'bold'),bg='pale green', fg='blue')
        lab3.grid(row=3,column=2)
        buttons["text"] = "X"
        click = False
        CheckWinner()
        flag += 1


    elif buttons["text"] == " " and click == False:
        buttons["text"] = "O"
        click = True
        CheckWinner()
        flag += 1
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")
    
#Function to Check Winner
def CheckWinner():
    global pa,pb,flag,a,b,d
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
        button7['text'] =='X' and button8['text'] == 'X' and button9['text'] == 'X' or
        button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
        button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
        button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
        button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
        button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        disableButton()
        msg=pa+' Wins!'
        tkinter.messagebox.showinfo("Tic-Tac-Toe",msg)
        a+=1
        lab1=Label(wn,text=pa+':'+str(a),font=("consolas",13,'bold'),bg='pale green', fg='blue')
        lab1.grid(row=1,column=2)
        lab2=Label(wn,text=pb+':'+str(b),font=("consolas",13,'bold'),bg='pale green', fg='blue')
        lab2.grid(row=2,column=2)
        lab3=Label(wn,text='Draw:'+str(d),font=("consolas",13,'bold'),bg='pale green', fg='blue')
        lab3.grid(row=3,column=2)

    elif(flag == 8):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")
        d+=1
        lab1=Label(wn,text=pa+':'+str(a),font=("consolas",13,'bold'),bg='pale green', fg='blue')
        lab1.grid(row=1,column=2)
        lab2=Label(wn,text=pb+':'+str(b),font=("consolas",13,'bold'),bg='pale green', fg='blue')
        lab2.grid(row=2,column=2)
        lab3=Label(wn,text='Draw:'+str(d),font=("consolas",13,'bold'),bg='pale green', fg='blue')
        lab3.grid(row=3,column=2)

    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
          button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
        disableButton()
        msg=pb+' Wins!'
        tkinter.messagebox.showinfo("Tic-Tac-Toe", msg)
        b+=1
        lab1=Label(wn,text=pa+':'+str(a),font=("consolas",13,'bold'),bg='pale green', fg='blue')
        lab1.grid(row=1,column=2)
        lab2=Label(wn,text=pb+':'+str(b),font=("consolas",13,'bold'),bg='pale green', fg='blue')
        lab2.grid(row=2,column=2)
        lab3=Label(wn,text='Draw:'+str(d),font=("consolas",13,'bold'),bg='pale green', fg='blue')
        lab3.grid(row=3,column=2)
#Function to Disable Buttons
def disableButton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)
#Function to Enable Buttons
def enableButton():
    button1.configure(state=NORMAL)
    button2.configure(state=NORMAL)
    button3.configure(state=NORMAL)
    button4.configure(state=NORMAL)
    button5.configure(state=NORMAL)
    button6.configure(state=NORMAL)
    button7.configure(state=NORMAL)
    button8.configure(state=NORMAL)
    button9.configure(state=NORMAL)
#Reset Function
def Restart():
    global click, flag
    enableButton()
    button1['text']= ' '
    button2['text']= ' '
    button3['text']= ' '
    button4['text']= ' '
    button5['text']= ' '
    button6['text']= ' '
    button7['text']= ' '
    button8['text']= ' '
    button9['text']= ' '
    click=True
    flag=0
    
    

#Buttons
reset=Button(wn,text='Restart',height=1, width=14,bd=5, font=('Consolas',13,'bold'),bg='pink',command=lambda:Restart())
reset.grid(row=3,column=0)

buttons = StringVar()

button1 = Button(wn, text=' ', font='Times 20 bold', bg='royal blue', fg='white',disabledforeground="white", height=4, width=8, bd=5,command=lambda:Move(button1))
button1.grid(row=4, column=0)

button2 = Button(wn, text=' ', font='Times 20 bold', bg='royal blue', fg='white',disabledforeground="white", height=4, width=8, bd=5,command=lambda:Move(button2))
button2.grid(row=4, column=1)

button3 = Button(wn, text=' ',font='Times 20 bold', bg='royal blue', fg='white',disabledforeground="white", height=4, width=8, bd=5,command=lambda:Move(button3))
button3.grid(row=4, column=2)

button4 = Button(wn, text=' ', font='Times 20 bold', bg='royal blue', fg='white',disabledforeground="white", height=4, width=8, bd=5,command=lambda:Move(button4))
button4.grid(row=5, column=0)

button5 = Button(wn, text=' ', font='Times 20 bold', bg='royal blue', fg='white',disabledforeground="white", height=4, width=8,bd=5,command=lambda:Move(button5))
button5.grid(row=5, column=1)

button6 = Button(wn, text=' ', font='Times 20 bold', bg='royal blue', fg='white',disabledforeground="white", height=4, width=8,bd=5,command=lambda:Move(button6))
button6.grid(row=5, column=2)

button7 = Button(wn, text=' ', font='Times 20 bold', bg='royal blue', fg='white',disabledforeground="white", height=4, width=8,bd=5,command=lambda:Move(button7))
button7.grid(row=6, column=0)

button8 = Button(wn, text=' ', font='Times 20 bold', bg='royal blue', fg='white',disabledforeground="white", height=4, width=8,bd=5,command=lambda:Move(button8))
button8.grid(row=6, column=1)

button9 = Button(wn, text=' ', font='Times 20 bold', bg='royal blue', fg='white',disabledforeground="white", height=4, width=8,bd=5,command=lambda:Move(button9))
button9.grid(row=6, column=2)

#Game Loop
wn.mainloop()

