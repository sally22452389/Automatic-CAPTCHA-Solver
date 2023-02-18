from PIL import Image
import ddddocr
import pyautogui
import FindImage
from twocaptcha import TwoCaptcha

pyautogui.FAILSAFE = True

# 文件夾所在位置
current_dir = 'C:/Users/admin1/Desktop'


def auto_verification():
    # 第1次 ddddocr 識別
    verification = FindImage.image_verification()
    if verification == False:
        print("結束偵測")
        return False
    if verification != False:
        # 讀取圖片
        image_path = current_dir+'/Number Verification/image/screen/Screen.jpg'
        image = Image.open(image_path)

        # 檢查圖片是否被正確讀取
        if image is None:
            print('Failed to read image.')
        else:
            x = verification[0] # 取得驗證碼的 x 座標
            y = verification[1] # 取得驗證碼的 y 座標
            imgNumber = verification[2] # 取得驗證碼所在的圖片路徑
            if imgNumber == current_dir+'/Number Verification/image/image_verification/cap0009(verification).jpg':
                # 裁切圖片
                image_code = image.crop((x-110, y+85, x+30, y+160)) 
            elif imgNumber == current_dir+'/Number Verification/image/image_verification/cap0008(verification).jpg':
                image_code = image.crop((x-110*0.8, y+85*0.8, x+30*0.8, y+160*0.8))
            else:
                print('Error image not exist.')
            # 儲存裁切後僅驗證碼圖片
            image_code.save(current_dir+'/Number Verification/image/screen/image_code.jpg')

        ocr = ddddocr.DdddOcr()
        image_code_path = current_dir+'/Number Verification/image/screen/image_code.jpg'
        with open(image_code_path, 'rb') as f:
            img_bytes = f.read()
        res = ocr.classification(img_bytes)
        print('code:'+res)
        enter_code(res)

    # 1~2次 2Captcha 識別
    for i in range(0,2):
        verification = FindImage.image_verification()
        if verification == False:
            print("結束偵測")
            return False
        if verification != False:
            # 讀取圖片
            image_path = current_dir+'/Number Verification/image/screen/Screen.jpg'
            image = Image.open(image_path)

            # 檢查圖片是否被正確讀取
            if image is None:
                print('Failed to read image')
            else:
                x = verification[0] # 取得驗證碼的 x 座標
                y = verification[1] # 取得驗證碼的 y 座標
                imgNumber = verification[2] # 取得驗證碼所在的圖片路徑
                if imgNumber == current_dir+'/Number Verification/image/image_verification/cap0009(verification).jpg':
                    # 裁切圖片
                    image_code = image.crop((x-110, y+85, x+30, y+160)) 
                elif imgNumber == current_dir+'/Number Verification/image/image_verification/cap0008(verification).jpg':
                    image_code = image.crop((x-110*0.8, y+85*0.8, x+30*0.8, y+160*0.8))
                else:
                    print('Error image not exist.')
                # 儲存裁切後僅驗證碼圖片
                image_code.save(current_dir+'/Number Verification/image/screen/image_code.jpg')

            print('TwoCaptcha 驗證')
            image_code_path = current_dir+'/Number Verification/image/screen/image_code.jpg'
            solver = TwoCaptcha('apikey')
            try:
                result = solver.normal(image_code_path,numeric=1)
            except Exception as e:
                pyautogui.moveTo(1070, 20) 
                pyautogui.mouseDown(); pyautogui.mouseUp() 
                print(e)
                raise AssertionError('TwoCaptcha 驗證異常，關閉遊戲停止腳本')
            else:
                res = str(result['code'])
                print('code:'+res)
            enter_code(res)




def enter_code(res):
    image_code_path = current_dir+'/Number Verification/image/screen/image_code.jpg'
    pyautogui.PAUSE=0.1
    # 滑鼠點擊輸入框
    FindImage.image_input()
    pyautogui.PAUSE=0.1
    # 檢查res是否只包含數字
    if res.isdigit() is True:
        res = res
    else:
        res = '1'
    # 依序輸入數字
    for i in range(0,len(res)):
        pyautogui.press(f'num{res[i]}')
    pyautogui.PAUSE=0.1
    # 紀錄驗證結果
    imageScreen = pyautogui.screenshot(f'{current_dir}/Number Verification/image/log/Screen {res}.jpg')
    image_code_path = Image.open(image_code_path)
    image_code_path.save(f'{current_dir}/Number Verification/image/log/{res}.jpg')
    pyautogui.press('enter')
    print(f'enter:{res}')


