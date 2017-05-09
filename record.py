import datetime
import os
import sys
import time

import cv2

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
PHOTO_PATH = os.path.join(DIR_PATH, 'photos')


def get_current_photo_location():
    current = datetime.datetime.time(datetime.datetime.now())
    file_name = str(current.hour) + '_' + str(current.minute) + '.jpg'
    file_path = os.path.join(PHOTO_PATH, file_name)
    return file_path


def main(sys_argv):
    cam = cv2.VideoCapture(0)
    time.sleep(1)
    ret_val, img = cam.read()
    photo_location = get_current_photo_location()
    print(photo_location)
    cv2.imwrite(photo_location, img)


if __name__ == '__main__':
    main(sys.argv)
