import requests
from pprint import pprint

#requests.get()
#requests.post()
#requests.delete()
#requests.head()
#requests.put()
#requests.patch()

#get
param = {'a':1}
header = {"content-type":"application/json"}
r = requests.get("http://www.baidu.com", params=param, headers=header)
print r.status_code
print r.encoding
print r.cookies
print r.headers
print r.content

item_id = "Uf53a4bad3865232a5936c0a8d3453a76"
r = requests.get("http://10.15.19.223:9200/8af021fedc23280595427b8374a49f4e_item/base_item2/%s" % item_id, timeout=1)
print r.status_code
pprint(r.json())

#post
header = {"content-type":"application/json"}
data = """
{
  "interface":"cn.uc.reco.RetrievalService",
  "version":"1.0.0",
  "group":"HSF",
  "method":"RetrieveItems",
  "type":"bytes",
  "args": {"req_id":"8bb01be9-1516345556113","appid":"8af021fedc23280595427b8374a49f4e","type":"item","utdid":"VocTCMhCvVcDAI1bzwVvbeyB","compress":false,"reco_sim_level":0.0,"retrieves":[{"req_fields":[],"query":{"and":[{"field":"parent_asset_id","type":"=","value":1712}],"or":[]},"filter":{"and":[{"field":"audit_str","type":"=","value":"1,0"}],"or":[]},"sortby":[{"field":"publish_timestamp","order":"desc"}],"size":300}]}
}
"""
r = requests.post("http://100.84.73.137:8848/", data=data, headers=header)
print r.status_code
print r.json()

s = requests.session()
r = s.post("http://100.84.73.137:8848/", data=data, headers=header)
r = s.post("http://100.84.73.137:8848/", data=data, headers=header)
print r.status_code
print r.cookies
pprint(r.json())
