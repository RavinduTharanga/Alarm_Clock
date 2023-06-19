from datetime import datetime

alarmtime = input("Enter the time HH:MM \n")
alarmhour = alarmtime[0:2]
alarmminute= alarmtime[3:5]
print("Setting up alarm..")

while True:
    now = datetime.now()
    current_hour=now.strftime("%H")
    current_minute = now.strftime("%M")
    # current_seconds = now.strftime("%S")
    # current_period = now.strftime("%p")
    if alarmhour==current_hour and alarmminute==current_minute:
                    print("Wake Up!")
                    break
