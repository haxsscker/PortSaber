#!/usr/bin/env python
import threading, random, sys, httplib, Queue, getopt,os,socket
try:
    import msvcrt
    is_shouhu = 1
except:
    is_shouhu = 0
    print "Is linux or have no msvcrt"

timeout = 2   
socket.setdefaulttimeout(timeout)

class ftp_saber(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)

        def check_server(self,address,port):
            self.s=socket.socket()
            try:
                print address,port
                self.s.connect((address,int(port)))
                return True
            except socket.error,e:
                return False

        def run(self):
            while 1:
                if queue.empty() == True:
                    break
                self.the_s_ip = queue.get()
                self.the_ports = self.the_s_ip[1]
                self.the_ports = self.the_ports.split('|')
                self.the_new_s_ip = self.the_s_ip[0]
                for self.the_port in self.the_ports:
                    self.check = self.check_server(self.the_new_s_ip,self.the_port)
                    if (self.check):
                        f.write(self.the_new_s_ip+" Port "+self.the_port+" is on ")
                        print "Port  %s is on" %self.the_port
                        self.check2 = self.check_server(self.the_new_s_ip,self.the_port)
                        if (self.check2):
                            f.write(" the_second_on")
                            print "the_second is on"
                        else:
                            f.write(" the_second_off ")
                        f.write("\n")

class ThreadGetKey(threading.Thread):
    def run(self):
        while 1:
            try:
                chr = msvcrt.getch()
                if chr == 'q':
                    print "stopped by your action ( q )" 
                    os._exit(1)
                else:
                    continue
            except:
                print "Is linux or have no msvcrt"
                os._exit(1)


if __name__ == '__main__':
    f = open("c:/check_open_port.txt","a+")
    ip_arr = []
    f2 = open("c:/open_port.txt","r")

    ############
    if is_shouhu:
        shouhu = ThreadGetKey()
        shouhu.setDaemon(True)
        shouhu.start()
    ##############threads start########
    threads = [] 
    queue = Queue.Queue()
    for the_ip in f2.readlines():
        queue.put(the_ip.split(","))

    f.close()

    for i in range(15):
        a = ftp_saber()
        a.start()
        threads.append(a)
    for j in threads:
        j.join()

    f2.close()
