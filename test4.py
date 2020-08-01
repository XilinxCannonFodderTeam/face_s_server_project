import requests
from mqtt_client import device_interface as Client
import time
import cv2
from flask import url_for


def find_stranger(topics):
    if isinstance(topics, str):
        payload = "find_stranger 1 "+ topics + " "
    else: 
        payload = "find_stranger " + str(len(topics)) +" " + " ".join(topics) + " "
    localtime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    payload = payload + localtime
    # print(payload)
    client.publish(client.topic["2server"], payload, client.qos)

def upload_pic(frame):
    url = "http://52.184.15.163:5000/upload?pic_name=\"test.jpg\"&topic=\"todevice\"&time=2020"
    params_data = {"pic_name":"test.jpg","topic":"device_id","time":"202007291709"}
    
    files = {'file':(frame)}
    # ,params = params_data,
    r = requests.post(url, files=files)
    print(r.url)
    print("get state code is :",r.status_code)

def starnger_test():
    print("this is test for find stranger")
    find_stranger("toapp")
    print("finish to send msg 1")
    img = cv2.imread("./test.jpg")
    upload_pic(img)
    print("finish to send msg 3")




device_id = "device"
device_topic_sub = "todevice"
app_topic = "toapp"
app_id = "app"
host = "52.184.15.163"
port = 1883
client = Client(device_id)
client.run("123", host, port)
time.sleep(1)
client.add_subscribe(device_topic_sub)
client.add2device_topic("todevice")
client.add2app_device_topic("toapp")

starnger_test()