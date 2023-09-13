from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher

import json
import logging
import requests
from random import randint
from requests.auth import HTTPDigestAuth

#########################################################################
BOT_TOKEN = 'YOUR TOKEN'
urlTelegram = 'https://api.telegram.org/bot' + BOT_TOKEN + '/sendMessage'
#########################################################################

# ----------------------------------- #
#     Your Bot Users List (dict.)     #
# ----------------------------------- #
door_users = {
'Aleksey': Aleksey_id,
'Magomed': Magomed_id
}

#IP & Password of doorphone
#IP и Пароль домофона
IPTest = 'A.B.C.D'
PSWTest = 'your_password'

#automatic key collection
#автосбор ключей
def AutoCollectKeys(IntercomIP, name, pswd, onoff):
    r = requests.post('http://' + IntercomIP + '/cgi-bin/rfid_cgi?action=set&AutoCollectKeys=' + onoff,\
                      auth=HTTPDigestAuth(name, pswd),\
                      data = {'flag':'4600', 'paramchannel':'0',\
                              'paramcmd':'0', 'paramctrl':'1',\
                              'paramstep':'0', 'paramreserved':'0'})
    if r.status_code == 200:
        return True
    else:
        return False

#deactivate the door open code
#деактивация кода открытия двери
def DoorCodeOff(IntercomIP, name, pswd):
    r = requests.post('http://' + IntercomIP + '/cgi-bin/intercom_cgi?action=set&DoorCodeActive=off',\
                      auth=HTTPDigestAuth(name, pswd),\
                      data = {'flag':'4600', 'paramchannel':'0', 'paramcmd':'0', 'paramctrl':'1', 'paramstep':'0', 'paramreserved':'0'})
    if r.status_code == 200:
        return True
    else:
        return False

#activate the door open code
#активация кода открытия двери
def DoorCodeOn(IntercomIP, name, pswd):
    r = requests.post('http://' + IntercomIP + '/cgi-bin/intercom_cgi?action=set&DoorCodeActive=on',\
                      auth=HTTPDigestAuth(name, pswd),\
                      data = {'flag':'4600', 'paramchannel':'0', 'paramcmd':'0', 'paramctrl':'1', 'paramstep':'0', 'paramreserved':'0'})
    if r.status_code == 200:
        return True
    else:
        return False

#keep the door closed (the doorphone is operating normally)
#удерживание двери закрытой (нормальный режим работы домофона)
def DoorOff(IntercomIP, name, pswd):
    r = requests.post('http://' + IntercomIP + '/cgi-bin/intercom_cgi?action=set&MainDoorOpenMode=off',\
                      auth=HTTPDigestAuth(name, pswd),\
                      data = {'flag':'4600', 'paramchannel':'0', 'paramcmd':'0', 'paramctrl':'1', 'paramstep':'0', 'paramreserved':'0'})
    if r.status_code == 200:
        return True
    else:
        return False

#keep the door open
#удерживание двери открытой
def DoorOn(IntercomIP, name, pswd):
    r = requests.post('http://' + IntercomIP + '/cgi-bin/intercom_cgi?action=set&MainDoorOpenMode=on',\
                      auth=HTTPDigestAuth(name, pswd),\
                      data = {'flag':'4600', 'paramchannel':'0', 'paramcmd':'0', 'paramctrl':'1', 'paramstep':'0', 'paramreserved':'0'})
    if r.status_code == 200:
        return True
    else:
        return False

#opening the door
#открытие двери
def DoorOpen(IntercomIP, name, pswd):
    r = requests.post('http://' + IntercomIP + '/cgi-bin/intercom_cgi?action=maindoor',\
                      auth=HTTPDigestAuth(name, pswd),\
                      data = {'flag':'4600', 'paramchannel':'0', 'paramcmd':'0', 'paramctrl':'1', 'paramstep':'0', 'paramreserved':'0'})
    if r.status_code == 200:
        return True
    else:
        return False

#find out the current door opening code
#узнать текущий код открытия двери
def GetDoorCode(IntercomIP, name, pswd):
    r = requests.post('http://' + IntercomIP + '/cgi-bin/intercom_cgi?action=get',\
                      auth=HTTPDigestAuth(name, pswd),\
                      data = {'flag':'4600', 'paramchannel':'0', 'paramcmd':'0', 'paramctrl':'1', 'paramstep':'0', 'paramreserved':'0'})
    if r.status_code == 200:
        return True, r.text[r.text.find('DoorCode')+len('DoorCode')+1:r.text.find('DoorCode')+len('DoorCode')+6]
    else:
        return False

#find out the current key scan code
#узнать текущий код сканирования ключей
def GetScanCode(IntercomIP, name, pswd):
    r = requests.post('http://' + IntercomIP + '/cgi-bin/rfid_cgi?action=get',\
                      auth=HTTPDigestAuth(name, pswd),\
                      data = {'flag':'4600', 'paramchannel':'0',\
                              'paramcmd':'0', 'paramctrl':'1',\
                              'paramstep':'0', 'paramreserved':'0'})
    if r.status_code == 200:
        return True, r.text[r.text.find('RegCode')+len('RegCode')+1:r.text.find('RegCode')+len('RegCode')+6]
    else:
        return False

#deactivate the key scan code
#деактивация кода сканирования ключей
def ScanCodeOff(IntercomIP, name, pswd):
    r = requests.post('http://' + IntercomIP + '/cgi-bin/rfid_cgi?action=set&RegCodeActive=off',\
                      auth=HTTPDigestAuth(name, pswd),\
                      data = {'flag':'4600', 'paramchannel':'0', 'paramcmd':'0', 'paramctrl':'1', 'paramstep':'0', 'paramreserved':'0'})
    if r.status_code == 200:
        return True
    else:
        return False

