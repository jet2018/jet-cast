import datetime
from time import sleep, timezone
import numpy as np
import cv2
import pyscreenshot as ImageGrab
import os
from colorama import Fore, Style



class Screen():

    def __init__(self, image_folder = 'Screenshots', video_folder = 'Videos'):
        self.image_folder = image_folder
        self.video_folder = video_folder

    def create_folder(self, name):
        try:
            if not os.path.exists(name):
                os.makedirs(name)
            return name
        except OSError:
            print('Error: Creating directory. ' + name)
            return False
    
    # def save_video(name):
    def delete_folder(self, name):
        try:
            if os.path.exists(name):
                os.rmdir(name)
            return self
        except OSError:
            print('Error: Deleting directory. ' + name)
            return False

    def record(self, wait):
        """
           This continuosly grabs the screen and saves it as a jpg file
        """
        print(Fore.RED+' Press CTRL+C to stop recording')
        print(Style.RESET_ALL)

        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.create_folder(self.video_folder)
        namer= datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        name = f'Videos/video-{namer}.mp4'
        out = cv2.VideoWriter(name, fourcc, 20.0, (1920, 1080))
        while True:
            img = ImageGrab.grab()
            img_np = np.array(img)
            frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
            # cv2.imshow('JET Recorder', frame)
            out.write(frame)
            c = cv2.waitKey(1)
            if c == 27:
                break
        out.release()
        cv2.destroyAllWindows()

    def shot(self):
        img = ImageGrab.grab(bbox=(0, 0, 1920, 1080))
        img_np = np.array(img)
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        slug = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        directory = self.image_folder
        
        try:
            self.create_folder(directory)
        except OSError:
            print("Error: {}".format(OSError))
        cv2.imwrite(f'{directory}/screen-{slug}.jpg', img_np)
        
        print(f'Screen shot saved as screen-{slug}.jpg in {os.path.abspath(directory)}')
        return f'screen-{slug}.jpg'
