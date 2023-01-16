import webbrowser
import time 

my_sit = ["https://www.youtube.com/channel/UC1uHwQYaxnLtMOgv6Dn-nbw"]

while True: 
    for i in my_sit:
        webbrowser.open(i)
        time.sleep(10)