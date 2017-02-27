import webbrowser
import time

print "What time to set up the alarm Mr. Harish Gandhi?[eg time format: 16:40]"
alarmtime = raw_input()
min = int(alarmtime.split(':')[1])
hr = int(alarmtime.split(':')[0])

def alert(min,hr):
    execute = True
    while(execute):
        dt = list(time.localtime())

        if(hr == dt[3] and min == dt[4]):

            #paste the url of your favorite song
            url = 'https://youtu.be/JGwWNGJdvx8'

            # Open URL in a new tab, if a browser window is already open.
            webbrowser.open_new_tab(url)

            # Open URL in new window, raising the window if possible.
            webbrowser.open_new(url)
            execute = False
        else:
            execute = True


alert(min,hr)




