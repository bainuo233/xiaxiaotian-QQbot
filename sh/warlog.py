# -*- coding: utf-8 -*-
import urllib.request
import json
import ssl

with open("mykey.txt") as f:
    mykey=f.read().rstrip("\n")
    
    ssl._create_default_https_context = ssl._create_unverified_context
    
    base_url = "https://api.clashroyale.com/v1"
     
    endpoint = "/clans/%2388GUJ80/warlog"
    
    request = urllib.request.Request(
                   base_url+endpoint,
                   None,
                   {
                            "Authorization":"Bearer %s" % mykey
                   }
                )
    response = urllib.request.urlopen(request).read().decode("utf-8")
       
    data = json.loads(response)
    
    for item in data["items"]:
                    print("成员名称：%s\n奖杯：%d\n竞技场：%s\n " % (
                                    item["wins"], 
                                    item["name"],
                                    item["battlesPlayed"]
                            ))