#activate the key scan code
#активация кода сканирования ключей
def ScanCodeOn(IntercomIP, name, pswd):
    r = requests.post('http://' + IntercomIP + '/cgi-bin/rfid_cgi?action=set&RegCodeActive=on',\
                      auth=HTTPDigestAuth(name, pswd),\
                      data = {'flag':'4600', 'paramchannel':'0', 'paramcmd':'0', 'paramctrl':'1', 'paramstep':'0', 'paramreserved':'0'})
    if r.status_code == 200:
        return True
    else:
        return False

#set a new door open code
#установка нового кода открытия двери
def SetNewDoorCode(IntercomIP, name, pswd):
    r = requests.post('http://' + IntercomIP + '/cgi-bin/intercom_cgi?action=set&DoorCode=' + str(randint(10000, 99999)),\
                      auth=HTTPDigestAuth(name, pswd),\
                      data = {'flag':'4600', 'paramchannel':'0', 'paramcmd':'0', 'paramctrl':'1', 'paramstep':'0', 'paramreserved':'0'})
    if r.status_code == 200:
        DoorCodeOn(IntercomIP, name, pswd)
        return True
    else:
        return False

#set the standard (12345) door opening code
#установка стандартного (12345) кода открытия двери
def SetStdDoorCode(IntercomIP, name, pswd):
    r = requests.post('http://' + IntercomIP + '/cgi-bin/intercom_cgi?action=set&DoorCode=12345',\
                      auth=HTTPDigestAuth(name, pswd),\
                      data = {'flag':'4600', 'paramchannel':'0', 'paramcmd':'0', 'paramctrl':'1', 'paramstep':'0', 'paramreserved':'0'})
    if r.status_code == 200:
        DoorCodeOn(IntercomIP, name, pswd)
        return True
    else:
        return False

#set a new key scan code and activate it
#установка нового кода сканирования ключей и его активация
def SetNewScanCode(IntercomIP, name, pswd):
    r = requests.post('http://' + IntercomIP + '/cgi-bin/rfid_cgi?action=set&RegCode=generate',\
                      auth=HTTPDigestAuth(name, pswd),\
                      data = {'flag':'4600', 'paramchannel':'0', 'paramcmd':'0', 'paramctrl':'1', 'paramstep':'0', 'paramreserved':'0'})
    if r.status_code == 200:
        ScanCodeOn(IntercomIP, name, pswd)
        return True
    else:
        return False



# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


##"/changedoorcode" command handler (change of door opening code)
##обработчик команды "/changedoorcode" (смена кода открытия двери)
@dp.message_handler(commands=['changedoorcode'])
async def send_changedoorcode(message: types.Message):
    if message.from_user.id in door_users.values():
        SetNewDoorCode(IPTest, 'admin', PSWTest)
        await message.reply('Новый код двери - ' + GetDoorCode(IPTest, 'admin', PSWTest)[1])
    else:
        await message.reply('Неавторизованный пользователь.'+'\n'+\
                            'Пройдите регистрацию !'+'\n')

##"/doorcodeoff" command handler (deactivate the door opening code)
##обработчик команды "/doorcodeoff" (деактивировать код открытия двери)
@dp.message_handler(commands=['doorcodeoff'])
async def send_doorcodeoff(message: types.Message):
    if message.from_user.id in door_users.values():
        DoorCodeOff(IPTest, 'admin', PSWTest)
    else:
        await message.reply('Неавторизованный пользователь.'+'\n'+\
                            'Пройдите регистрацию !'+'\n')

##"/doorcodeon" command handler (activate the door opening code)
##обработчик команды "/doorcodeon" (активировать код открытия двери)
@dp.message_handler(commands=['doorcodeon'])
async def send_doorcodeon(message: types.Message):
    if message.from_user.id in door_users.values():
        DoorCodeOn(IPTest, 'admin', PSWTest)
    else:
        await message.reply('Неавторизованный пользователь.'+'\n'+\
                            'Пройдите регистрацию !'+'\n')

##"/keepclosed" command handler (keep closed)
##обработчик команды "/keepclosed" (держать закрытой)
@dp.message_handler(commands=['keepclosed'])
async def send_keepclosed(message: types.Message):
    if message.from_user.id in door_users.values():
        DoorOff(IPTest, 'admin', PSWTest)
    else:
        await message.reply('Неавторизованный пользователь.'+'\n'+\
                            'Пройдите регистрацию !'+'\n')

##"/keepopen" command handler (keep open)
##обработчик команды "/keepopen" (держать открытой)
@dp.message_handler(commands=['keepopen'])
async def send_keepopen(message: types.Message):
    if message.from_user.id in door_users.values():
        DoorOn(IPTest, 'admin', PSWTest)
    else:
        await message.reply('Неавторизованный пользователь.'+'\n'+\
                            'Пройдите регистрацию !'+'\n')

##"/open" command handler (open the door)
##обработчик команды "/open" (открыть дверь)
@dp.message_handler(commands=['open'])
async def send_open(message: types.Message):
    if message.from_user.id in door_users.values():
        DoorOpen(IPTest, 'admin', PSWTest)
    else:
        await message.reply('Неавторизованный пользователь.'+'\n'+\
                            'Пройдите регистрацию !'+'\n')

##"/stdpass" command handler (setting the standard door code)
##обработчик команды "/stdpass" (установка стандартного кода двери)
@dp.message_handler(commands=['stdpass'])
async def send_stdpass(message: types.Message):
    if message.from_user.id in door_users.values():
        SetStdDoorCode(IPTest, 'admin', PSWTest)
        await message.reply('Код двери - стандартный')
    else:
        await message.reply('Неавторизованный пользователь.'+'\n'+\
                            'Пройдите регистрацию !'+'\n')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
