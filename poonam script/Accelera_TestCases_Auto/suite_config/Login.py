import requests
import json

#This function does login and returns login session cookie
def login():
    baseurl = "http://192.168.2.39/accelera_poonam/index.php"
    loginrequest = baseurl+'/ajax?request_type=login_user&email=admin@acceleramb.com&password=welcome'
    loginresponse = requests.get(loginrequest)
    login_cookies = loginresponse.cookies
    #print login_cookies
    return login_cookies
