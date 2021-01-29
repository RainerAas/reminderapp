"""
Reminder app.

By: Rainer Aas
Contact: raineraas2@gmail.com
"""

import winsound
from win10toast import ToastNotifier


def timer(reminder, minutes):
    """Timer function."""
    seconds = minutes * 60
    notificator = ToastNotifier()

    if minutes < 1:
        text = f"The alarm will go off in {seconds} seconds."
    elif minutes == 1:
        x_minutes = int(minutes)
        text = f"The alarm will go off in {x_minutes} minute."
    else:
        text = f"The alarm will go off in {minutes} minutes."

    notificator.show_toast("Reminder", text, duration=seconds)
    notificator.show_toast("Reminder", reminder, duration=0)

    for i in range(6):
        frequency = 900
        duration = 100
        winsound.Beep(frequency, duration)


if __name__ == '__main__':
    reminder_text = str(input("What would you like a reminder about? "))
    is_correct = False

    try:
        minutes = float(input("In how many minutes? "))
        is_correct = True
    except ValueError:
        print("Please enter a valid number!")

    if is_correct:
        timer(reminder_text, minutes)
