import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        seconds -= 1

    print("Time's up!")

if __name__ == "__main__":
    try:
        user_input = int(input("Enter the countdown time in seconds: "))
        countdown_timer(user_input)
    except ValueError:
        print("Please enter a valid integer for the countdown time.")
