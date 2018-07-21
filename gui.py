from Tkinter import *
from login import *
from logout import *

import tkMessageBox

def err_password(event=None):
    tkMessageBox.showinfo(
        "Message",
        "Please Enter Password!!!"
    )



def err_username(event=None):
    tkMessageBox.showinfo(
        "Message",
        "Please Enter Username!!!"
    )



def check(event=None):
    if us_name.get() :
        if ps_name.get():
            if logvar.get() == "Login":
                ans_out = log_out(us_name,0)
                ans = 0
                if ans_out != 0:
                    ans = log_in(us_name, ps_name)


                if ans == 1:
                    logvar.set("Logout")
                    us_name.config(state='disabled')
                    ps_name.config(state='disabled')
            else:
                log_out(us_name,1)
                logvar.set("Login")
                us_name.config(state='normal')
                ps_name.config(state='normal')

        else :
            err_password()
    else :
        err_username()




root = Tk()
root.title("Sophos Login")
root.geometry("400x200+500+250")
root.resizable(width=False,height=False)


Label(root,text="Username").grid(row=0,column=0,padx=4)
us_name = Entry(root,width=40)
us_name.grid(row=0,column=1,pady=4)
Label(root,text="Password").grid(row=1,column=0,padx=4)
ps_name = Entry(root,width=40,show="*")
ps_name.grid(row=1,column=1,pady=4)


logvar = StringVar()
logvar.set("Login")
B1 = Button(root,textvariable=logvar,command=check)
B1.grid(row=2,column=0)

root.mainloop()