from tkinter import*
import random, string



root = Tk()
root.geometry("400x280")
root.title("Password Generator")

#intro text
title = StringVar()
label = Label(root,textvariable=title).pack()
title.set("The strength of password;")

def selection():
    selection=choice.get()


choice = IntVar()
R1 = Radiobutton(root, text="POOR",variable=choice,value=1,command=selection).pack(anchor=CENTER)
R2 = Radiobutton(root, text="AVERAGE",variable=choice,value=2,command=selection).pack(anchor=CENTER)
R3 = Radiobutton(root, text="ADVANCED",variable=choice,value=3,command=selection).pack(anchor=CENTER)


labelchoice = Label(root)
labelchoice.pack()

lenlabel=StringVar()
lenlabel.set("password length")
lentitle=Label(root,textvariable=lenlabel).pack()


val=IntVar()
spinlength=Spinbox(root,from_=8,to_=24,textvariable=val,width=13).pack()





def callback():
    Isum.configtext=passgen()


passgenButton=Button(root,text="Generate Password",bd=5,height=2,command=callback,pady=3)
passgenButton.pack()
password = str(callback)


Isum = Label(root,text="")
Isum.pack(side=BOTTOM)






#logic
poor=string.ascii_uppercase+string.ascii_lowercase
average=string.ascii_uppercase+string.ascii_lowercase+string.digits



symbols=",._-""@!$%^&*()[]{}\''+<>?/"
letters="abcdefghijklmnopqrstuvwxyz"
capitals="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
advance=poor+average+symbols+letters+capitals


def passgen():
    if choice.get()==1:
        return "".join(random.sample(poor,val.get()))
    elif choice.get()==2:
        return "".join(random.sample(average,val.get()))
    elif choice.get()==3:
        return "".join(random.sample(advance,val.get()))

root.mainloop()
                     
                     
    
