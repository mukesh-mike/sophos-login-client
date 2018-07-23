import requests
import re
import tkMessageBox


def logoff_msg():
    tkMessageBox.showinfo(
        "Message",
        "You have Logged-Off Successfully."
    )



def gateway(event=None):
    tkMessageBox.showerror(
        "Message",
        "Gateway Unreachable!!!"
    )



def log_out(us_name2,num):
    try:
        with requests.Session() as s:
            payload = {
		        "mode": "193",
		        "username": us_name2.get()
	        }

            url = 'https://172.31.1.6:8090/login.xml'
            page = s.post(url,verify=False,data=payload)
            p = page.content
            loggoff_msg = re.compile("You have successfully logged off")

            if loggoff_msg.search(p) is not None:
                if num==1:
                    logoff_msg()

    except:
        gateway()
        return 0




