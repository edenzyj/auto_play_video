import base64
from  play_video import *

ServerURL = 'https://class.iottalk.tw' #For example: 'https://iottalk.tw'
MQTT_broker = 'class.iottalk.tw' # MQTT Broker address, for example:  'iottalk.tw' or None = no MQTT support
MQTT_port = 5566
MQTT_encryption = True
MQTT_User = 'iottalk'
MQTT_PW = 'iottalk2023'

device_model = 'Music_to_Video'
IDF_list = []
ODF_list = ['MP4_O']
device_id = '31283301712261529' #if None, device_id = MAC address
device_name = 'player'
exec_interval = 1  # IDF/ODF interval

def on_register(r):
    print('Server: {}\nDevice name: {}\nRegister successfully.'.format(r['server'], r['d_name']))

def MP4_O(data:list):
    print("len of data = ", len(data[0])) 
    if len(data[0]) > 0:
        play_video(data[0])
    else:
        print("error")
