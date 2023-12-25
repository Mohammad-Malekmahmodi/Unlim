from datetime import datetime, timedelta

def alarm_status(alarm_time, alarm_duration, wake_up_times):
    status = []

    for i in range(5):
        wake_up_time = wake_up_times[i]

        if wake_up_time < alarm_time:
            status.append("GREAT")
        elif wake_up_time <= (datetime.combine(datetime.today(), alarm_time) + alarm_duration).time():
            status.append("YES")
        else:
            status.append("NO")

    return status

def main():
    alarm_input = input("").split()
    wake_up_times_input = input("").split()

    alarm_time = datetime.strptime(alarm_input[0], '%H:%M').time()
    alarm_duration = timedelta(minutes=int(alarm_input[1]))
    wake_up_times = [datetime.strptime(time, '%H:%M').time() for time in wake_up_times_input]

    status = alarm_status(alarm_time, alarm_duration, wake_up_times)

    for i in status:
        print(i)

if __name__ == "__main__":
    main()
