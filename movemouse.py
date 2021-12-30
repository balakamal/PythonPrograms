import pyautogui as mouse
import time as t
c = 0
while True:
    mouse.moveTo(500, 100)
    mouse.drag(0, 100, button='left')
    mouse.moveRel(100, 5)
    mouse.moveRel(0, 150)
    mouse.moveRel(150, 0)
    c += 1
    print("Move : " + str(c))
    t.sleep(5)
