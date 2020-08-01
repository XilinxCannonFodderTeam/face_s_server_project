# import requests
# import json

# url = "http://52.184.15.163:5000/test"

# data = [{"name":"lock"}]
# data = json.dumps(data)
# print(type(data))

# r = requests.get(url,data=data)

# print("lock" == 'lock')


import flask

app = flask.Flask(__name__)

@app.route("/test",methods=["GET","POST"])
def test():
    print("mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")
    print(str(flask.request))
    print(flask.request.data)
    print(flask.request.date)
    print(flask.request.values)
    print(flask.request.form)
    print(flask.request.form_data_parser_class)
    for item in flask.request.headers.items():
        print(item)
    print(flask.request.host_url)
    print(flask.request.headers)
    print(flask.request.url)
    print(flask.request.args)
    print(flask.request.files)
    print(flask.request.stream.read())
    return "0"

def get_pic_path(topic, time):
    return "./","test.jpg"

@app.route("/get_pic",methods = ["GET","POST"])
def get_pic():
    print("****************************************************")
    dir_path,filename = get_pic_path(None, None)

    return flask.send_from_directory(directory= dir_path, filename= filename)

app.run("192.168.43.103",5000)