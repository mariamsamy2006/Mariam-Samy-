from tkinter import*
root=Tk()
root.geometry('400x500')
root.title('Home')
def fun():
    name=txt.get('1.0,end')
    lbl['text']=name
btn=Button(root,command=fun,text='click me',width='12',height='3',fg='white',bg='black',font='25')
lbl=Label(root,width='25',height='3',bg='black',fg='white',font='25')
txt=Text(root,width='15',height='13',font='25',bg='white',fg='black')
lbl.pack()
btn.pack()
txt.pack()


root.mainloop()