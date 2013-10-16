import requests
import json
import properties
import Login
import utils

class TestCreateConfig(unittest.TestCase):
    def setUp(self):
        global login_cookie
        login_cookie = None
        login_cookie = Login.login()
        if [] in login_cookie:
            raise AssertionError("Login is not successful.")
        else:
            print "Login is done successfully."

#This function checks whether config blob is already exists if yes then updates its parameters with given parameters else creates new blob with given parameters
    def test_1_create_config(self):
        """
            This test case checks whether config blob is already exists
            if not then creates a new config blob with given parameters.
        """
        baseurl = properties.baseurl
        js = utils.config_list(login_cookie)
        for i in range(len(js['results'])):    
            ourResult = js['results'][i]['config_name']
            if properties.configuration_name in ourResult:
                _id = js['results'][i]['id']
                createconfig_request = baseurl +("/ajax?request_type=configuration&config_name=%s&sntp_server=pool.ntp.org&log_server=logserver&radio_config_count=2&radio_id[]=2.4G&power[]=10&channel[]=4&admin_status[]=disabled&radio_id[]=5G&power[]=12&channel[]=6&admin_status[]=enabled&wif_config_count=4&wifi_radio_id[0]=2.4G&ssid[0]=MGMT&security[0]=none&passphrase[0]=&wifi_radio_id[1]=5G&ssid[1]=EMP&security[1]=none&passphrase[1]=&wifi_radio_id[2]=2.4G&ssid[2]=STUDENT&security[2]=wpa-psk&passphrase[2]=password&wifi_radio_id[3]=5G&ssid[3]=GUEST&security[3]=wpa2-psk&passphrase[3]=password&config_id=%s" % (properties.configuration_name,_id))
                break
            else:
                createconfig_request = baseurl + ("/ajax?request_type=configuration&config_name=%s&sntp_server=pool.ntp.org&log_server=logserver&radio_config_count=2&radio_id[]=2.4G&power[]=10&channel[]=4&admin_status[]=disabled&radio_id[]=5G&power[]=12&channel[]=6&admin_status[]=enabled&wif_config_count=4&wifi_radio_id[0]=2.4G&ssid[0]=MGMT&security[0]=none&passphrase[0]=&wifi_radio_id[1]=5G&ssid[1]=EMP&security[1]=none&passphrase[1]=&wifi_radio_id[2]=2.4G&ssid[2]=STUDENT&security[2]=wpa-psk&passphrase[2]=password&wifi_radio_id[3]=5G&ssid[3]=GUEST&security[3]=wpa2-psk&passphrase[3]=password" % properties.configuration_name)
        createconfig_response = requests.get(createconfig_request,cookies=login_cookie)
        js1 = json.loads(createconfig_response.text)
        print js1
        if 'Configuration Updated in DB!' in js1['results']['message'] or 'Configuration Saved in DB!' in js1['results']['message']:
            print "Configuration blob is added in database successfully."
        else:
            raise AssertionError("Configuration blob is not added in database.")

    def tearDown(self):
        pass

        
    
            
        
