from toutatis import *
from six.moves import input
import requests
import hmac
import hashlib
import random
import string
import json
import argparse




fa = print('''\033
-------------------------------
.:: Extract user information ::.
    
██████╗ ██████╗  █████╗ ██╗  ██╗███████╗  ██╗      █████╗ ███╗   ███╗
██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔════╝  ██║     ██╔══██╗████╗ ████║
██║  ██║██████╔╝███████║█████═╝ █████╗    ██║     ███████║██╔████╔██║
██║  ██║██╔══██╗██╔══██║██╔═██╗ ██╔══╝    ██║     ██╔══██║██║╚██╔╝██║
██████╔╝██║  ██║██║  ██║██║ ╚██╗███████╗  ███████╗██║  ██║██║ ╚═╝ ██║
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝  ╚══════╝╚═╝  ╚═╝╚═╝    ╚═╝  
-----------------Make by Drake Lam--------------
Have a nice day!


\033''')

print("_________________________________________________________ ")

if fa == '1':
  parser = argparse.ArgumentParser()


username = input('username : ')
sessionsId = input('sessionsId : ') 
infos = getAllInfos(username,sessionsId)

print("Information about : "+infos["username"])
print("First Name: "+infos["FullName"])
print("Instagram ID : "+infos["userID"])

info = getInfo(username,sessionsId)
print("Verified Account: "+str(info['is_verified']))
print("Personal account: "+str(info["is_private"]))
print("Followers: "+str(info["follower_count"]))
print("Following : "+str(info["following_count"]))
print("Post count: "+str(info["media_count"]))
print("Number of #tags in posts : "+str(info["following_tag_count"]))
print("External URL: "+info["external_url"])
print("IGTV Post Number: "+str(info["total_igtv_videos"]))
if len(infos["biography"]) >1:
    infos["biography"]="Not found!"

print("Biography: "+infos["biography"])

if len(infos["publicEmail"])==0:
     infos["publicEmail"]="Not found!"

print("Public Email: "+infos["publicEmail"])

if infos["recoveryEmail"]=="NULL":
     infos["recoveryEmail"]=="Not found!"

print("Recovery email : "+infos["recoveryEmail"])

if len(infos["public_phone_number"])<1:
    infos["public_phone_number"]="Not found!"

print("Public phone number : "+infos["public_phone_number"])
print("Image link: "+infos["ProfilePicture"])
######## HMAC keyed-hash message authentication code
if fa == '2':
  def HMAC(text):
    key = '3f0a7d75e094c7385e3dbaa026877f2e067cbd1a4dbcf3867748f6b26f257117'
    hash = hmac.new(key,msg=text,digestmod=hashlib.sha256)
    return hash.hexdigest()

def randomString(size):
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(size))

