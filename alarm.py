import time
import datetime
import os
import sys

os.system("mode con cols=55 lines=7")

current_datetime = datetime.datetime.now()
alarm_datetime = current_datetime.replace(hour=int(sys.argv[1]), minute=int(sys.argv[2]))
if alarm_datetime < current_datetime:
    alarm_datetime = alarm_datetime + datetime.timedelta(days=1)
alarm_datetime = alarm_datetime.replace(second=0, microsecond=0)

while current_datetime - alarm_datetime <= datetime.timedelta(seconds=0):
    os.system("cls")
    current_datetime = datetime.datetime.now()
    temps_restant = alarm_datetime - current_datetime + datetime.timedelta(minutes=1)
    print("\n Heure actuelle : " + current_datetime.strftime('%H:%M (%A, %B %d)'))
    print(" Heure d'alarme : " + alarm_datetime.strftime('%H:%M (%A, %B %d)'))
    print(" Temps restant : " + ':'.join(str(temps_restant).split(':')[:-1]))
    print("\n Vérifier le volume des enceintes et VLC.")
    time.sleep(1)

os.system("start /b C:\\Users\\nperez\\Music\\pl.flv")