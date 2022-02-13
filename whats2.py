import pywhatkit
import datetime


def whatsapp(number, gif):
    current_time = datetime.datetime.now()

    hours = current_time.strftime("%H")

    minute = current_time.strftime("%M")


    times = {"00":'0', '01':'1', '02':'2', '03':'3', '04':'4', '05':'5', '06':'6', '07':'7', '08':'8', '09':'9' }

    if hours in times:
        hours = times[hours]
    if minute in times:
        minute = times[minute]

    print(hours, minute)
    send_gif = "I love you girl<3 "+ gif
    pywhatkit.sendwhatmsg(number, send_gif, int(hours), int(minute) +1 , 15, True, True)