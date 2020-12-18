from django.shortcuts import render
from django.http import HttpResponse
import requests
import json,urllib.request
from django.template.defaulttags import register
# Create your views here.
def index(req):
    data=True
    result=None
    gb=None
    countries=None
    while(data):
        try:
            result=requests.get('https://api.covid19api.com/summary')
            json=result.json()
            gb=json['Global']
            countries=json['Countries']
            data=False
        except:
            data=True
    
    # print(result.json()['Global'])
    return render(req,'index.html',{'global':gb,'countries':countries})

def india(req):
    @register.filter
    def get_item(dictionary, key):
        return dictionary.get(key)
    result=requests.get('https://api.covid19api.com/summary')
    countries=result.json()['Countries']
    data = urllib.request.urlopen("https://api.covid19india.org/v4/data.json").read()
    output = json.loads(data)
    #removing total 
    a=output.pop('TT')
    name={"AN":"Andaman and Nicobar Islands", "AP":"Andhra Pradesh", "AR":"Arunachal Pradesh", "AS":"Assam", "BR":"Bihar" ,"CH":"Chandigarh", "CT":"Chhattisgarh", "DL":"Delhi", "DN":"Dadra and Nagar Haveli and Daman and Diu", "GA":"Goa", "GJ":"Gujarat" ,"HP":"Himachal Pradesh" ,"HR":"Haryana" ,"JH":"Jharkhand", "JK":"Jammu and Kashmir", "KA":"Karnataka", "KL":"Kerala", "LA":"Lakshadweep ", "MH":"Maharashtra", "ML":"Meghalaya", "MN":"Manipur", "MP":"Madhya Pradesh", "MZ":"Mizoram", "NL":"NagaLand", "OR":"Orissa", "PB":"Punjab" ,"PY":"Puducherry", "RJ":"Rajasthan", "SK":"Sikkim", "TG":"Telangana" ,"TN":"Tamil Nadu", "TR":"Tripura", "TT":"TT" ,"UP":"Uttar Pradesh", "UT":"Uttrakhand", "WB":"West Bengal"}
    # print(name)
    
    
    return render(req,'india.html',{'countries':countries,'states':output,'name':name})
