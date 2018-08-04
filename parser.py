#!/usr/bin/python
## -*- coding: utf-8 -*-

import sys
import dpkt
import socket, random

# RR types
A = 0
NS = 0
CNAME = 0
SOA = 0
NULL = 0
PTR = 0
HINFO = 0
MX = 0
TXT = 0
AAAA = 0
SRV = 0
OPT = 0

codes = {1:"A",2:"NS",5:"CNAME",6:"SOA",10:"NULL",12:"PTR",13:"HINFO",15:"MX",16:"TXT",28:"AAAA",33:"SRV",41:"OPT"}
summ_of_each = {"A":0,"NS":0,"CNAME":0,"SOA":0,"NULL":0,"PTR":0,"HINFO":0,"MX":0,"TXT":0,"AAAA":0,"SRV":0,"OPT":0}

number_of_request = 0

f = open('dump')
pcap = dpkt.pcap.Reader(f)

for ts, buf in pcap: 
  eth = dpkt.ethernet.Ethernet(buf)
  ip = eth.data
  udp = ip.data
  dns = dpkt.dns.DNS(udp.data)
  for an in dns.an: 
    if an.type is not None: 
      number_of_request += 1
    if an.type is not None: 
      summ_of_each[codes[an.type]] += 1

print "\n"
for key, value in summ_of_each.items():
  print('Request {}\t has {}\t of request(s)'.format(key,value))


print ""
print "######################################"
print ""
print "The whole number of all types of request: ", number_of_request
