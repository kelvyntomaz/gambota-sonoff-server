#!/usr/bin/python3
# Mantainer: Kelvyn Tomaz <kelvyntomaz@gmail.com>

# require websocket-client
# require socketserver
# pip install websocket-client socketserver


import http.server
import socketserver
import websocket
import time
import calendar
import sys
import yaml
import os

#Importa o Config File
config = yaml.safe_load(open(os.path.join(sys.path[0],"config.yml")))

#define port for API
HOST = config['webserver']['host']
PORT = config['webserver']['port']
SONOFF_WS = "ws://{}:8081".format(config['sonoff']['sonoff_quarto']['ip'])

#Define logs
logfile = open(config['log_file'], 'a', 1)
sys.stdout = logfile
sys.stderr = logfile

#TODO: arrancar saporra
sonoff_quarto = 0

#TODO: Colocar json para pegar o estado atual https://www.w3schools.com/python/python_json.asp

ws = websocket.WebSocket()

class my_handler(http.server.BaseHTTPRequestHandler):
   def do_GET(self):
    global sonoff_quarto
    timestamp = calendar.timegm(time.gmtime())
    if self.path=="/quarto":
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        if sonoff_quarto == 0:
            print("Ligando")
            ws.send('{"action": "update", "userAgent": "RaspHome", "controlType": 4, "apikey": "7b00252c-41f5-4ca9-8624-0b388fd3b17d", "deviceid": "100077a7f3", "ts": 0, "sequence": "' + str(timestamp) + '", "params": {"switch": "on"}}')
            self.wfile.write(b"<center><h1>Ligado!</h1></center>")
            sonoff_quarto = 1
        else:
            print("Desligando")
            ws.send('{"action": "update", "userAgent": "RaspHome", "controlType": 4, "apikey": "7b00252c-41f5-4ca9-8624-0b388fd3b17d", "deviceid": "100077a7f3", "ts": 0, "sequence": "' + str(timestamp) + '", "params": {"switch": "off"}}')
            self.wfile.write(b"<center><h1>Desligado!</h1></center>")
            sonoff_quarto = 0

    elif self.path=="/liga":
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        #self.wfile.write("<center><h1>FUNFOU MLK!</h1></center>")
        print("Ligando")
        ws.send('{"action": "update", "userAgent": "RaspHome", "controlType": 4, "apikey": "7b00252c-41f5-4ca9-8624-0b388fd3b17d", "deviceid": "100077a7f3", "ts": 0, "sequence": "' + str(timestamp) + '", "params": {"switch": "on"}}')
        result =  ws.recv()
        print(result)
        sonoff_quarto = 1

    elif self.path=="/desliga":
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        #self.wfile.write("<center><h1>FUNFOU MLK!</h1></center>")
        print("Desligando")
        ws.send('{"action": "update", "userAgent": "RaspHome", "controlType": 4, "apikey": "7b00252c-41f5-4ca9-8624-0b388fd3b17d", "deviceid": "100077a7f3", "ts": 0, "sequence": "' + str(timestamp) + '", "params": {"switch": "off"}}')
        result =  ws.recv()
        print(result)
        sonoff_quarto = 0

    elif self.path=="/botao":
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(b'''<script src="http://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
        <input id="botao" type="submit" value="ESse Funfa" style="width:150px">
        <form action="/quarto" method="post">
        <input type="submit" value="gpio4 On">
        <button name="teste" value="upvote">Quarto</button>
        <script>
        $( "#botao" ).click(function() {
            $.get("/quarto")
        });</script>
        </form>''')
    else:
        self.send_response(404)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(b"<center><h1>ERRRRRROOOOOOOUUUUUUU</h1></center>")

    return


try:

    print("Conectando")
    ws.connect(SONOFF_WS)
    print("Conectado!!!!")
    timestamp = calendar.timegm(time.gmtime())
    ws.send('{"action": "update", "userAgent": "RaspHome", "controlType": 4, "apikey": "7b00252c-41f5-4ca9-8624-0b388fd3b17d", "deviceid": "100077a7f3", "ts": 0, "sequence": "' + str(timestamp) + '", "params": {"switch": "off"}}')
    result =  ws.recv()
    print(result)

    #HTTP
    httpd = socketserver.ThreadingTCPServer((HOST, PORT), my_handler)
    print("servidor web rodando na porta", PORT)
    httpd.serve_forever()


except KeyboardInterrupt:
    print("Voce pressionou ^C, encerrando...")
    httpd.socket.close()
    ws.close()
    logfile.close()

except:
    print("Morri!")
    httpd.socket.close()
    ws.close()
    logfile.close()
