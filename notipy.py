# 1hour = 3600 Second
# 1day = 86400 second

login = 1

import datetime
import time
import threading
from loguru import logger
from progress.bar import ChargingBar
dt = datetime.datetime.now()
chbar = ChargingBar('Processing:', max=100)
for i in range(10):
    chbar.next()
time.sleep(1)
for i in range(10):
    chbar.next()
time.sleep(1)
for i in range(25):
    chbar.next()
time.sleep(1) 
for i in range(5):
    chbar.next()
time.sleep(1)
for i in range(49):
    chbar.next()
time.sleep(1) 
for i in range(1):
    chbar.next()
time.sleep(1)
chbar.finish()




print(dt)
print("Введите через какое время: ")
print("[day] one day, [hour] one hour, [other] other time [log] Enable logging mode")




umenu = input("Enter: ")
if umenu == "hour":



    logger.info("Был выбран /// hour")
    print("Через один час вам нужно будет написать [/turn]")
    print("Возможность ввести команду будет доступна за 1 минуту")
    time.sleep(3540)
    def hoti():
        logger.error("/// Ошибочно /// Время вышло")
    
    timer = threading.Timer(60, hoti, args=None, kwargs=None)
    timer.start()
    
    hmenu = input("Enter: ")
    
    if hmenu == "/turn":
        timer.cancel()
        logger.info("/// Успешно /// [/turn]")
        
        
        
        
if umenu == "day":





    logger.info("Был выбран /// day")
    print("Через один день вам нужно будет написать [/turn]")
    print("Возможность ввести команду будет доступна за 1 минуту")
    time.sleep(86340)
    def dati():
        logger.error("/// Ошибочно /// Время вышло")
    datimer = threading.Timer(60, dati, args=None, kwargs=None)
    datimer.start()

    daymenu = input("Enter: ")
    
    if daymenu == "/turn":
        datimer.cancel()
        logger.info("/// Успешно /// [/turn]")
        
        
        
if umenu == "other":
    print("Введите количество секунд(больше 60): ")
    second = input("Enter: ")
    if second < 60:
        print("Вы ввели меньше 60")
    selected_second = second - 60
    time.sleep(selected_second)
    
    def otherm():
        logger.error("/// Ошибочно /// Время вышло")
    
    
    other_timer = threading.Timer(60, dati, args=None, kwargs=None)
    other_timer.start()
    
    othermen = input ("Enter: ")
    
    if othermen == "/turn":
        other_timer.cancel()
        logger.info("/// Успешно /// [/turn]")
        
        
        
        
        
        
if umenu == "log":
    logger.error("Внимание, это отключить не получится")
    print("Вы включаете созранение логов в файл ['debug_noti.log']")
    logmenu = input("Enter(Y/N): ")
    if logmenu == "Y":
        logger.add("debug_noti.log",format = "{time} {level} {message}", level = "DEBUG")
        logger.info("/// Успешно включён /// log")
    if logmenu == "N":
        logger.info("/// Вы успешно вышли /// log")
