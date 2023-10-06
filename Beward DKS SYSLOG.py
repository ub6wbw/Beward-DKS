import json
import requests
import socket
import time
from requests.auth import HTTPDigestAuth

BOT_TOKEN = ''
urlTelegram = 'https://api.telegram.org/bot' + BOT_TOKEN + '/sendMessage'

IPDoorphone = 'a.b.c.d'
PSWDoorphone = ''

TELEGRAM_ID = ''

# Screenshot method (saves the * .jpg file to the code folder)
def ScreenShot(IntercomIP, name, pswd):
    r = requests.get('http://' + IntercomIP +\
                      '/cgi-bin/images_cgi?channel=0' +\
                      '&user=' + name + '&pwd=' + pswd)
    if r.status_code == 200:
        file_name = str(int(time.time())) + '.jpg'
        f = open(file_name, 'wb')
        f.write(r.content)
        f.close()
        return file_name, True
    else:
        return False

# A TCP based server
serverSocket = socket.socket();

# Bind the IP address and the port number
serverSocket.bind((IPDoorphone, 32002))

# Listen for incoming connections
serverSocket.listen()

# Start accepting client connections
while(True):
    (clientSocket, clientAddress) = serverSocket.accept()
    data = clientSocket.recv(1024)
    clientSocket.close()
    print(data.decode())

    if 'door' in data.decode():
        files = {'photo': open(ScreenShot(IPDoorphone, 'admin', PSWDoorphone)[0], 'rb')}
        requests.post(f'https://api.telegram.org/bot' + BOT_TOKEN + '/sendPhoto?'+\
                          'chat_id=' + TELEGRAM_ID, files=files)

    elif 'Detected RFID key' in data.decode():
        files = {'photo': open(ScreenShot(IPDoorphone, 'admin', PSWDoorphone)[0], 'rb')}
        requests.post(f'https://api.telegram.org/bot' + BOT_TOKEN + '/sendPhoto?'+\
                          'chat_id=' + TELEGRAM_ID, files=files)

    elif 'Doors unlock switch is' in data.decode():
        files = {'photo': open(ScreenShot(IPDoorphone, 'admin', PSWDoorphone)[0], 'rb')}
        requests.post(f'https://api.telegram.org/bot' + BOT_TOKEN + '/sendPhoto?'+\
                          'chat_id=' + TELEGRAM_ID, files=files)
        
    elif 'is not present in database' in data.decode():
        files = {'photo': open(ScreenShot(IPDoorphone, 'admin', PSWDoorphone)[0], 'rb')}
        requests.post(f'https://api.telegram.org/bot' + BOT_TOKEN + '/sendPhoto?'+\
                          'chat_id=' + TELEGRAM_ID, files=files)

    elif 'Opening door by service door code' in data.decode():
        files = {'photo': open(ScreenShot(IPDoorphone, 'admin', PSWDoorphone)[0], 'rb')}
        requests.post(f'https://api.telegram.org/bot' + BOT_TOKEN + '/sendPhoto?'+\
                          'chat_id=' + TELEGRAM_ID, files=files)
        
    elif 'SS_MAINAPI_ReportAlarmFinish' in data.decode():
        files = {'photo': open(ScreenShot(IPDoorphone, 'admin', PSWDoorphone)[0], 'rb')}
        requests.post(f'https://api.telegram.org/bot' + BOT_TOKEN + '/sendPhoto?'+\
                          'chat_id=' + TELEGRAM_ID, files=files)
        
    elif 'SS_MAINAPI_ReportAlarmHappen'in data.decode():
        files = {'photo': open(ScreenShot(IPDoorphone, 'admin', PSWDoorphone)[0], 'rb')}
        requests.post(f'https://api.telegram.org/bot' + BOT_TOKEN + '/sendPhoto?'+\
                          'chat_id=' + TELEGRAM_ID, files=files)
    data = None
    
serverSocket.close()
