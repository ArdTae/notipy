# 1hour = 3600 Second
# 1day = 86400 second
instbag = open("/storage/emulated/0/Word/WordFile/notification/installation_bag.sh", mode = 'r')
print(instbag)
from progress.bar import ChargingBar
chbar = ChargingBar("Processing:", max=100)
for i in range(10):
    import os
    import datetime
    import time
    import threading
    import psutil
    import platform
    import vk_api
    import banners
    from colorama import init
    from colorama import Fore, Back, Style
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
    class C:
        a = Fore.GREEN
        b = Fore.RED
        c = Fore.WHITE
        d = Fore.BLUE
    class System:
        clear = "clear"
    class Name:
        name = C.b+ "@RokSkr"
        enter = C.a+ "."
        
    class Error:
        time = "/// False /// Time's up"  
    
    class Log:
        war = "/// Login Warning ///"
        selh = "Selected /// hour"
        seld = "Selected /// day"
        succ = "                               | /// Successfully /// [/turn]"
        settings_autodel = "/// Delete a file after use?[Y/N]///"
        final = "---------------Final logs---------------"
    class Vkb:
        banner = "[send] Send post [log] Log out of all sessions [del] Delete account [all] All action"
        send_message = "[str] Standard message [mes] Your message"
        
chbar.next()
time.sleep(1)
for i in range(49):
    uname = platform.uname()
    dt = datetime.datetime.now()
    sys = os.system
    ors = os.getcwd() + "/notipy.py"
    chbar.next()
    
    
    htimep1 = C.a + "You can enter a command in 1 minute"
    dtime = C.a + "After one day, you need to enter [/turn]"
    
    
    
    
    
    delmenu = ""
    final_print = ""
    Successfully = "Successfully worked"
    delete = "delete"
    second = "Seconds left: "
    vkmesspoint = ""
    vktoc = 0
    
    htime = 0
    dtime = 0
    vk1 = 0
    tg = 0
    yt = 0
       
    vkaut = 0   
    
    system_variable = 0
    enter = ""
    
time.sleep(1) 
for i in range(1):
    chbar.next()
time.sleep(1)

chbar.finish()
logger.info(Log.settings_autodel)
settings_autodel = input("Enter: ")
sys(System.clear)



            



















logger.info(Log.war)
print(C.a + banners.notipy_banner)
print(C.a + banners.enter_banner, uname.system, uname.node)
print(C.a + banners.enter_banner, uname.release, uname.version)
print(C.a + banners.enter_banner, uname.machine, uname.processor)
print(C.a + banners.enter_banner," Enter time: ")
print(C.a + banners.enter_banner, "[day] one day, [hour] one hour, [other] other time [set] settings")



