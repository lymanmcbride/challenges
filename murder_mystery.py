#  Version:      3.9.1
#  Name:        Lyman McBride
#  Date:        January 26, 2021
#  Purpose:     Weekly coding challenge. For this one I did have to look up the all() method. Very handy!


suspects = {'James': ['Jacob', 'Bill', 'Lucas'], 'Johnny': ['David', 'Kyle', 'Lucas'], 'Peter': ['Lucy', 'Kyle', 'Bill']}
killed = ['Lucas', 'Bill']

for key in suspects.keys():
    check = all(item in suspects[key] for item in killed)
    if check is True:
        print("The killer is: {}".format(key))
    else:
        continue