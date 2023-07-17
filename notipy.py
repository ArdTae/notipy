# 1hour = 3600 Second
# 1day = 86400 second

from progress.bar import ChargingBar
chbar = ChargingBar('Processing:', max=100)
for i in range(10):
    import datetime
    import time
    import threading
    import psutil
    import platform
    from loguru import logger
    chbar.next()
time.sleep(1)
for i in range(10):
    chbar.next()
time.sleep(1)
for i in range(25):
    logger.add("debug_notipy.log",format = "{time} {level} {message}", level = "DEBUG")
    chbar.next()
time.sleep(1) 
for i in range(5):
    chbar.next()
time.sleep(1)
for i in range(49):
    uname = platform.uname()
    dt = datetime.datetime.now()
    chbar.next()
time.sleep(1) 
for i in range(1):
    chbar.next()
time.sleep(1)
chbar.finish()


logger.info("/// Login Warning ///")
print("___________________________________| ")
print("     /   \   /   \   /   \         | ", dt)
print("     n   o   t   i   p   y         | ", uname.system, uname.node, )
print("     /   \   /   \   /   \         | ", uname.release, )
print("———————————————————————————————————| ", uname.machine, uname.processor, uname.version)

print("                                   | ")
print("                                   | Enter time: ")
print("                                   | [day] one day, [hour] one hour, [other] other time")




umenu = input("Enter:                             | ")
if umenu == "hour":



    logger.info("Selected /// hour")
    print("                                   | After an hour, you need to enter [/turn]")
    print("                                   | You can enter a command in 1 minute")
    time.sleep(10)
    def hoti():
        logger.error("/// False /// Time's up")
    
    timer = threading.Timer(10, hoti, args=None, kwargs=None)
    timer.start()
    
    hmenu = input("Enter:                             | ")
    
    if hmenu == "/turn":
        timer.cancel()
        logger.info("                               | /// Успешно /// [/turn]")
        
        
        
        
if umenu == "day":





    logger.info("Selected /// day")
    print("                                   | After one day, you need to enter [/turn]")
    print("                                   | You can enter a command in 1 minute")
    time.sleep(10)
    def dati():
        logger.error("/// False /// Time's up")
    datimer = threading.Timer(10, dati, args=None, kwargs=None)
    datimer.start()

    daymenu = input("Enter:                             | ")
    
    if daymenu == "/turn":
        datimer.cancel()
        logger.info("                               | /// Успешно /// [/turn]")
        
        
        
if umenu == "other":
    print("                               | Введите количество секунд(больше 60): ")
    second = input("Enter: ")
    if second < 60:
        print("                              | Вы ввели меньше 60")
    selected_second = second - 60
    time.sleep(selected_second)
    
    def otherm():
        logger.error("/// Ошибочно /// Время вышло")
    
    
    other_timer = threading.Timer(60, dati, args=None, kwargs=None)
    other_timer.start()
    
    othermen = input ("Enter:                        | ")
    
    if othermen == "/turn":
        other_timer.cancel()
        logger.info("/// Успешно /// [/turn]")
        
     