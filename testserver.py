from bottle import get, template, run, request
from bottle.ext.websocket import GeventWebSocketServer
from bottle.ext.websocket import websocket
from pymongo import MongoClient
from bson.json_util import dumps
import httpagentparser
import json
import time

users = set()

@get('/')
def index():
    return template('index2050')

@get('/admin')
def admin():
    return template('admin2050')

@get('/welcome')
def welcome():
    return template('part2')

@get('/websocket', apply=[websocket])
def chat(ws):
    print ws
    agent = request.environ.get('HTTP_USER_AGENT')
    browser = httpagentparser.detect(agent)
     
    json_str = json.dumps(browser)

    resp = json.loads(json_str)

    print (resp['os']['name'])
    print (resp['dist']['name'])
    print (resp['browser']['name'])
    print (resp['browser']['version'])
    
    ip=request.environ.get('REMOTE_ADDR')
    print (ip)
    print("abc")
    client = MongoClient()
    db = client.test
    
    if(db.ipad.find_one({"ip":ip,"os_name": resp['os']['name'],"platform_name": resp['dist']['name'],"browser_name": resp['browser']['name'],"browser_version": resp['browser']['version']})==None):
     
     db.ipad.insert({
      "ip": ip,
      "os_name": resp['os']['name'],
      "platform_name": resp['dist']['name'],
      "browser_name": resp['browser']['name'],
      "browser_version": resp['browser']['version'],
      "ct":"0"
      })
     if(db.mycol2.count()!=1):
      db.mycol2.insert({
       "ipa": ip,
       "id1": "abc"
       })
     else:
      cur3=db.mycol2.find_one()
      data3=json.loads(dumps(cur3))
      cur3=db.mycol2.update({"id1":"abc"},{'$set':{"ipa":ip}})
     cur2=db.mycol1.find_one()
     data2=json.loads(dumps(cur2))
     
        
     users.add(ws)
       
     cur = db.socket_count.find_one()
     data = json.loads(dumps(cur))
     count = int(data['count'])
     cur = db.socket_count.update({'soc': 'true'},{'$set':{'count': count+1}})
      
     print 'Clients online :', count+1
      
    elif(db.ipad.find_one({"ip":ip,"os_name": resp['os']['name'],"platform_name": resp['dist']['name'],"browser_name": resp['browser']['name'],"browser_version": resp['browser']['version']})!=None):
     cur5=db.ipad.find_one({"ip":ip,"os_name": resp['os']['name'],"platform_name": resp['dist']['name'],"browser_name": resp['browser']['name'],"browser_version": resp['browser']['version']})
     data5 = json.loads(dumps(cur5))
     ct1=int(data5['ct'])
     cur5=db.ipad.update({"ip":ip,"os_name": resp['os']['name'],"platform_name": resp['dist']['name'],"browser_name": resp['browser']['name'],"browser_version": resp['browser']['version']},{'$set':{'ct': str(ct1+1)}})
     cur9=db.ipad.find_one({"ip":ip,"os_name": resp['os']['name'],"platform_name": resp['dist']['name'],"browser_name": resp['browser']['name'],"browser_version": resp['browser']['version']})
     data9 = json.loads(dumps(cur9))
     ct2=int(data9['ct'])
     print ct2
    else:
     a=1        
           
    while True:
        msg = ws.receive()
        if msg is not None:
            for u in users:
                u.send(msg)
        else:
            break
    
    cur8=db.ipad.find_one({"ip":ip,"os_name": resp['os']['name'],"platform_name": resp['dist']['name'],"browser_name": resp['browser']['name'],"browser_version": resp['browser']['version']})
    data8=json.loads(dumps(cur8))
    cot=int(data8['ct'])
      
    if(db.ipad.find_one({"ip":ip,"os_name": resp['os']['name'],"platform_name": resp['dist']['name'],"browser_name": resp['browser']['name'],"browser_version": resp['browser']['version']})!=None and cot==0):

     abc=db.mycol1.find_one()

     data2= json.loads(dumps(abc))
     ip2=str(data2['ipa'])
     print(ip2)
     print("abc2")
     
     db.ipad.remove({"ip":ip,"os_name": resp['os']['name'],"platform_name": resp['dist']['name'],"browser_name": resp['browser']['name'],"browser_version": resp['browser']['version']})

     cur = db.socket_count.find_one()
     data = json.loads(dumps(cur))
     count = int(data['count'])
     cur = db.socket_count.update({'soc': 'true'},{'$set':{'count': count-1}})

     print 'Clients online :', count-1
     users.remove(ws)
    elif(db.ipad.find_one({"ip":ip,"os_name": resp['os']['name'],"platform_name": resp['dist']['name'],"browser_name": resp['browser']['name'],"browser_version": resp['browser']['version']})!=None and cot>0):
     cur6=db.ipad.find_one({"ip":ip,"os_name": resp['os']['name'],"platform_name": resp['dist']['name'],"browser_name": resp['browser']['name'],"browser_version": resp['browser']['version']})
     data6 = json.loads(dumps(cur6))
     ct3=int(data6['ct'])
     cur6=db.ipad.update({"ip":ip,"os_name": resp['os']['name'],"platform_name": resp['dist']['name'],"browser_name": resp['browser']['name'],"browser_version": resp['browser']['version']},{'$set':{'ct': str(ct3-1)}})
     cur10=db.ipad.find_one({"ip":ip,"os_name": resp['os']['name'],"platform_name": resp['dist']['name'],"browser_name": resp['browser']['name'],"browser_version": resp['browser']['version']})
     data10 = json.loads(dumps(cur10))
     ct4=int(data10['ct'])
     print ct4

    else:
     b=1 
  
