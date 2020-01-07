# import the module
import sys
sys.path.append("..") 
from common.loop import Loop
from common.img_process import classify_gray_hist
from common.window_action import *
import cv2
import gc
import pythoncom

import pyperclip
import time
 

# 截取点赞
def getZaned(img):
    zanedX = 442
    zanedY = 1002
    print(len(img[0]))
    return img[zanedY:(zanedY+20),zanedX:(zanedX+20)]

# 截取收藏
def getCangd(img):
    cangdX = 483
    cangdY = 1002
    return img[cangdY:(cangdY+20),cangdX:(cangdX+20)]
    
sampleImg = cv2.imread('sample.png');
zanedImg = getZaned(sampleImg);
cangdImg = getCangd(sampleImg);
    
def one_move():
    # 点第一篇文章
    openFirstArticle();
    # 截屏
    screenImg = window_capture();
    curZanedImg = getZaned(screenImg);
    curCangdImg = getCangd(screenImg);
    # 未点赞的，点赞
    if classify_gray_hist(curZanedImg, zanedImg):
        print('未点赞的，点赞')
        zan();
    # 未收藏的，收藏
    if classify_gray_hist(curCangdImg, cangdImg):
        print('未收藏的，收藏')
        cang();
    # 不管评没评过，评论
    comment();
    # 返回
    clickBakBtn();
    # 向上拖动一篇文章
    dragUp();
    

# 点第一篇文章
def openFirstArticle():
    mouse_click(150,530)
    time.sleep(3.0)

# 评论
def comment():
    # 点评论
    mouse_click(150,1010)
    time.sleep(1.0)
    # 点评论框
    mouse_click(150,950)
    time.sleep(0.5)
    # 先复制
    pyperclip.copy('赞')  
    # 再粘贴
    pyautogui.hotkey('ctrl', 'v')  
    time.sleep(0.1)
    # 点发布
    mouse_click(520,1010)
    time.sleep(2)

    
# 点赞
def zan():
    mouse_click(457,1010);
    time.sleep(1.0);
    

# 收藏  
def cang():
    mouse_click(500,1010);
    time.sleep(1.0);

    
# 点返回按钮    
def clickBakBtn():
    mouse_click(281,77);
    time.sleep(0.5);
    mouse_click(25,85);
    time.sleep(1.5);
    return True;
    
# 向上拖动一篇文章
def dragUp():
    mouse_drag(487,700,487,700-214,0.2,1.2);

def main():
    #初始化键盘钩子 监听 键盘事件
    #Loop().initKeyboardHook(one_move)
                
    # 进入循环，如不手动关闭，程序将一直处于监听状态dd
    #pythoncom.PumpMessages()
    while True:
        one_move()
    #dragUp()
    
    cv2.waitKey(0)   #等待用户操作，里面等待参数是毫秒，我们填写0，代表是永远，等待用户操作
    cv2.destroyAllWindows()  #销毁所有窗口
    #zanAndComment(462,861)

if __name__ == "__main__":
    main()