import datetime
import time

while True:
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time)
    time.sleep(1)