@get('/ws_welcome', apply=[websocket])
def ws_welcome(ws):
 agent = request.environ.get('HTTP_USER_AGENT')
 browser = httpagentparser.detect(agent)
 json_str = json.dumps(browser)
 client = MongoClient()
 db = client.test
 resp = json.loads(json_str)
 ip=request.environ.get('REMOTE_ADDR')
 cur20=db.ipad.find_one({"ip":ip,"os_name": resp['os']['name'],"platform_name": resp['dist']['name'],"browser_name": resp['browser']['name'],"browser_version": resp['browser']['version']})
 data20 = json.loads(dumps(cur20))
 ct1=int(data20['ct'])
 while True:
  msgg=ws.receive()
  if msgg is not None:
    
          
    if(db.ipad.find_one({"ip":ip,"os_name": resp['os']['name'],"platform_name": resp['dist']['name'],"browser_name": resp['browser']['name'],"browser_version": resp['browser']['version']})!=None):
               
     cur12=db.ipad.update({"ip":ip,"os_name": resp['os']['name'],"platform_name": resp['dist']['name'],"browser_name": resp['browser']['name'],"browser_version": resp['browser']['version']},{'$addToSet':{'pagew': msgg}})

     cur15=db.ipad.update({"ip":ip,"os_name": resp['os']['name'],"platform_name": resp['dist']['name'],"browser_name": resp['browser']['name'],"browser_version": resp['browser']['version']},{'$set':{'ct': str(ct1+1)}})
  else:
   break
 cur14=db.ipad.update({"ip":ip,"os_name": resp['os']['name'],"platform_name": resp['dist']['name'],"browser_name": resp['browser']['name'],"browser_version": resp['browser']['version']},{'$pop':{'pagew': msgg}})
 
 cur16=db.ipad.update({"ip":ip,"os_name": resp['os']['name'],"platform_name": resp['dist']['name'],"browser_name": resp['browser']['name'],"browser_version": resp['browser']['version']},{'$set':{'ct': str(ct1-1)}})

@get('/ws_admin', apply=[websocket])
def ws_admin(ws):
    while True:
        client = MongoClient()
        db = client.test
        cur2=db.mycol2.find_one()
        data2=json.loads(dumps(cur2))
        ipa1=str(data2['ipa'])
        msg = ws.receive()
        if msg is not None:        
            cur = db.socket_count.find_one()
            data = json.loads(dumps(cur))
            count = int(data['count'])
            cur1 = db.ipad.find_one()
            data1 = json.loads(dumps(cur1))
            mesg={"ipadd":ipa1,"count":count}
            ws.send(str(mesg))
        else:
            break



@get('/refresh')
def refresh():
    client = MongoClient()
    db = client.test
    cur = db.socket_count.update({'soc': 'true'},{'$set':{'count': 0}})
    db.ipad.remove()
    cur4=db.mycol2.find_one()
    data4=json.loads(dumps(cur4))
    cur4=db.mycol2.update({"id1":"abc"},{'$set':{"ipa":"NONE"}})
    return 'DB Refreshed'
    
run(host='192.168.0.11', port=8080, server=GeventWebSocketServer)


