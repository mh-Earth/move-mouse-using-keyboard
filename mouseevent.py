# Use the `a,s,d,w` to move the cursor
# use the keyboard arrow to move the curour
# 1 for click Left
# 0 for click RIght
# press `esc` for use the mouse
# press " ` " for use the keyboard as mouse
#  press "shift+\" to quit the programm

import keyboard
import pyautogui
import winsound
import pyttsx3
def speak(text):
    engine=pyttsx3.init()
    engine.setProperty("rate",150)
    engine.say(text)
    engine.runAndWait()

def beep(frequency,duration):
    winsound.Beep(frequency, duration)

if __name__=="__main__":
    position=pyautogui.position()
    x=position[0]
    y=position[1]
    # ___________________________
    speed=15
    # ___________________________
    working=True
    click=True
    drag=False
    scoll=False
    # ___________________________
    while True:
        try:
            if working:
                #moving the mouse to x,y position
                pyautogui.moveTo(x,y)

                #key board press ____________
                if keyboard.is_pressed('ctrl+1'):
                    speed=15
                    click=True
                    drag=False
                    pyautogui.mouseUp(button="LEFT")
                    pyautogui.mouseUp(button="RIGHT")
                    beep(2000,100)

                if keyboard.is_pressed('a'):
                    x-=speed
                if keyboard.is_pressed('d'):
                    x+=speed
                if keyboard.is_pressed('s'):
                    y+=speed
                if keyboard.is_pressed('w'):
                    y-=speed
                # ___________________________
                if keyboard.is_pressed('1'):
                    speed+=1
                    speak(speed)
                if keyboard.is_pressed('2'):
                    speed-=1
                    speak(speed)
                # ___________________________

                if keyboard.is_pressed('z'):
                    click=False
                    drag=True
                    speak("Drag mode on")

                if keyboard.is_pressed('x'):
                    pyautogui.mouseUp(button="LEFT")
                    pyautogui.mouseUp(button="RIGHT")
                    click=True
                    drag=False
                    speak("Drag mode off")
                # ___________________________
                if click:
                    if keyboard.is_pressed('q'):
                        pyautogui.click(button="LEFT")
                    if keyboard.is_pressed('e'):
                        pyautogui.click(button="RIGHT")
                    if keyboard.is_pressed('esc'):
                        beep(2000,100)
                        working=False
                # ___________________________
                if drag:
                    if keyboard.is_pressed('q'):
                        pyautogui.mouseDown(button="LEFT")
                    if keyboard.is_pressed('e'):
                        pyautogui.mouseDown(button="RIGHT")
                    if keyboard.is_pressed('esc'):
                        beep(2000,100)
                        working=False
                # ___________________________
                if keyboard.is_pressed('shift+\\'):
                    break
                # ___________________________

                else:
                    pass
            elif not working:
                if keyboard.is_pressed('`'):
                    beep(2000,500)
                    working=True
            else:
                pass
        except Exception as e:
            print(e)
            break 


