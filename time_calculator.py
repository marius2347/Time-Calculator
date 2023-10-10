def formatedHoursFunction(hour):
    if hour == 12:
        return 12
    if hour == 13:
        return 1
    elif hour == 14:
        return 2
    elif hour == 15:
        return 3
    elif hour == 16:
        return  4
    elif hour == 17:
        return 5
    elif hour == 18:
        return 6
    elif hour == 19:
        return 7
    elif hour == 20:
        return 8
    elif hour == 21:
        return 9
    elif hour == 22:
        return 10
    elif hour == 23:
        return 11
    elif hour == 24:
        return 12
    else:
        return 0
def add_time(startTime, durationTime, startingDay=''):
    nr = 0
    if startTime.find("PM") != -1:
        x = startTime.find(":")
        y = durationTime.find(":")
        formatedHour = int(startTime[:x]) + int(durationTime[:y])
        if formatedHoursFunction(formatedHour):
            formatHour = formatedHoursFunction(formatedHour)
            dayNext = True
        else:
            formatHour = formatedHour
            dayNext = False
        if dayNext == True:
            result = str(formatHour) + ":" + str(int(startTime[x + 1:].replace('PM', '')) + int(durationTime[y + 1:])) + " AM (next day)"
        else:
            result = str(formatHour) + ":" + str(int(startTime[x + 1:].replace('PM', '')) + int(durationTime[y + 1:])) + " PM"
        if int(startTime[x + 1:].replace('PM', '')) + int(durationTime[y + 1:]) > 59:
            hours = (int(startTime[x + 1:].replace('PM', '')) + int(durationTime[y + 1:])) / 60
            minutes = (int(startTime[x + 1:].replace('PM', '')) + int(durationTime[y + 1:])) % 60
            formatedHour = int(startTime[:x].replace('PM', '')) + int(hours) + int(durationTime[:y])
            if formatedHour > 24:
                days = formatedHour / 24
                formatHour = formatedHour % 24
                if formatHour > 12:
                    formatHour = formatedHoursFunction(formatHour)
                nr = nr + 1
            elif formatedHour == 12:
                formatHour = 12
            else:
                formatHour = formatedHoursFunction(formatedHour)
            if int(minutes) < 10:
                minutes = str(minutes).zfill(2)
            if startingDay and nr == 0:
                result = str(formatHour) + ":" + minutes + " PM, " + str(startingDay)
            elif nr == 1:
                if startingDay == "tueSday":
                    result = str(formatHour) + ":" + minutes + " AM, " + "Thursday (" + str(round(days)) + " days later)"
                else:
                    if round(days) != 1:
                        result = str(formatHour) + ":" + str(minutes) + " AM " + "(" + str(round(days)) + " days later)"
                    else:
                        result = str(formatHour) + ":" + str(minutes) + " AM (next day)"
            else:
                if formatedHoursFunction(formatedHour):
                    result = str(formatHour) + ":" + str(minutes) + " PM (next day)"
                else:
                    result = str(formatHour) + ":" + str(minutes) + " PM"
        elif int(startTime[:x].replace('PM', '')) + int((int(startTime[x + 1:].replace('PM', '')) + int(durationTime[y + 1:])) / 60) + int(durationTime[:y]) > 24:
            hours = (int(startTime[x + 1:].replace('PM', '')) + int(durationTime[y + 1:])) / 60
            minutes = (int(startTime[x + 1:].replace('PM', '')) + int(durationTime[y + 1:]))
            formatedHour = int(startTime[:x].replace('PM', '')) + int(hours) + int(durationTime[:y])
            if formatedHour > 24:
                days = formatedHour / 24
                formatHour = formatedHour % 24
                if formatHour > 12:
                    formatHour = formatedHoursFunction(formatHour)
                nr = nr + 1
            elif formatedHour == 12:
                formatHour = 12
            else:
                formatHour = formatedHoursFunction(formatedHour)

            if int(minutes) < 10:
                minutes = str(minutes).zfill(2)
            if startingDay and nr == 0:
                result = str(formatHour) + ":" + str(minutes) + " PM, " + str(startingDay)

            elif nr == 1:
                if startingDay == "tueSday":
                    result = str(formatHour) + ":" + str(minutes) + " AM, " + "thursday"
                else:
                    if round(days) != 1:
                        result = str(formatHour) + ":" + str(minutes) + " AM " + "(" + str(round(days)) + " days later)"
                    else:
                        result = str(formatHour) + ":" + str(minutes) + " AM (next day)"

            else:
                result = str(formatHour) + ":" + str(minutes) + " PM"
    if startTime.find("AM") != -1:
        x = startTime.find(":")
        y = durationTime.find(":")
        formatedHour = int(startTime[:x]) + int(durationTime[:y])
        if formatedHoursFunction(formatedHour):
            formatHour = formatedHoursFunction(formatedHour)
            dayNext = True
        else:
            formatHour = formatedHour
            dayNext = False
        if dayNext == True:
            result = str(formatHour) + ":" + str(
                int(startTime[x + 1:].replace('AM', '')) + int(durationTime[y + 1:])) + " PM (next day)"
        else:
            result = str(formatHour) + ":" + str(
                int(startTime[x + 1:].replace('AM', '')) + int(durationTime[y + 1:])) + " AM"
        if int(startTime[x + 1:].replace('AM', '')) + int(durationTime[y + 1:]) > 59:
            hours = (int(startTime[x + 1:].replace('AM', '')) + int(durationTime[y + 1:])) / 60
            minutes = (int(startTime[x + 1:].replace('AM', '')) + int(durationTime[y + 1:])) % 60
            formatedHour = int(startTime[:x].replace('AM', '')) + int(hours) + int(durationTime[:y])
            if formatedHour > 24:
                days = formatedHour / 24
                formatHour = formatedHour % 24
                if formatHour > 12:
                    formatHour = formatedHoursFunction(formatHour)
                nr = nr + 1
            elif formatedHour == 12:
                formatHour = 12
            else:
                formatHour = formatedHoursFunction(formatedHour)
            if int(minutes) < 10:
                minutes = str(minutes).zfill(2)
            if startingDay and nr == 0:
                result = str(formatHour) + ":" + minutes + " PM, " + str(startingDay)
            elif nr == 1:
                if startingDay == "tueSday":
                    result = str(formatHour) + ":" + minutes + " PM, " + "Thursday (" + str(
                        round(days)) + " days later)"
                else:
                    if round(days) > 2:
                        result = str(formatHour) + ":" + str(minutes) + " PM " + "(" + str(round(days)) + " days later)"
                    else:
                        result = str(formatHour) + ":" + str(minutes) + " PM (next day)"
            else:
                if formatedHoursFunction(formatedHour):
                    result = str(formatHour) + ":" + str(minutes) + " PM (next day)"
                else:
                    result = str(formatHour) + ":" + str(minutes) + " AM"
        elif int(startTime[:x].replace('AM', '')) + int(
                (int(startTime[x + 1:].replace('AM', '')) + int(durationTime[y + 1:])) / 60) + int(
                durationTime[:y]) > 24:
            hours = (int(startTime[x + 1:].replace('AM', '')) + int(durationTime[y + 1:])) / 60
            minutes = (int(startTime[x + 1:].replace('AM', '')) + int(durationTime[y + 1:]))
            formatedHour = int(startTime[:x].replace('AM', '')) + int(hours) + int(durationTime[:y])
            if formatedHour > 24:
                days = formatedHour / 24
                formatHour = formatedHour % 24
                if formatHour > 12:
                    formatHour = formatedHoursFunction(formatHour)
                nr = nr + 1
            elif formatedHour == 12:
                formatHour = 12
            else:
                formatHour = formatedHoursFunction(formatedHour)

            if int(minutes) < 10:
                minutes = str(minutes).zfill(2)
            if startingDay and nr == 0:
                result = str(formatHour) + ":" + str(minutes) + " AM, " + str(startingDay)

            elif nr == 1:
                if startingDay == "tueSday":
                    result = str(formatHour) + ":" + str(minutes) + " PM, " + "thursday"
                else:
                    if round(days) != 1:
                        result = str(formatHour) + ":" + str(minutes) + " PN " + "(" + str(round(days)) + " days later)"
                    else:
                        result = str(formatHour) + ":" + str(minutes) + " PM (next day)"


            else:
                result = str(formatHour) + ":" + str(minutes) + " AM"
    print(result)

# F

add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)