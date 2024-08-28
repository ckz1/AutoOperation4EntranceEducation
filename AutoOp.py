import pyautogui
import time 
import sys

# 鼠标移动至屏幕左上角时终止程序
pyautogui.FAILSAFE = True

# 获取屏幕宽度和高度
width, height = pyautogui.size()

def get_mouse_position(duration:float=0.5):
    """
    Args:
        duration : 每次获取鼠标坐标后的暂停时间
    """
    print('Press Ctrl+C to quit.')
    try:
        while True:
            x,y = pyautogui.position()
            position_str = f"X: {x:4d} Y: {y:4d}"
            print(position_str, end='')
            print('\b'*len(position_str),end='',flush=True)
            time.sleep(3)
    except KeyboardInterrupt:
        print('\n')


def page_goon():
    # 接触暂停
    pos = pyautogui.locateCenterOnScreen('shi.png',confidence=0.8)
    if pos is not None:
        pyautogui.click(x=pos[0],y=pos[1],button='left')

    # 学习下一章节
    pos = pyautogui.locateCenterOnScreen('xuexixiayizhangjie.png',confidence=0.8)
    if pos is not None:
        pyautogui.click(x=pos[0],y=pos[1],button='left')
        time.sleep(5)

    # 播放视频
    pyautogui.moveTo(int(width*0.5),int(height*0.5),1)

    pos = pyautogui.locateCenterOnScreen('play.png',confidence=0.8)
    if pos is not None:
        pyautogui.click(x=pos[0],y=pos[1],button='left')

        pos = pyautogui.locateCenterOnScreen('beisu.png',confidence=0.8)
        if pos is not None:
            pyautogui.click(x=pos[0],y=pos[1],button='left')

        pos = pyautogui.locateCenterOnScreen('2.0x.png',confidence=0.8)
        if pos is not None:
            pyautogui.click(x=pos[0],y=pos[1],button='left')

    time.sleep(3)



def keep_page_alive():
    print('Press Ctrl+C to quit.')
    try:
        while True:
            page_goon()

            # 视频播放页面每5分钟检测一次是否有操作
            pyautogui.moveTo(int(width*0.25),int(height*0.25),1,pyautogui.easeOutQuad)
            # pyautogui.click(x=200,y=200,button='left')
            # pyautogui.moveTo(int(width*0.25),int(height*0.25),1,pyautogui.easeInQuad)
            time.sleep(60*1)

            page_goon()

            pyautogui.moveTo(int(width*0.75),int(height*0.75),1,pyautogui.easeInBounce)
            time.sleep(60*1)

            pos = pyautogui.locateCenterOnScreen('queding.png',confidence=0.8)
            if pos is not None:
                pyautogui.alert(title='提示',text='学习完成',button='OK')
                break

    except KeyboardInterrupt:
        print('\n')

def multi_page_down(times:int=10,duration=5):
    for _ in range(10):
        # pyautogui.scroll(clicks=-10,x=int(width/2),y=int(height/2))

        pyautogui.click(x=int(width/2),y=int(height/2),button='left')
        pyautogui.press('pagedown')
        time.sleep(5)

def main():
    task_type = pyautogui.confirm(title='GUI',text='功能选择:',buttons=['获取鼠标坐标','保持网页活跃','连续翻页'])
    # print(task_type)
    if task_type == '获取鼠标坐标':
        get_mouse_position()
    elif task_type == '保持网页活跃':
        keep_page_alive()
    elif task_type == '连续翻页':
        multi_page_down()
    else:
        print('Wrong task_type!')


if __name__ == '__main__':
    main()



