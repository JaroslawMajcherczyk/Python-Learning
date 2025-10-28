import time
import datetime
import pygame


def set_alarm(alarm_time):
    print(f"Alarm time: {alarm_time}")
    sound_file = "alarm-clock2.mp3"
    is_runung = True

    while is_runung:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print(f"Alarm time: {alarm_time}, WAKE UP 😴😪🥱💤🛌🏼!")

            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            if input("Enter Y key to stop: ").lower() == "y":
                pygame.mixer.music.stop()
            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_runung = False

        time.sleep(1)



if __name__ == "__main__":
    alarm_time = input("Enter the alarm time: (HH:MM:SS): ")
    set_alarm(alarm_time)