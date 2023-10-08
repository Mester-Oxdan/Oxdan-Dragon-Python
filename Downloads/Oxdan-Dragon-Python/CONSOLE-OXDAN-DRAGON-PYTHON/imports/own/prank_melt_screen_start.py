import msvcrt
import win32api
import win32con
import pyautogui, cv2, numpy, random
from colorama import Fore
import imports.own.will_go_to_start

def prank_melt_screen_start():

        #cv2.waitKey(1000)

        print(Fore.RED + "\nClick on console then Press 'Esc' for exit" + Fore.WHITE)
        #print(" ")

        image_screenshot = pyautogui.screenshot()
        _array_image = numpy.array(image_screenshot)
        image = cv2.cvtColor(_array_image, cv2.COLOR_RGB2BGR)

        cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        cv2.setWindowProperty("window",cv2.WND_PROP_TOPMOST,cv2.WND_PROP_TOPMOST)

        def mouse_evt(event, x, y, flags, param):
        # Mouse is Moving
            if event == cv2.EVENT_MOUSEMOVE:
                win32api.SetCursor(win32api.LoadCursor(0, win32con.IDC_ARROW))

        cv2.setMouseCallback("window", mouse_evt)

        cv2.imshow("window", image)

        _width = _array_image.shape[1] #width
        _height = _array_image.shape[0] #height
        _columns = 40
        _step = _width // _columns
        _move_down_by = 5
        #_key = 0

        #_key = ord(msvcrt.getch())

        while True:
                
                #_key = ord(msvcrt.getch())
                _col = random.randint(0,_columns)*_step
                for i in range(_move_down_by):
                    _array_image[i+1:_height,_col:_col+_step,:3] = _array_image[i:_height-1,_col:_col+_step,:3]
                    image = cv2.cvtColor(_array_image, cv2.COLOR_RGB2BGR)
                    cv2.imshow("window", image)

                if cv2.waitKey(27) >= 0:

                    cv2.destroyAllWindows()

                    imports.own.will_go_to_start.main()