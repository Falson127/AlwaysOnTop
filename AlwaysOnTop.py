import sys
import os
import win32gui
import win32con
import keyboard
import pystray
from PIL import Image

def toggle_always_on_top(hwnd):
    current_ex_style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
    print(hwnd)
    print(win32con.GWL_EXSTYLE)
    if current_ex_style & win32con.WS_EX_TOPMOST == 0:
        new_ex_style = current_ex_style | win32con.WS_EX_TOPMOST
        settopmost = True
        print("Making window stay on top")
    else:
        new_ex_style = current_ex_style & ~win32con.WS_EX_TOPMOST
        settopmost = False
        print("Banashing window to bottom")
    win32gui.SetWindowPos(
        hwnd,
        win32con.HWND_TOPMOST if settopmost else win32con.HWND_NOTOPMOST,
        0, 0, 0, 0,
        win32con.SWP_NOMOVE | win32con.SWP_NOSIZE
    )
    win32gui.ShowWindow(hwnd, win32con.SW_SHOW)
def EmptyAction():
    i = 1 # this action does nothing
def on_exit(icon, item):
    icon.stop()
    sys.exit(0)
def main():
    keyboard.add_hotkey("shift+t",lambda: toggle_always_on_top(win32gui.GetForegroundWindow()))
    script_directory = os.getcwd() #only works when built into exe, finds wrong directory when debugging directly
    image_path = os.path.join(script_directory,"pin.png")
    image = Image.open(image_path)
    menu = (
        pystray.MenuItem("Select a window and press 'Shift + T' to toggle pin to top mode",EmptyAction),
        pystray.MenuItem("Exit",on_exit)
    )
    icon = pystray.Icon("Pin-to-Top",image,"Pin-to-Top",menu)
    icon.run()
    
if __name__ == "__main__":
    main()
    
