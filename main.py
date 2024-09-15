# step 1 - to start this project you need to install PyCharm community edition or VS Code
# step 2 - you need to download a free alarm sound that you wish to hear at the end of this project or can use the one I will be providing with the main file
# step 3 - you need to install a new package from your terminal in order to run this project
# step 4 - open your terminal and type "pip3 install playsound3" and import it as shown
# step 5 - you need to paste the downloaded alarm sound in the same folder next to your main Python file
# step 6 - start coding


from playsound3 import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"


def alarm(seconds):
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}")

    playsound("alarm.mp3")

minutes = int(input("How many minutes to wait before the alarm goes off: "))
seconds = int(input("How many seconds to wait before the alarm goes off: "))
total_seconds = minutes * 60 + seconds

alarm(total_seconds)