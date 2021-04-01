#    Coding Challenge:    Time Function
#    By:                  Lyman McBride
#    Date:                3/2/2021

#    Purpose:             Made for the wednesday coding challenge at The Tech Academy,
#                         this program takes an integer representing seconds and returns the 
#                         time in HH:MM:SS

def time(seconds):
    if seconds <= 359999:
        hours = seconds//3600
        seconds_sans_hours = seconds - (3600*hours)
        minutes = seconds_sans_hours//60
        seconds = seconds_sans_hours - minutes*60
        hours = '%02d' % hours
        minutes = '%02d' % minutes
        seconds = '%02d' % seconds
        print("{}:{}:{}".format(hours, minutes, seconds))

time(356254)