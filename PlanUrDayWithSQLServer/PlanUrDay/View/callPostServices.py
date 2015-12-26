import http.client as hc
#from flask import jsonify
import json

def callPostServices(host, port, headers, params, resource):
    conn = hc.HTTPConnection(host, port)
    print(params)
    conn.request("POST", resource ,json.dumps(params),headers)
    return conn.getresponse()


#callPostServices("127.0.0.1", 5000, {"Content-type": "application/json",
  #         "Accept": "application/json"}, {'firstname': 'mmmm', 'lastname': 'yyyy', 'mobileno': 858585, 'dob': '2014-05-06', 'emailid':'maaa@ggg.com', 'password': 'ggggg'},"/addUser")
