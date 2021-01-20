# Use the `a,s,d,w` to move the cursor
# use the keyboard arrow to move the curour
# 1 for click Left
# 0 for click RIght
# press `esc` for use the mouse
# press " ` " for use the keyboard as mouse
#  press f1 to quit the programm
import keyboard
import pyautogui
x=500
y=500
working=True
while True:
    try:
        if working:
            #moving th mouse to x,y position
            pyautogui.moveTo(x,y)

            #key board press 
            if keyboard.is_pressed('a'):
                x-=15
            if keyboard.is_pressed('d'):
                x+=15
            if keyboard.is_pressed('s'):
                y+=15
            if keyboard.is_pressed('w'):
                y-=15
            if keyboard.is_pressed('q'):
                pyautogui.mouseDown(button="LEFT")
            if keyboard.is_pressed('e'):
                pyautogui.mouseDown(button="RIGHT")
            if keyboard.is_pressed('esc'):
                working=False
            if keyboard.is_pressed('shift+\\'):
                break

            else:
                pass
        elif not working:
            if keyboard.is_pressed('`'):
                working=True
        else:
            pass
    except Exception as e:
        print(e)
        break 
