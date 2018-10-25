from pyautogui import press
import time
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
start = input("What number do you want to start at?")
for i in range(start):
    if f == 9:
        if e == 9:
            e = 0
            if d == 9:
                d = 0
                if c == 9:
                    c = 0
                    if b == 9:
                        b = 0
                        a += 1
                    else:
                        b += 1
                else:
                    c += 1
            else:
                d += 1
        else:
            e += 1
    f = i % 10
print("Count will begin in 10 seconds")
time.sleep(10)
for i in range(start, 1000001):
    time.sleep(1)
    if f == 9:
        if e == 9:
            e = 0
            if d == 9:
                d = 0
                if c == 9:
                    c = 0
                    if b == 9:
                        b = 0
                        a += 1
                    else:
                        b += 1
                else:
                    c +=1
            else:
                d += 1
        else:
            e += 1

    f = i % 10
    if a > 0:
        press(str(a))
    if b > 0 or a > 0:
        press(str(b))
    if c > 0 or b > 0 or a > 0:
        press(str(c))
    if d > 0 or c > 0 or b > 0 or a > 0:
        press(str(d))
    if e > 0 or d > 0 or c > 0 or b > 0 or a > 0:
        press(str(e))
    press(str(f))
    press('return')
