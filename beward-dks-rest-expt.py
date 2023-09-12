from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher

import json
import logging
import requests
from random import randint
from requests.auth import HTTPDigestAuth

from secretdata import Aleksey_id, Magomed_id


#########################################################################
BOT_TOKEN = 'YOUR TOKEN'
urlTelegram = 'https://api.telegram.org/bot' + BOT_TOKEN + '/sendMessage'
#########################################################################


# ----------------------------------- #
#     Your Bot Users List (dict.)     #
# ----------------------------------- #
door_users = {
    'Aleksey': Aleksey_id,
    'Magomed': Magomed_id,
}

#IP & Password of doorphone
#IP и Пароль домофона
IPTest = 'A.B.C.D'
PSWTest = 'your_password'


req_stat = lambda requests: True if (requests.post == 200) else False


def DoorCodeOff(IntercomIP, name, pswd):
    """
    deactivate the door open code
    деактивация кода открытия двери
    """

    r = requests.post(
        'http://' + IntercomIP + '/cgi-bin/intercom_cgi?action=set&DoorCodeActive=off',
        auth = HTTPDigestAuth(name, pswd),
        data = {
            'flag':'4600', 
            'paramchannel':'0', 
            'paramcmd':'0', 
            'paramctrl':'1', 
            'paramstep':'0', 
            'paramreserved':'0'
        }
    )

    return req_stat(r)
    

def DoorCodeOn(IntercomIP, name, pswd):
    """
    activate the door open code
    активация кода открытия двери
    """

    r = requests.post(
        'http://' + IntercomIP + '/cgi-bin/intercom_cgi?action=set&DoorCodeActive=on',\
        auth = HTTPDigestAuth(name, pswd),
        data = {
            'flag':'4600', 
            'paramchannel':'0', 
            'paramcmd':'0', 
            'paramctrl':'1', 
            'paramstep':'0', 
            'paramreserved':'0'
        }
    )

    return req_stat(r)  

def DoorOff(IntercomIP, name, pswd):
    """
    keeping the door closed (the doorphone is operating normally)
    удерживание двери закрытой (нормальный режим работы домофона)
    """

    r = requests.post(
        'http://' + IntercomIP + '/cgi-bin/intercom_cgi?action=set&MainDoorOpenMode=off',\
        auth = HTTPDigestAuth(name, pswd),\
        data = {
            'flag':'4600', 
            'paramchannel':'0', 
            'paramcmd':'0', 
            'paramctrl':'1', 
            'paramstep':'0', 
            'paramreserved':'0'
        }
    )
    
    return req_stat(r)

def DoorOn(IntercomIP, name, pswd):
    """
    keep the door open
    удерживание двери открытой
    """

    r = requests.post(
        'http://' + IntercomIP + '/cgi-bin/intercom_cgi?action=set&MainDoorOpenMode=on',
        auth = HTTPDigestAuth(name, pswd),
        data = {
            'flag':'4600', 
            'paramchannel':'0', 
            'paramcmd':'0', 
            'paramctrl':'1', 
            'paramstep':'0', 
            'paramreserved':'0'
        }
    )

    return req_stat(r)


def DoorOpen(IntercomIP, name, pswd):
    """
    opening the door
    открытие двери
    """

    r = requests.post(
        'http://' + IntercomIP + '/cgi-bin/intercom_cgi?action=maindoor',
        auth = HTTPDigestAuth(name, pswd),
        data = {
            'flag':'4600', 
            'paramchannel':'0', 
            'paramcmd':'0', 
            'paramctrl':'1', 
            'paramstep':'0', 
            'paramreserved':'0'
        }
    )

    return req_stat(r)


def GetDoorCode(IntercomIP, name, pswd):
    """
    find out the current door opening code
    узнать текущий код открытия двери
    """

    r = requests.post(
        'http://' + IntercomIP + '/cgi-bin/intercom_cgi?action=get',
        auth = HTTPDigestAuth(name, pswd),
        data = {
            'flag':'4600', 
            'paramchannel':'0', 
            'paramcmd':'0', 
            'paramctrl':'1', 
            'paramstep':'0', 
            'paramreserved':'0'
        }
    )
    
    return req_stat(r)


def ScanCodeOff(IntercomIP, name, pswd):
    """
    deactivate the key scan code
    деактивация кода сканирования ключей
    """

    r = requests.post(
        'http://' + IntercomIP + '/cgi-bin/rfid_cgi?action=set&RegCodeActive=off',
        auth=HTTPDigestAuth(name, pswd),
        data = {
            'flag':'4600', 
            'paramchannel':'0', 
            'paramcmd':'0', 
            'paramctrl':'1', 
            'paramstep':'0', 
            'paramreserved':'0'
        }
    )

    return req_stat(r)


def ScanCodeOn(IntercomIP, name, pswd):
    """
    activate the key scan code
    активация кода сканирования ключей
    """

    r = requests.post(
        'http://' + IntercomIP + '/cgi-bin/rfid_cgi?action=set&RegCodeActive=on',
        auth=HTTPDigestAuth(name, pswd),
        data = {
            'flag':'4600', 
            'paramchannel':'0', 
            'paramcmd':'0', 
            'paramctrl':'1', 
            'paramstep':'0', 
            'paramreserved':'0'
        }
    )

    return req_stat(r)


