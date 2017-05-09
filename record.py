import datetime
import os
import sys
import time

import cv2

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
PHOTO_PATH = os.path.join(DIR_PATH, 'photos')


def current():
    current = datetime.datetime.time(datetime.datetime.now())
    return current


def get_current_photo_location():
    now = current()
    file_name = str(now.hour) + '_' + str(now.minute) + '.jpg'
    file_path = os.path.join(PHOTO_PATH, file_name)
    return file_path


def capture_photo():
    cam = cv2.VideoCapture(0)
    time.sleep(1)
    ret_val, img = cam.read()
    photo_location = get_current_photo_location()
    print(photo_location)
    cv2.imwrite(photo_location, img)


def main(sys_argv):
    while True:
        now = current()
        if now.minute % 5 == 0:
            capture_photo()
        time.sleep(60)


if __name__ == '__main__':
    main(sys.argv)
