import time
import datetime
import pygame

def setAlarm(alarmTime):
    print(f"\nAlarm Stop: {alarmTime}")
    sound = "Millionaire Glory 320 Kbps.mp3"   # song file path
    running = True   
    alarm_start_time = None    # for stores the start time of the alarm sound 

    while running:
        curr_time = datetime.datetime.now().strftime("%I:%M:%S %p")  # return current time in 12-hour format
        print(f"\r\033[031m{curr_time}\033[0m", end="")
       
        if curr_time == alarmTime:       # check if current time matches the alarm time
            print()
            print("Wake Up!")
            running = False     # stop the loop

            pygame.mixer.init()
            pygame.mixer.music.load(sound)   #load the alarm sound file 
            pygame.mixer.music.play()        # for play the alarm sound
            alarm_start_time = time.time()  # start time of the alarm sound.

            while pygame.mixer.music.get_busy():          # loop for while music is playing 
                if time.time() - alarm_start_time >= 45:    # check if the time hits 45 sec
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