umenu = input("Enter:                             | ")
if umenu == "hour":

    

    logger.info(Log.selh)
    print(C.a + banners.notipy_banner, Name.name)
    print(C.a + banners.setm)
    houpm = input("Enter: ")
    if houpm == "vk":
        print("Vk")
        vklogin = input("Enter login: ")
        vkpass = input("Enter password: ")
        vk_session = vk_api.VkApi(vklogin, vkpass)
        vk_session.auth()
        vk = vk_session.get_api()
        print(Vkb.banner)
        
        vkban = input ("Enter: ")
        if vkban == "send":
            print(Vkb.send_message)
            vk_send = input("Enter: ")
            if vk_send == "str":
                vkmesspoint = "stme"
        
            if vk_send == "mes":
                vkmesspoint = "mes"
                vkyoumess = input("Enter message: ")
                
    if houpm == "delf":
        delmenu = input("Enter: ")
        if os.path.isfile(delmenu):
            print("Found")
            
    if houpm == "tg":
        print("tg")
            
    if houpm == "all":
        
        print("vk")
        vklogin = input("Enter login: ")
        vkpass = input("Enter password: ")
        vk_session = vk_api.VkApi(vklogin, vkpass)
        vk_session.auth()
        vk = vk_session.get_api()
        print(Vkb.banner)
        
        vkban = input ("Enter: ")
        if vkban == "send":
            print(Vkb.send_message)
            
            if vkmess == "str":
                vkmesspoint = "stme"
        
            if vkmess == "mes":
                vkmesspoint = "mes"
                vkyoumess = input("Enter message: ")
        time.sleep(3)
        print("tg")
        time.sleep(3)
        print("Yt")
        time.sleep(3)
        print("delete files")
        delmenu = input("Enter: ")
        if os.path.isfile(delmenu):
            print("Found")
        
        
    time.sleep(5)
    while htime<10:
        print(C.a + banners.notipy_banner, Name.name)
        htime = htime +1
        print(C.a + banners.hpost, htime)
        
        time.sleep(1)
        sys(System.clear)
    else:
        print(C.a + banners.notipy_banner, Name.name)
        print(C.a + banners.up10)
        
    time.sleep(10)
    
    def hoti():
        
        logger.error(Error.time)
        if vkmesspoint == "mes":
            final_print = "Wrongly [hour] [time up] [mes]"
            print(vk.wall.post(message=vkyoumess))
            print("Send message(", vkyoumess, ")")
        if vkmesspoint == "str":
            final_print = "Wrongly [hour] [time up] [str]"
            print(vk.wall.post(message=banners.standvkmess))
            print("Send message (Standard message)")
        if os.path.isfile(delmenu):
            final_print = "Wrongly [hour] [time up] [del]"
            os.remove(delmenu)
            print("A file was deleted (" , delmenu, ")")
            
            
    timer = threading.Timer(10, hoti, args=None, kwargs=None)
    timer.start()
    
    hmenu = input("Enter:                             | ")
    
    if hmenu == "/turn":
        timer.cancel()
        logger.info(Log.succ)
        final_print = "Successful [hour] [",houpm,"]"
        
        
        
if umenu == "day":





    logger.info(Log.seld)
    print(C.a + banners.notipy_banner, Name.name)
    time.sleep(2)
    while dtime<10:
        print(C.a + banners.notipy_banner, Name.name)
        dtime = dtime +1
        print(banners.hpost, dtime)
        time.sleep(1)
        sys(System.clear)
    else:
        print(C.a + banners.notipy_banner, Name.name)
        print(C.a + banners.up10)
    time.sleep(10)
    
    
    def dati():
        logger.error(Error.time)
    datimer = threading.Timer(10, dati, args=None, kwargs=None)
    datimer.start()

    daymenu = input("Enter:                             | ")
    
    if daymenu == "/turn":
        datimer.cancel()
        logger.info("                               | ", Log.succ)
        final_print = "Successful [day] []"

      
    
if umenu == "other":
    print(banners.other_banner)
    other_menu = int(input("Enter: "))
    other_menu1 = other_menu
    while other_menu > 0:
        print(C.a + banners.notipy_banner, Name.name)
        other_menu = other_menu - 1
        print(C.a + second, other_menu)
        time.sleep(1)
        sys(System.clear)
    print("Successful")
    sys(System.clear)
    final_print = "Successful [other] [", other_menu1, "s.]"
 
 
 
 
#почта   
if umenu == "ma":
    print(C.a + banners.notipy_banner, Name.name)
    print(C.a + banners.mailba)
    print(banners.mail_banner)
    mail_menu = input("Enter: ")
    if mail_menu == "se":
        print("mail send")
        print(C.a + banners.notipy_banner, Name.name)
        






if umenu == "set":
    print(banners.seth)
    print("Commands: ")
    print(banners.setm)
    setmenu = input("Enter: ")
    if setmenu == "vk":
        
        
        
        
        
        
        
        
        
        vkaut = vkaut + 1
        vk1 = vk1 + 1
        sys(System.clear)
#Конечный print(Y)
if settings_autodel == "Y":
    print(C.a + banners.notipy_banner, Name.name)
    print(C.a + Log.final)
    print("Delete")
    print(ors)
    print(final_print)
#Конечный print(N)
if settings_autodel == "N":
    print(C.a + banners.notipy_banner, Name.name)
    print(C.a + Log.final)
    print("No line found/you selected 'N'")
    print(final_print)