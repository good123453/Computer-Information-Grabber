import psutil
import platform
import socket
from pyfiglet import Figlet
from termcolor import colored



# absraction block: information much enhancer minimal clean and clear
def line(text, extra_line = "") -> None: 
    print("=" * 50)
    print(text)
    print("=" * 50)
    if extra_line == "\n":
        print()
    else:
        print("", end="")
        
        
        
def Banner(text="enter the text",fonts="ne",color="white"):
    
    coloroption = {"y": "light_yellow",
                    "b": "light_blue",
                    "c": "light_cyan",
                    "g": "light_green",
                    "m": "light_magenta",
                    "r": "light_red"}
    
    fonts_mapping = {"ne": "big_money-ne",
                     "nw": "big_money-nw",
                     "se": "big_money-se",
                     "sw": "big_money-sw"}
    
    f = Figlet(font=fonts_mapping.get(fonts, "big_money-ne"))
    
    colors = coloroption.get(color, "white")
    font_text = f.renderText(text)
    print(colored(font_text, colors))


Banner("COMPUTER INFORMATION GRABBER")
   

line("HARDWARE INFORMATION", "\n")

# Cpu information block: takes cpu model , cores and threads
line("CPU INFORMATION", "\n")

physical = psutil.cpu_count(logical=False)
threads = psutil.cpu_count(logical=True)
architecture = platform.architecture()
processor = platform.processor()
print(f"CPU: {physical} Cores, {threads} Threads\n")
print(f"ARCHITECTURE: {architecture[1]}\n")
print(f"PROCESSOR: {processor}\n")



# Ram information block: takes ram information how much ram in your computer and your ram usage also tells
line("RAM INFORMATON", "\n")
Ram = psutil.virtual_memory()
print(f"RAM: {Ram.total / (1024**3):.2f}GB\n")
print(f"RAM USAGE: {Ram.used / (1024**3):.2f}GB\n")
print(f"RAM USAGE PERCENT: {Ram.percent}%\n")
print(f"RAM AVAILABLE: {Ram.available / (1024**3):.2f}GB\n")
print(f"RAM FREE: {Ram.free / (1024**3):.2f}GB\n")


# Operating system information block: takes Operating system information which are you using and what release build
line("OPERATING SYSTEM INFORMATON", "\n")
os = platform.version()

build = os.split(".")[2]


if int(build) >= 22000:
    print(f"OPERATING SYSTEM: Windows 11\n\nbuild: {os}\n")
    
elif int(build) <=22000:
    print(f"Operating System: Windows 10\n\nbuild: {os}\n" )

elif os in ["Linux", "Mac"]:
    print(f"OPERATING SYSTEM: Linux\\Mac {build}\n")







# Storage Partition information block : takes your system disk partitions information to displayed
line("DISK INFORMATION","\n")
Storage = psutil.disk_partitions()

for disks in Storage:
    print(f"STORAGE PARTITIONS: {disks.device}\nFORMAT TYPE: {disks.fstype}\n\n")
    partitions = str(disks.device)
    path = partitions
    partitions = psutil.disk_usage(path)
    print(f"STORAGE {path} DRIVE:{partitions.total / (1024**3):.2f}GB\n")
    print(f"STORAGE USAGE {path} DRIVE:{partitions.used / (1024**3):.2f}GB\n")
    print(f"STORAGE FREE {path} DRIVE:{partitions.free / (1024**3):.2f}GB\n")
    print("\n")



# Laptop or Workstation detection system block: takes minimal information on your system to see if you have battery then you use laptop otherwise workstation
line("BATTERY INFORMATION", "\n")
battery = psutil.sensors_battery()

if battery:
    print("DEVICE: Laptop\n")
    print(f"BATTERY: {battery.percent}%\n")
else:
    print("DEVICE: Desktop/Workstation\n")



# Network detection block: takes internet connection information to see your pc is wifi connected or not connected
line("NETWORK INFORMATION", "\n")
print(f"WIFI CONNECTION: {'Connected' if psutil.net_if_stats() else 'Disconnected'}")




try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


    sock.connect(("1.1.1.1", 80))

    ip = sock.getsockname()[0]


    print(f"COMPUTER IP ADDRESS: {ip}")
    
except OSError:
    print("No connection")
