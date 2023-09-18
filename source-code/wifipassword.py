import subprocess
import re
import time
from time import sleep
from colorama import Fore
from rich.console import Console
from rich.progress import track

print(Fore.LIGHTMAGENTA_EX,'''

     _              _      ____                 ____       _ _      
    / \   _ __ ___ (_)_ __|  _ \ ___ ______ _  |  _ \  ___| (_)_ __ 
   / _ \ | '_ ` _ \| | '__| |_) / _ \_  / _` | | | | |/ _ \ | | '__|
  / ___ \| | | | | | | |  |  _ <  __// / (_| | | |_| |  __/ | | |   
 /_/   \_\_| |_| |_|_|_|  |_| \_\___/___\__,_| |____/ \___|_|_|_|   
                                                                    ''')
print(Fore.LIGHTCYAN_EX,'''
        |=====================================|
        |  Programmer: AmirRezaDelir          |
        |  Email: AmirRezaDelir@hotmail.com   |
        |  Instagram: AmirReza_Delir          |
        |  https://github.com/AmirRezaDelir   |
        |=====================================| 
''')
console = Console()
console.rule("[bold Blue]App Version 1.23")
def process_data():
    sleep(0.04)
for _ in track(range(80), description='[purple]Loading...'):
    process_data()

netsh_output = subprocess.run(
    ["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode()

profile_names = (re.findall("All User Profile     : (.*)\r", netsh_output))

wifi_list = []

if len(profile_names) != 0:
    for name in profile_names:

        wifi_profile = {}

        profile_info = subprocess.run(
            ["netsh", "wlan", "show", "profile", name], capture_output=True).stdout.decode()
        if re.search("Security key           : Absent", profile_info):
            continue
        else:
            wifi_profile["ssid"] = name
            profile_info_pass = subprocess.run(
                ["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output=True).stdout.decode()
            password = re.search(
                "Key Content            : (.*)\r", profile_info_pass)
            if password == None:
                wifi_profile["password"] = None
            else:
                wifi_profile["password"] = password[1]

            wifi_list.append(wifi_profile)
print('\n')
for x in range(len(wifi_list)):
    print(Fore.GREEN,wifi_list[x],"\n")
print(Fore.BLUE,"script closes after "+Fore.RED+"30 "+Fore.BLUE+"minutes...")
time.sleep(1800)
