from mqtt_client import device_interface as Client
import time

def time_test(msg):
    print("time_test:success,call by mqtt client")
    time4 = time.time()
    payload = str(msg.payload,encoding="utf-8")
    time2 = time.time()
    time1 = float(payload.split()[1])
    time3 = time.time()
    print("converting btyes to str using :{}ms".format((time2-time4)*1000))
    print("spilt the str with space using:{}ms".format((time3-time2)*1000))
    print("from send to use api using    :{}ms".format((time4-time1)*1000))
    # print("time use is :{}ms".format())

payload_length = 1*1000
tmp = list(map(str,list(range(1000000))))
payload_str = "    ".join(tmp)[:payload_length]

if __name__ == "__main__":
    topic = "test"
    clinet_id = "test1"
    host = "52.184.15.163"
    port = 1883
    t = Client(clinet_id)
    t.add2device_topic(topic)
    t.add_action(time_test)
    # print(t.action.keys())
    # print(type(t.action.keys()))
    # print("print_msg" in t.action.keys())
    t.run("123",host,port)
    t.subscribe("test",2)
    print("set down")
    t2 = Client("test3")
    t2.run("234",host,port)
    for i in range(100):

        time1 = time.time()
        t2.publish("test","time_test "+str(time.time())+" time"+str(i)+" "+payload_str,2)
        time2 = time.time()
        print("\r\nsending test in loop {},and use time {}".format(i,(time2-time1)*1000))
        time.sleep(5)
    time.sleep(1000)