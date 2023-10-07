def add_time(startTime, durationTime, startingDay = "Monday"):
    if startTime.find("PM"):
        x = startTime.find(":")
        y = durationTime.find(":")
        result = str(int(startTime[:x]) + int(durationTime[:y])) + ":" + str(int(startTime[x + 1:].replace('PM', '')) + int(durationTime[y + 1:])) + " PM"
        print(result)
    # if startTime.find("AM"):
    #     x = startTime.find(":")
    #     y = durationTime.find(":")
    #     if int(startTime[x + 1].replace('AM', '')) + int(durationTime[y + 1]) > 59:
    #         hours = int(startTime[x + 1].replace('AM', '')) + int(durationTime[y + 1]) / 60
    #         minutes = int(startTime[x + 1].replace('AM', '')) + int(durationTime[y + 1]) % 60
    #         result = str(int(startTime[:x].replace('AM', ''))) + str(hours) + ":" + str(minutes) + "AM"
    #         print(result)
add_time("3:20 PM", "3:10")


# add_time("11:30 AM", "2:32")