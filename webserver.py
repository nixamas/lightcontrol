#Copyright Jon Berg , turtlemeat.com

import string,cgi,time,lightcontrol as LC,urlparse
from os import curdir, sep
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
#import pri

class MyHandler(BaseHTTPRequestHandler):
    myLightControl = LC.LightControl()
    def do_GET(self):
        print "recieved a get command :: " + str(self.path)
        parsed_path = urlparse.urlparse(self.path)
        try:
            params = dict([p.split('=') for p in parsed_path[4].split('&')])
        except:
            params = {}

        if params:
            print "params exist"

            print "first element ::: " + params["lights"]
            num = 0
            if params["lights"] == "1":
                print "lights :: 1"
                num = 1
            elif params["lights"] == "2":
                print "lights :: 2"
                num = 2
            elif params["lights"] == "3":
                print "lights :: 3"
                num = 3
            elif params["lights"] == "4":
                print "lights :: 4"
                num = 4
            elif params["lights"] == "5":
                print "lights :: 5"
                num = 5
            else:
                print "lights :: 0"
                num = 0
            
            self.myLightControl.setLights(num)

        else:
            print "params does not exist"


        print "params :: " + str(params)
        try:
            if self.path[0] == "/":
                print "1st 11 :: " + self.path[0:11]
                if self.path[0:11] == "/index.html" and params != None:
                    print "index.html"
                    f = open(curdir + sep + "index.html")
                    self.send_response(200)
                    self.send_header('Content-type','text/html')
                    self.end_headers()
                    self.wfile.write(f.read())
                    f.close()
                elif self.path[0:11] == "/index.html" and params:
                    self.send_response(200)
                    self.send_header('Content-type','text/html')
                    self.end_headers()
                else:
                    print "file request, no index.html"
                    f = open(curdir + self.path)
                    self.send_response(200)
                    self.send_header('Content-type','text/html')
                    self.end_headers()
                    self.wfile.write(f.read())
                    f.close()
                return
            if self.path.endswith(".html") or params:
                #f = open(curdir + sep + self.path) #self.path has /test.html
#note that this potentially makes every file on your computer readable by the internet
                f = open(curdir + sep + "index.html")
                self.send_response(200)
                self.send_header('Content-type',	'text/html')
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
                return
            if self.path.endswith(".esp"):   #our dynamic content
                self.send_response(200)
                self.send_header('Content-type',	'text/html')
                self.end_headers()
                self.wfile.write("hey, today is the" + str(time.localtime()[7]))
                self.wfile.write(" day in the year " + str(time.localtime()[0]))
                lightcontrol.turnOnOneLight()
                return
            if self.path.endswith(".css"):
                print "recieved request for .css"
                c = open(curdir + sep + "blueCSS.css")
                self.send_response(200)
                self.send_header('Content-type','text/css')
                self.end_headers()
                self.wfile.write(c.read())
                c.close()
                return
            return
        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)
     

    def do_POST(self):
        global rootnode
        try:
            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                query=cgi.parse_multipart(self.rfile, pdict)
            self.send_response(301)
            
            self.end_headers()
            upfilecontent = query.get('upfile')
            print "filecontent", upfilecontent[0]
            self.wfile.write("<HTML>POST OK.<BR><BR>");
            self.wfile.write(upfilecontent[0]);
            
        except :
            pass

def main():
    try:
        server = HTTPServer(('', 80), MyHandler)
        print 'started httpserver...'
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        pass

def main():
    try:
        server = HTTPServer(('', 80), MyHandler)
        print 'started httpserver...'
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()

if __name__ == '__main__':
    main()
