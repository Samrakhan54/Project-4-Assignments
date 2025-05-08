# Countdown Timer

import time

secs = int(input("Enter time in seconds: "))

while secs > 0:
    mins = secs // 60
    sec = secs % 60
    timer = f"{mins:02d}:{sec:02d}"
    print(timer, end="\r")
    time.sleep(1)
    secs -= 1

print("Time's up!")
