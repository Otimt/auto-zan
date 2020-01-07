import win32gui, win32ui, win32con, win32api
import cv2
import time
import pyautogui
import numpy as np
from pymouse import PyMouse
m = PyMouse()

#window操作========================================================================================================
#关机
def shutdown():
    print("关机")

# 鼠标点击
def mouse_click(x,y):
    pyautogui.click(x, y)

# 按键
def keyboard_press(key):
    ascii = ord(key)
    win32api.keybd_event(ascii,0,0,0) #ctrl键位码是17
    return True;
    
# 鼠标拖拽
def mouse_drag(x,y,x2,y2,duration=0.5,mouseUpDelay=0.05):
    # instantiate an mouse object
    screen_size = m.screen_size()
    m.move(x, y)    #鼠标移动到  
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)    #左键按下
    time.sleep(0.05)
    pyautogui.moveTo(x2,y2,duration)
    time.sleep(mouseUpDelay)
    SW = screen_size[0]
    SH = screen_size[1]
    mw = int(x2 * 65535 / SW) 
    mh = int(y2 * 65535 / SH)
    win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE + win32con.MOUSEEVENTF_MOVE, mw, mh, 0, 0)    
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    
# 截屏
def window_capture():
    img = pyautogui.screenshot(region=[0,0,1920,1080]) # x,y,w,h
    arr = np.asarray(img);
    #img.save('screenshot.png')
    return cv2.cvtColor(np.asarray(img),cv2.COLOR_RGB2BGR);
    
