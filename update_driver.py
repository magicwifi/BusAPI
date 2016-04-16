#-*- coding:utf-8 -*-
import requests
import sys
from sys import argv
from bs4 import BeautifulSoup
import urllib
import urllib2
import json

def main(name,lng,lat):
        data = {'name':name, 'lng':lng,'lat':lat}
        url = "http://219.141.189.132:3000/api/update_driver"
        req = urllib2.Request(url)
        req.add_header('Content-Type', 'application/json')
        response = urllib2.urlopen(req,json.dumps(data))
        result = response.read()
        print result

if __name__ == '__main__':
        if len(sys.argv) != 4:
                print 'Usage: python input_name output_name'
                exit(1)
        name = sys.argv[1]
        lng = sys.argv[2]
        lat = sys.argv[3]
        main(name,lng,lat)
