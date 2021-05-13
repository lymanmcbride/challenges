
def format_duration(seconds):
    #special case:
    if seconds == 0: return "now"

    #Ascertain variables: Years, days, hours, minutes, and seconds
    years = seconds//31536000 #number of seconds in a year
    #cascading variables allows for an input greater than or less than each benchmark
    yearsLeftOver = seconds - (31536000*years) if years > 0 else seconds
    days = yearsLeftOver//86400
    daysLeftOver = yearsLeftOver - (86400 * days) if days > 0 else seconds
    hours = daysLeftOver//3600
    hoursLeftOver = daysLeftOver - (3600 * hours) if hours > 0 or days > 0 else seconds
    minutes = hoursLeftOver//60
    #or statements control for the lowest value being current variable
    seconds = hoursLeftOver - (60*minutes) if minutes > 0 or hours > 0 or days > 0 else seconds 

    # put variables and labels into tuples
    times = [(years, "year"), (days, "day"), (hours, "hour"), (minutes, "minute"), (seconds, "second")]
    # add new ones to list if greater than 0
    return_string_list = [time for time in times if time[0] > 0]

    #build the string
    return_string = ""
    for i, time in enumerate(return_string_list):
        s = ""
        if time[0] > 1: s = "s" #if plural, the label needs an "s"
        conjunction = ""
        comma = ""
        if i == (len(return_string_list) - 1) and len(return_string_list) > 1: conjunction = "and " #if on last index and there's more than one thing in list: add an and
        elif i < (len(return_string_list) - 2) and len(return_string_list) > 2: comma = ", " #if not on second to last variable and our length is greater than 2
        elif i < (len(return_string_list) - 1) and len(return_string_list) > 1: comma = " "  # if not on last variable and length is greater than 1
        return_string += "{conj}{num} {label}{plural}{comma}".format(conj = conjunction, num = time[0], label = time[1], plural = s, comma = comma)
    return return_string

print(format_duration(3662))