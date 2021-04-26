#    Coding Challenge:    Divide dictionaries of developers into groups and sort
#    By:                  Lyman McBride
#    Date:                4/25/2021

#    Purpose:             Made for the wednesday coding challenge at The Tech Academy,
#                         this program takes a list of dictionaries of developers info
#                         and returns their names, grouped by preferred coding language
#                         and sorted by years of experience.

#   Runtime:              O(N log N)


def devGroup(developersList):
    groups = {}
    developersList.sort(key=lambda k: k['yearsOfExperience'], reverse=True)
    for developer in developersList:
        if developer['language'] in groups.keys():
            groups[developer['language']] += ", {} {}".format(developer['firstName'], developer['lastName'])
        else:
            groups[developer['language']] = "{} {}".format(developer['firstName'], developer['lastName'])
    for language in groups.keys():
        print('{}: {}'.format(language, groups[language]))

devGroup([
    {'firstName': 'Jeff', 'lastName': 'A', 'age': 28, 'language': 'C#', 'yearsOfExperience': 5},
    {'firstName': 'Lindsey', 'lastName': 'S', 'age': 35, 'language': 'Python', 'yearsOfExperience': 3},
    {'firstName': 'Gavin', 'lastName': 'K', 'age': 46, 'language': 'Java', 'yearsOfExperience': 12}, 
    {'firstName': 'Marleen', 'lastName': 'B', 'age': 51, 'language': 'C#', 'yearsOfExperience': 20}, 
    {'firstName': 'Brent', 'lastName': 'K', 'age': 21, 'language': 'JavaScript', 'yearsOfExperience': 1}, 
    {'firstName': 'Ashley', 'lastName': 'T', 'age': 33, 'language': 'JavaScript', 'yearsOfExperience': 6}, 
    {'firstName': 'Kristen', 'lastName': 'H', 'age': 41, 'language': 'Python', 'yearsOfExperience': 9}, 
    {'firstName': 'Joshua', 'lastName': 'Y', 'age': 50, 'language': 'Python', 'yearsOfExperience': 5}    
])