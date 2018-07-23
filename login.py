import requests
import re
import tkMessageBox

def max_limit(event=None):
    tkMessageBox.showerror(
        "Message",
        "Maximum Login Limit Reached!!!"
    )



def invalid_login(event=None):
    tkMessageBox.showerror(
        "Message",
        "Invalid Login Credentials."
    )



def success_login(event=None):
    tkMessageBox.showinfo(
        "Message",
        "You have Logged-In Successfully."
    )



def gateway(event=None):
    tkMessageBox.showerror(
        "Message",
        "Gateway Unreachable!!!"
    )




def log_in(us_name1,ps_name1):
    try:
        with requests.Session() as s:
            payload = {
                "mode": "191",
                "username": us_name1.get(),
                "password": ps_name1.get()
            }


            url = 'https://172.31.1.6:8090/login.xml'
            page = s.post(url, verify=False, data=payload)
            p = page.content
            # print p

            login_max_msg = re.compile("You have reached the maximum login limit")
            login_error_msg = re.compile("Invalid user name/password")
            login_success_msg = re.compile("You have successfully logged in")
            if login_success_msg.search(p) is not None:
                success_login()
                return 1
            elif login_max_msg.search(p) is not None:
                max_limit()
                return 0
            elif login_error_msg.search(p) is not None:
                invalid_login()
                return 0

    except:
        gateway()
        return 0