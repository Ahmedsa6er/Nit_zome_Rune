import time
import pyautogui
import win32api
import win32con
import sys

time.sleep(4)
def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    
def main():
    start_time = time.time()
    while time.time() - start_time <= 21600:
        pyautogui.moveTo(1495, 728)
        click()
        time.sleep(10)
#1
        if 1198 <= time.time() - start_time < 1216:
            pyautogui.click(1495, 946)
            click()
            time.sleep(2)
            pyautogui.click(1495, 946)
            click()
            time.sleep(2)
            pyautogui.click(1495, 946)
            click()
            time.sleep(2)
            pyautogui.click(1495, 946)
            click()
            time.sleep(2)
#2
        if 2398 <= time.time() - start_time < 2416:
            pyautogui.click(1538, 945)
            click()
            time.sleep(2)
            pyautogui.click(1538, 945)
            click()
            time.sleep(2)
            pyautogui.click(1538, 945)
            click()
            time.sleep(2)
            pyautogui.click(1538, 945)
            click()
            time.sleep(2)
            
#3
        if 3598 <= time.time() - start_time < 3616:
            pyautogui.click(1579, 945)
            click()
            time.sleep(2)
            pyautogui.click(1579, 945)
            click()
            time.sleep(2)
            pyautogui.click(1579, 945)
            click()
            time.sleep(2)
            pyautogui.click(1579, 945)
            click()
            time.sleep(2)
#4
        if 4798 <= time.time() - start_time < 4816:
            pyautogui.click(1621, 948)
            click()
            time.sleep(2)
            pyautogui.click(1621, 948)
            click()
            time.sleep(2)
            pyautogui.click(1621, 948)
            click()
            time.sleep(2)
            pyautogui.click(1621, 948)
            click()
            time.sleep(2)
#21
        if 5998 <= time.time() - start_time < 6016:
            pyautogui.click(1496, 910)
            click()
            time.sleep(2)
            pyautogui.click(1496, 910)
            click()
            time.sleep(2)
            pyautogui.click(1496, 910)
            click()
            time.sleep(2)
            pyautogui.click(1496, 910)
            click()
            time.sleep(2)
#22
        if 7198 <= time.time() - start_time < 7216:
            pyautogui.click(1539, 911)
            click()
            time.sleep(2)
            pyautogui.click(1539, 911)
            click()
            time.sleep(2)
            pyautogui.click(1539, 911)
            click()
            time.sleep(2)
            pyautogui.click(1539, 911)
            click()
            time.sleep(2)
#23
        if 8398 <= time.time() - start_time < 8416:
            pyautogui.click(1579, 911)
            click()
            time.sleep(2)
            pyautogui.click(1579, 911)
            click()
            time.sleep(2)
            pyautogui.click(1579, 911)
            click()
            time.sleep(2)
            pyautogui.click(1579, 911)
            click()
            time.sleep(2)
#24
        if 9598 <= time.time() - start_time < 9616:
            pyautogui.click(1622, 910)
            click()
            time.sleep(2)
            pyautogui.click(1622, 910)
            click()
            time.sleep(2)
            pyautogui.click(1622, 910)
            click()
            time.sleep(2)
            pyautogui.click(1622, 910)
            click()
            time.sleep(2)
#31
        if 10798 <= time.time() - start_time < 10816:
            pyautogui.click(1496, 876)
            click()
            time.sleep(2)
            pyautogui.click(1496, 876)
            click()
            time.sleep(2)
            pyautogui.click(1496, 876)
            click()
            time.sleep(2)
            pyautogui.click(1496, 876)
            click()
            time.sleep(2)
#32
        if 11998 <= time.time() - start_time < 12016:
            pyautogui.click(1536, 875)
            click()
            time.sleep(2)
            pyautogui.click(1536, 875)
            click()
            time.sleep(2)
            pyautogui.click(1536, 875)
            click()
            time.sleep(2)
            pyautogui.click(1536, 875)
            click()
            time.sleep(2)
#33
        if 13198 <= time.time() - start_time < 13216 :
            pyautogui.click(1580, 877)
            click()
            time.sleep(2)
            pyautogui.click(1580, 877)
            click()
            time.sleep(2)
            pyautogui.click(1580, 877)
            click()
            time.sleep(2)
            pyautogui.click(1580, 877)
            click()
            time.sleep(2)
#34
        if 14398 <= time.time() - start_time < 14416 :
            pyautogui.click(1620, 876)
            click()
            time.sleep(2)
            pyautogui.click(1620, 876)
            click()
            time.sleep(2)
            pyautogui.click(1620, 876)
            click()
            time.sleep(2)
            pyautogui.click(1620, 876)
            click()
            time.sleep(2)


    sys.exit()
if __name__ == "__main__":
    main()
    
