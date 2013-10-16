import requests
import json
import properties
import Login
import utils
import pymongo
import unittest
from nose.tools import *
    
class TestPushConfig(unittest.TestCase):
    def setUp(self):
        global login_cookie
        login_cookie = None
        login_cookie = Login.login()
        if [] in login_cookie:
            raise AssertionError("Login is not successful.")
        else:
            print "Login is done successfully."
            
    def test_1_push_config(self):
        """
                This test case verifies whether Default config is applied to customer.
        """
        global customer_id, config_id
        baseurl = properties.baseurl
        js2 = utils.customer_list(login_cookie)
        for i in range(len(js2['results'])):    
            ourResult = js2['results'][i]['name']
            if properties.customer_name == ourResult:
                customer_id = js2['results'][i]['id']
                js = utils.config_list(login_cookie)
                for i in range(len(js['results'])):    
                    ourResult = js['results'][i]['config_name']
                    if properties.configuration_name in ourResult:
                        config_id = js['results'][i]['id']
                        default_config_request = baseurl + ("/ajax?request_type=update_default_config_customer&customer_id=%s&config_id=%s&create_config_request=true" % (customer_id,config_id))
                        config_update_response = requests.get(default_config_request, cookies=login_cookie)
                        js3 = json.loads(config_update_response.text)
                        if "Default Configuration of Customer updated" in js3['results']['message']:
                            print "Default config is applied to customer successfully."
                        else:
                            raise AssertionError("Default config is not applied to customer.")

    def test_2_verify_db(self):
        """
                This test case verifies whether Default config id parameter is updated in DB for customer.
        """
        mongo_db_ip = properties.mongo_ip
        connection = pymongo.MongoClient(mongo_db_ip)
        db_name = properties.db_to_be_used
        mongo_db = connection[db_name]
        collection_name = properties.customer_collection_name
        mongo_collection = mongo_db[collection_name]
        mongo_document = mongo_collection.find_one({"name" : "default"},{"default_config_id" : 1})
        if str(mongo_document['_id']) == str(customer_id):
            if not str(mongo_document['default_config_id']) == str(config_id):
                raise AssertionError("Default config is not assigned to customer")
            else:
                print "Default config is assigned to customer"
        connection.disconnect()

    def tearDown(self):
        pass
