import pyautogui
from PIL import Image
import os

# 定義當前目錄 Number Verification 文件夾所在位置
current_dir = 'C:/Users/admin1/Desktop'


def image_verification():
    file_path = current_dir+'/Number Verification/image/screen/Screen.jpg'
    # 如果文件存在，則刪除
    if os.path.exists(file_path):
        os.remove(file_path)
        print('File deleted. path:' + file_path)
    else:
        print('File does not exist. path:' + file_path)
    pyautogui.PAUSE=1

    # 截圖並儲存到指定路徑
    imageScreen = pyautogui.screenshot()
    imageScreen.save(file_path)
    print('printscreen')
    pyautogui.PAUSE=1

    # 讀取驗證圖片並與截圖做比對
    image_verification_1 = current_dir+'/Number Verification/image/image_verification/cap0008(verification).jpg'
    image_verification_2 = current_dir+'/Number Verification/image/image_verification/cap0009(verification).jpg'
    for image_verification in [image_verification_1, image_verification_2]:
        image = Image.open(image_verification)
        # 取得驗證圖片座標，如果未找到返回None
        imageCenter = pyautogui.locateCenterOnScreen(image, confidence=0.8)
        if imageCenter != None:
            print('偵測到驗證碼')
            # 返回圖片座標中心點，及偵測到的圖片名稱
            return imageCenter.x, imageCenter.y, image_verification
        else:
            continue

    print('無驗證視窗')
    return False

def image_input():
    pyautogui.PAUSE=1
    image_input_1 = current_dir+'/Number Verification/image/image_input/cap0008(input).jpg'
    image_input_2 = current_dir+'/Number Verification/image/image_input/cap0009(input).jpg'
    for image_input in [image_input_1, image_input_2]:
        image = Image.open(image_input)
        # 取得輸入框中心點座標
        buttonCenter = pyautogui.locateCenterOnScreen(image, confidence=0.8)
        if buttonCenter != None:
            # 滑鼠點擊該取得座標
            pyautogui.moveTo(buttonCenter.x, buttonCenter.y) 
            pyautogui.mouseDown(); pyautogui.mouseUp() 
            pyautogui.mouseDown(); pyautogui.mouseUp() 
            return True
        else:
            continue

    print('找不到輸入框座標')



