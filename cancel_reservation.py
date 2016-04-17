#-*- coding:utf-8 -*-
import requests
import sys
from sys import argv
from bs4 import BeautifulSoup
import urllib
import urllib2
import json

def main(passenger_id,bus_number_id,site_id):
        data = {'passenger_id':passenger_id, 'bus_number_id':bus_number_id,'site_id':site_id}
        url = "http://219.141.189.132:3000/reservations/cancel"
        req = urllib2.Request(url)
        req.add_header('Content-Type', 'application/json')
        response = urllib2.urlopen(req,json.dumps(data))
        result = response.read()
        print result

if __name__ == '__main__':
        if len(sys.argv) != 4:
                print 'Usage: python input_name output_name'
                exit(1)
        passenger_id = sys.argv[1]
        bus_number_id = sys.argv[2]
        site_id = sys.argv[3]
        main(passenger_id,bus_number_id,site_id)
