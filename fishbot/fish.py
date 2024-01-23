import cv2 as cv
import numpy as np
import keyboard
from PIL import ImageGrab
import time
import pyautogui
import random
 
def fish_detected(screen, small_image):
    method = cv.TM_SQDIFF_NORMED
    
    result = cv.matchTemplate(small_image, screen, method)
    #print(result)
    #return result



#small_image2 = cv.imread('bob.png')
#Basically we have 3 images and an alphachannel
#*_, alpha = cv.split(small_image)
#cv.imwrite("result.png", small_image)
#smalimg2 = small_image[small_image[:,:,3] == 1]
#cv.imwrite("result2.png", small_image)
#print(small_image.shape)
#small_image = cv.cvtColor(small_image, cv.COLOR_BGR2GRAY)
#cap = cv.VideoCapture(1)
# if not cap.isOpened():
#     print("Cannot open camera")
#     exit()
i = 0
#time_found = time.time()´

class FishBot():
    def __init__(self) -> None:
        #config 
        self.threshold = 0.65
        self.running_time = 8 # hours
        #Frames
        self.frame = None
        self.boober = cv.imread('temp2.png')
        self.buff = cv.imread('buff.png')
        self.chum = cv.imread('chum.png')
        self.buff_and_chum = None

        #Keys
        self.fish_key = '1'
        self.pickup_key = 'home'
        self.chum_key = '3'
        self.buff_key = '2'
        

    def narrow_search_window(self):
        pass

    def menu(self):
        print("Welcome to the wow enhancer!🧙‍♂️🧚‍♀️🧚‍♂️🧝‍♀️")        
        while True:
            x = input("What do you want to do? \n 1. fishbot \n 2. record screen \n 3. view detection \n 0. Exit \n")
            if x == "1":
                self.fish_bot()
            if x == "2":
                self.record_screen(10)
            if x == "3":
                self.view_detection()
            if x == "0":
                print("Thanks for this time.")
                break
            print("No valid option taken!")

    def update_frame(self):
        self.frame = cv.cvtColor(np.array(ImageGrab.grab(bbox=(0,0,1920,1080))), cv.COLOR_BGR2RGB)
        

    def resize_screen(self,frame_w,frame_h):
        self.frame = cv.resize(self.frame, (frame_w,frame_h))

    def show_frame(self, frame_w, frame_h):
        #print(self.frame.shape)
        self.resize_screen(frame_w,frame_h)
        cv.imshow('frame', self.frame)

    def draw_rectangle(self, location):
        w, h = self.boober.shape[:-1]
        for pt in zip(*location[::-1]):  # Switch columns and rows
            cv.rectangle(self.frame, pt, (pt[0] + h, pt[1] + w), (0, 0, 255), 2)
            time_found = time.time()
        pass

    def bobber_found(self) ->bool:
        res = cv.matchTemplate(self.frame, self.boober, cv.TM_CCOEFF_NORMED)
        loc = np.where(res >= self.threshold)
        self.draw_rectangle(loc)
        if loc[1].size == 0:
            print('done')
            return False
        return True

    def cut_frame(self):
        #self.frame = self.frame[int(1080/4*3):1080, int(0/3*2):int(1920/3)]
        self.frame = self.frame
 


    def fish_catch(self) -> None:
        time_found = 0
        time_start = time.time()
        choosen_limit = random.randint(15,25) + random.random() + random.random()
        while True:
            #If not is buff on, press key.
            current_time = time.time()
            self.update_frame()
            self.cut_frame()
            if not self.bobber_found():
                print("Fish found🦈🎣")
                return
            
            self.show_frame(int(960/4), int(540/4))
            if time.time() - time_start > choosen_limit:
                print(f"Time have passsed: {choosen_limit}")
                return
            if cv.waitKey(1) == ord('q'):
                return
        
    def is_buff_seen(self):
        res = cv.matchTemplate(self.frame, self.buff, cv.TM_CCOEFF_NORMED)
        w, h = self.buff.shape[:-1]
        loc = np.where(res >= self.threshold)
        for pt in zip(*loc[::-1]):  # Switch columns and rows
            cv.rectangle(self.frame, pt, (pt[0] + h, pt[1] + w), (0, 0, 255), 2)
            time_found = time.time()
        if loc[1].size == 0:
            print('done')
            return False
        return True

    def is_chum_seen(self):
        res = cv.matchTemplate(self.frame, self.chum, cv.TM_CCOEFF_NORMED)
        w, h = self.chum.shape[:-1]
        loc = np.where(res >= self.threshold)
        for pt in zip(*loc[::-1]):  # Switch columns and rows
            cv.rectangle(self.frame, pt, (pt[0] + h, pt[1] + w), (0, 0, 255), 2)
            time_found = time.time()
        if loc[1].size == 0:
            print('done')
            return False
        return True

    def cast_buff(self):
        #pyautogui.press(self.buff_key)
        pyautogui.keyDown(self.buff_key)
        time.sleep(0.2 + random.random()/5)
        pyautogui.keyUp(self.buff_key)
        time.sleep(3)
        time.sleep(random.random())


    def cast_chum(self):
        for i in range(6):
            pyautogui.keyDown(self.chum_key)
            time.sleep(0.2 + random.random()/5)
            pyautogui.keyUp(self.chum_key)
            time.sleep(1.2 + random.random())
        
        time.sleep(3)
        time.sleep(random.random())

    def cast_lure(self):
        print("Lure key down")
        pyautogui.keyDown(self.fish_key)
        time.sleep(0.2 + random.random()/5)
        print("lure key up")
        pyautogui.keyUp(self.fish_key)
        time.sleep(3.5)
        time.sleep(random.random())

    def pickup_lure(self):
        pyautogui.keyDown(self.pickup_key)
        time.sleep(0.2 + random.random()/5)
        pyautogui.keyUp(self.pickup_key)
        time.sleep(random.random())

    def fish_bot(self):
        print("Go to the screen")
        time_start = time.time()
        time.sleep(3)
        count = 0
        print("Lure put on")
        #pyautogui.press('2')
        while not keyboard.is_pressed('*'):
            #start screen and watch
            print("Casting Lure")
            self.cast_lure()
            print("Looking for fish")
            self.fish_catch()
            print("Picking up the lure")
            self.pickup_lure()
            time.sleep(5 +random.random())
            count+=1
            print(f'Count: {count}')
            self.update_frame()
            if not self.is_buff_seen():
                self.cast_buff()
            # if not self.is_chum_seen():
            #     self.cast_chum()
            if time.time() - time_start > self.running_time*60*60:
                return

    def record_screen(self,time_to_record: int):
        print("Screen Reccording started")
        time_found = 0
        time_start = time.time()
        i = 0
        while True:
            self.update_frame()
            i+=1
            cv.imwrite(f'pics2/{i}.png', self.frame)

            if time.time() - time_start > time_to_record:
                print(f"Time have passsed: {time_to_record}")
                break
            if cv.waitKey(1) == ord('q'):
                break
    def time_have_passed(self, seconds):
        pass

    def view_detection(self):
        time_found = 0
        time_start = time.time()
        choosen_limit = random.randint(15,25) + random.random() + random.random()
        while True:
            #If not is buff on, press key.
            current_time = time.time()
            self.update_frame()
            self.cut_frame()
            self.bobber_found()
            self.show_frame()
            if cv.waitKey(1) == ord('q'):
                return
#okay so now we can consistently put the things in


if __name__ == "__main__":
        FishBot().menu()

