# encoding = utf-8

import os
import shutil
from time import sleep


# noinspection PyShadowingNames
def uCopy(usb_path):
    usb_file = os.listdir(usb_path)
    while True:
        new_usb_file = os.listdir(usb_path)
        if new_usb_file != usb_file:
            break
        sleep(5)
    file = [f for f in new_usb_file if f not in usb_file]
    shutil.copytree(os.path.join(usb_path, file[0]), '/home/work/usb/copy')


if __name__ == '__main__':
    usb_path = "/Volumes"
    uCopy(usb_path)
