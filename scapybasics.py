from scapy.all import *

#Reading a pcap
packets = rdpcap('HTTP_Traffic_mini.pcap')


count=0
DNScount=0
for packet in packets[0:5]:
    hexoutput=':'.join(a.encode('hex') for a in str(packet))
    count+=1
    print "Packet: "+str(count) 
    print "Hex output\n"+hexoutput  #print each output in hex
    print "\nSummary of packet\n"+packet.summary()  #print summary of each packet
    print "\nComplete detail of packet\n"+str(packet.show())    #print complete details of each packet
    if packet.haslayer(DNS):    #check if DNS packet
        print "Packet has DNS packet"

    if packet.haslayer(DNSRR): #print domain name
        if isinstance(packet.an, DNSRR):
            print "Domain Name:  "+packet.an.rrname