def SetNewDoorCode(IntercomIP, name, pswd):
    """
    set a new door open code
    установка нового кода открытия двери
    """

    r = requests.post(
        'http://' + IntercomIP + '/cgi-bin/intercom_cgi?action=set&DoorCode=' + str(randint(10000, 99999)),
        auth = HTTPDigestAuth(name, pswd),
        data = {
            'flag':'4600', 
            'paramchannel':'0', 
            'paramcmd':'0', 
            'paramctrl':'1', 
            'paramstep':'0', 
            'paramreserved':'0'
        }
    )

    return req_stat(r)


def SetStdDoorCode(IntercomIP, name, pswd):
    """
    set the standard (12345) door opening code
    установка стандартного (12345) кода открытия двери
    """

    r = requests.post(
        'http://' + IntercomIP + '/cgi-bin/intercom_cgi?action=set&DoorCode=12345',
        auth=HTTPDigestAuth(name, pswd),
        data = {
            'flag':'4600', 
            'paramchannel':'0', 
            'paramcmd':'0', 
            'paramctrl':'1', 
            'paramstep':'0', 
            'paramreserved':'0'
        }
    )

    if r.status_code == 200:
        DoorCodeOn(IntercomIP, name, pswd)
        return True
    else:
        return False


def SetNewScanCode(IntercomIP, name, pswd):
    """
    set a new key scan code and activate it
    установка нового кода сканирования ключей и его активация
    """

    r = requests.post(
        'http://' + IntercomIP + '/cgi-bin/rfid_cgi?action=set&RegCode=generate',
        auth = HTTPDigestAuth(name, pswd),
        data = {
            'flag':'4600', 
            'paramchannel':'0', 
            'paramcmd':'0', 
            'paramctrl':'1', 
            'paramstep':'0', 
            'paramreserved':'0'
        }
    )

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


@dp.message_handler(commands=['changedoorcode'])
async def send_changedoorcode(message: types.Message) -> None:
    """
    "/changedoorcode" command handler (change of door opening code)
    обработчик команды "/changedoorcode" (смена кода открытия двери)
    """

    if message.from_user.id in door_users.values():
        SetNewDoorCode(IPTest, 'admin', PSWTest)
        await message.reply('Новый код двери - ' + GetDoorCode(IPTest, 'admin', PSWTest)[1])
    else:
        await message.reply('Неавторизованный пользователь.'+'\n'+\
                            'Пройдите регистрацию !'+'\n')
    return


@dp.message_handler(commands=['doorcodeoff'])
async def send_doorcodeoff(message: types.Message) -> None:
    """
    "/doorcodeoff" command handler (deactivate the door opening code)
    обработчик команды "/doorcodeoff" (деактивировать код открытия двери)
    """

    if message.from_user.id in door_users.values():
        DoorCodeOff(IPTest, 'admin', PSWTest)
    else:
        await message.reply('Неавторизованный пользователь.'+'\n'+\
                            'Пройдите регистрацию !'+'\n')
    return


@dp.message_handler(commands=['doorcodeon'])
async def send_doorcodeon(message: types.Message) -> None:
    """
    "/doorcodeon" command handler (activate the door opening code)
    обработчик команды "/doorcodeon" (активировать код открытия двери)
    """

    if message.from_user.id in door_users.values():
        DoorCodeOn(IPTest, 'admin', PSWTest)
    else:
        await message.reply('Неавторизованный пользователь.'+'\n'+\
                            'Пройдите регистрацию !'+'\n')
    return


@dp.message_handler(commands=['keepclosed'])
async def send_keepclosed(message: types.Message) -> None:
    """
    "/keepclosed" command handler (keep closed)
    обработчик команды "/keepclosed" (держать закрытой)
    """

    if message.from_user.id in door_users.values():
        DoorOff(IPTest, 'admin', PSWTest)
    else:
        await message.reply(
            'Неавторизованный пользователь.' + '\n' + \
            'Пройдите регистрацию !' + '\n'
        )
    return


@dp.message_handler(commands=['keepopen'])
async def send_keepopen(message: types.Message) -> None:
    """
    "/keepopen" command handler (keep open)
    обработчик команды "/keepopen" (держать открытой)
    """

    if message.from_user.id in door_users.values():
        DoorOn(IPTest, 'admin', PSWTest)
    else:
        await message.reply(
            'Неавторизованный пользователь.' + '\n' +\
            'Пройдите регистрацию !' + '\n'
        )
    return


@dp.message_handler(commands=['open'])
async def send_open(message: types.Message) -> None:
    """
    "/open" command handler (open the door)
    обработчик команды "/open" (открыть дверь)
    """

    if message.from_user.id in door_users.values():
        DoorOpen(IPTest, 'admin', PSWTest)
    else:
        await message.reply(
            'Неавторизованный пользователь.' + '\n' +\
            'Пройдите регистрацию !' + '\n'
        )
    return


@dp.message_handler(commands=['stdpass'])
async def send_stdpass(message: types.Message) -> None:
    """
    "/stdpass" command handler (setting the standard door code)
    обработчик команды "/stdpass" (установка стандартного кода двери)
    """

    if message.from_user.id in door_users.values():
        SetStdDoorCode(IPTest, 'admin', PSWTest)
        await message.reply('Код двери - стандартный')
    else:
        await message.reply(
            'Неавторизованный пользователь.' + '\n' +\
            'Пройдите регистрацию !' + '\n'
        )
    return


def main() -> int:
    executor.start_polling(dp, skip_updates=True)
    return 0


if __name__ == '__main__':
    main()
