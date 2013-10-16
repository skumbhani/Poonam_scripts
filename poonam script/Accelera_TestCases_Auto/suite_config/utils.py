import requests
import json     
import properties
global baseurl

baseurl = properties.baseurl

def config_list(cookies):
    configrequest = baseurl+'/ajax?request_type=configuration_list'
    config_response = requests.get(configrequest,cookies=cookies)
    js = json.loads(config_response.text)
    return js

def customer_list(cookies):
    customer_request = baseurl + "/ajax?request_type=customers"
    customer_response = requests.get(customer_request,cookies=cookies)
    js2 = json.loads(customer_response.text)
    return js2
