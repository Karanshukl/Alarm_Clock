import time
import datetime
import pygame

def setAlarm(alarmTime):
    print(f"\nAlarm Stop: {alarmTime}")
    sound = "Millionaire Glory 320 Kbps.mp3"   # song file path
    running = True
    alarm_start_time = None  

    while running:
        curr_time = datetime.datetime.now().strftime("%I:%M:%S %p")
        print(f"\r\033[031m{curr_time}\033[0m", end="")
       
        if curr_time == alarmTime:
            print()
            print("Wake Up!")
            running = False

            pygame.mixer.init()
            pygame.mixer.music.load(sound)
            pygame.mixer.music.play()
            alarm_start_time = time.time()

            while pygame.mixer.music.get_busy():
                if time.time() - alarm_start_time >= 45:
                    pygame.mixer.music.stop()
                    break
                
        time.sleep(1)

if __name__ == "__main__":
    hour = int(input("Enter Hour: "))
    minute = int(input("Enter Minutes: "))
    seconds = int(input("Enter seconds: "))
    symbol= input("AM / PM: ")
    alarmTime = (f"{hour:02d}:{minute:02d}:{seconds:02d} {symbol}").upper()   # format specifier (:02d) for 2 digit decimal 
    setAlarm(alarmTime)
