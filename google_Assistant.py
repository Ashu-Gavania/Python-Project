from os import system
import webbrowser
from sys import exit
import urllib.request
import re
#import subprocess
#from pyttsx3 import speak
#speak("Hello Guest!! Please enter your choice Number for open program ")
web=["https://www.google.com/", "https://www.youtube.com/"]
print("Ramu Kaka : Hi , how can i help")
while True:
 p=input("You  : ")
 p=p.lower()
 #search_keyword=str(p)
 if ((("run" in p) or ("start" in p) or ("open" in p )or ("execute" in p) or ("launch" in p)) and (("notepa" in p) or ("editor" in p))) and ((("don't" not in p) and ("dont" not  in p )and ("not " not  in p ))):
    system("start notepad")      
    print("Ramu Kaka : Program has been opened sir")
 elif ((("run" in p) or ("start" in p) or ("open" in p ) or ("execute" in p) or ("launch" in p)) and (("chrom" in p) or ("browser" in p))) and (("don't" not in p) and ("dont" not  in p )and ("not " not  in p )):
    system("start chrome")
    print("Ramu Kaka : Program has been opened sir")
 elif ((("run" in p) or ("start" in p) or ("open" in p ) or ("execute" in p) or ("launch" in p)) and ("python" in p)) and (("don't" not in p) and ("dont" not  in p )and ("not " not  in p )):
    system("start python")
    print("Ramu Kaka : Program has been opened sir")
 elif ((("run" in p) or ("start" in p) or ("open" in p ) or ("execute" in p)or ("play" in p) or ("launch" in p)) and (("media player" in p)or ("window media" in p))) and (("don't" not in p) and ("dont" not  in p )and ("not " not  in p )):
    system("start wmplayer")
    print("Ramu Kaka : Program has been opened sir")
 elif ((("run" in p) or ("start" in p) or ("open" in p ) or ("execute" in p) or ("launch" in p)) and (("ie" in p )or ("internet exp") in p ))and (("don't" not in p) and ("dont" not  in p )and ("not " not  in p )):
    system("start iexplore")
    print("Ramu Kaka : Program has been opened sir")
 elif ((("run" in p) or ("start" in p) or ("open" in p ) or ("execute" in p) or ("launch" in p)) and (("paint" in p ))) and (("don't" not in p) and ("dont" not  in p )and ("not " not  in p )):
    system("start mspaint")
    print("Ramu Kaka : Program has been opened sir")
 elif ((("run" in p) or ("start" in p) or ("open" in p )or ("execute" in p) or ("launch" in p)) and (("word" in p ) or ("microsoft wor" in p ) )) and (("don't" not in p) and ("dont" not  in p )and ("not " not  in p )):
    system("start WINWORD")
    print("Ramu Kaka : Program has been opened sir")
 elif ((("run" in p) or ("start" in p) or ("open" in p )or ("execute" in p) or ("launch" in p)) and (("excel" in p ) or ("microsoft exce" in p ))) and (("don't" not in p) and ("dont" not  in p )and ("not " not  in p )):
    system("start EXCEL")
    print("Ramu Kaka : Program has been opened sir")
 elif ((("run" in p) or ("start" in p) or ("open" in p ) or ("execute" in p) or ("launch" in p)) and (("powerpoint" in p )or ("ppt" in p ) )) and (("don't" not in p) and ("dont" not  in p )and ("not " not  in p )):
    system("start POWERPNT")
    print("Ramu Kaka : Program has been opened sir")
 elif ((("run" in p) or ("start" in p) or ("open" in p )or ("execute" in p) or ("launch" in p)) and (("adobe" in p ))) and (("don't" not in p) and ("dont" not  in p )and ("not " not  in p )):
    system("start acrord32")
    print("Ramu Kaka : Program has been opened sir")
 elif ((("run" in p) or ("start" in p) or ("open" in p ) or ("execute" in p) or ("launch" in p)) and (("control pane" in p ))) and (("don't" not in p) and ("dont" not  in p )and ("not " not  in p )):
    system("start control")
    print("Ramu Kaka : Program has been opened sir")
 elif ((("run" in p) or ("start" in p) or ("open" in p )or ("execute" in p) or ("launch" in p)) and (("network settin" in p ))) and (("don't" not in p) and ("dont" not  in p )and ("not " not  in p )):
    system("start ncpa.cpl")
    print("Ramu Kaka : Program has been opened sir")
 elif ((("run" in p) or ("start" in p) or ("open" in p ) or ("execute" in p)) and (("printer" in p ))) and (("don't" not in p) and ("dont" not  in p )and ("not " not  in p )):
    system("start control printers")
    print("Ramu Kaka : Program has been opened sir")
 elif ((("run" in p) or ("start" in p) or ("open" in p ) or ("execute" in p) or ("launch" in p))  and (("device manage" in p ))) and (("don't" not in p) and ("dont" not  in p )and ("not " not  in p )):
    system("start devmgmt.msc")
    print("Ramu Kaka : Program has been opened sir")
 elif ((("run" in p) or ("start" in p) or ("open"  in p )or ("execute" in p) or ("launch" in p)) and (("disk mgmt" in p ) or ("disk manage" in p ))) and (("don't" not in p) and ("dont" not  in p )and ("not " not  in p )):
    system("start diskmgmt.msc")
    print("Ramu Kaka : Program has been opened sir")
 elif ((("run" in p) or ("start" in p) or ("open" in p ) or ("execute" in p) or ("launch" in p)) and (("calculator" in p ) )) and (("don't" not in p) and ("dont" not  in p )and ("not " not  in p )):
    system("start calc")
    print("Ramu Kaka : Program has been opened sir")
 elif ((("run" in p) or ("start" in p) or ("open" in p ) or ("execute" in p) or ("launch" in p)) and (("remote desk" in p ))) and (("don't" not in p) and ("dont" not  in p )and ("not " not  in p )):
    system("start mstsc")
    print("Ramu Kaka : Program has been opened sir")
 elif ((("shut" in p) or ("poweroff" in p) or ("turnoff") in p ) and (("pc" in p ) or ("laptop" in p ) or ("computer" in p ) or ("system" in p ))) and (("don't" not in p) and ("dont" not  in p )and ("not " not  in p )):
    system("SHUTDOWN /i")
    print("Ramu Kaka : Shutdown in progress sir..")
 elif ((("logoff" in p) or ("log off" in p) or ("sign off ") in p or ("sigoff" in p)) and (("pc" in p ) or ("laptop" in p ) or ("computer" in p ) or ("system" in p ))) and (("don't" not in p) and ("dont" not  in p )and ("not " not  in p )):
    system("SHUTDOWN /l")
    print("Ramu Kaka : Signing off.")
 elif ((("reboot" in p) or ("restart" in p)) and (("pc" in p ) or ("laptop" in p ) or ("computer" in p ) or ("system" in p ))) and (("don't" not in p) and ("dont" not  in p )and ("not " not  in p )):
    system("SHUTDOWN /r")
    print("Ramu Kaka : reboot in progress")
 elif ((("lock" in p)) and (("pc" in p ) or ("laptop" in p ) or ("computer" in p ) or ("system" in p ))) and (("don't" not in p) and ("dont" not  in p )and ("not " not  in p )):
    system("rundll32.exe user32.dll,LockWorkStation")
    print("Ramu Kaka : System has been locked")
 elif ((("start" in p) or ("open" in p) ) and (("explorer" in p ) or ("file expl" in p ))) and (("don't" not in p) and ("dont" not  in p )and ("not " not  in p )):
    system("start explorer") 
    print("Ramu Kaka : Program has been opened sir")
 elif ((("start" in p) or ("open" in p) or ("run" in p ) or ("launch" in p)) and (("putty" in p ))) and (("don't" not in p) and ("dont" not  in p )and ("not " not  in p )):
    system("start putty") 
    print("Ramu Kaka : Program has been opened sir")  
 elif ("thanks" in p) or ("thank you" in p) or ("thank" in p):
    print("Ramu Kaka : Its my Pleasure Sir :)")
 elif (len(p)==0):
    print("Ramu Kaka : I Haven't received any input from you Sir!!")
 elif (("weather" in p ) or ("temperature" in p) or ("temprature" in p)) and (("don't" not in p) and ("dont" not  in p )and ("not " not  in p )):
    search_keyword=str(p)
    webbrowser.open('http://www.google.com/search?btnG=1&q=%s'%search_keyword)
 elif (("music" in p ) or ("movie" in p) or ("song" in p) or ("comedy" in p)) and (("play" in p)) and (("don't" not in p) and ("dont" not  in p )and ("not " not  in p ))  :
    print("Ramu Kaka : Here is your some option in youtube sir!!")
    search_keyword=str(p)
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" +(str(re.sub("[ ]", "+", search_keyword))))
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    url=('https://www.youtube.com/watch?v=' + video_ids[0])
    webbrowser.open_new(url)
 elif (("hi" in p ) or ("hello" in p) or ("helooo" in p) or ("hey" in p)) and (("don't" not in p) and ("dont" not  in p )and ("not " not  in p )):
    print("Ramu Kaka : Hi, what  can i do for you ?")
 elif (( "Ok" in p) or ("okay" in p)):
    print("Ramu Kaka : :)")
 elif (("annoy" in p ) or ("anger" in p) or ("bother" in p) or ("irritate" in p) or ("angry" in p)) and (("don't" in p) or ("dont"   in p )or ("not "   in p )):
    print("Ramu Kaka : I'm sorry to hear that. i'll do better next time?")
 elif ("exit" in p) or ("quit" in p) or ("terminate" in p) or ("bye" in p):
    print("Ramu Kaka :Thank you Sir!!! We are always here for your help!!")
    break  
 else:
    print("Ramu Kaka : Here what i found on web about",p,"!!")
    search_keyword=str(p)
    webbrowser.open('http://www.google.com/search?btnG=1&q=%s'%search_keyword)
