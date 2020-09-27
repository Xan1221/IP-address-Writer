# -*- coding: utf-8 -*-
#import statemnts
import requests
import csv

def IpWriter():
    #open the csv file and setting it to write
    c = csv.writer(open("ipdata.csv","w"),lineterminator = '\n')
    c.writerow(["number","ip Address","country","region"])
    i=1
    
    
    #print welcome message
    print("This program will write an excel fill for you because arch is annoying")
    #while loop accepting user requests for IP addresses
    while True :
        g = input("please enter an IP address/space or quit: ")
        if g == "next":
            c.writerow([])
            i = 1
       
        elif g == "quit":
            return
        
        else:
            r = requests.get('https://geo.ipify.org/api/v1?apiKey='enter your API key' %g).json()
            c.writerow([i,r['ip'],r['location']['country'],r['location']['region']])
            i+=1
        
IpWriter()
