#    Coding Challenge:    For a certain recipe, and given a certain amount of ingredients, how many cakes can you bake?
#    By:                  Lyman McBride
#    Date:                02/03/2021

#    Purpose:             Made for the wednesday coding challenge at The Tech Academy,
#                         this program returns the amount of cakes someone could bake
#                         given a certain amount of ingredients

recipe = {"Rhubarb": 1.5, "Sugar": 2.25, "Cake Flour": 2.5, "Baking Powder": 1.25, "Baking Soda": 0.25, "Salt": 0.75, "Buttermilk": 1, "Butter": 10, "Eggs": 3, "Vanilla Extract": 2}

ingredients = {"Rhubarb": 4, "Sugar": 5, "Cake Flour": 5, "Baking Powder": 3, "Baking Soda": 1, "Salt": 5, "Buttermilk": 2, "Butter": 20, "Eggs": 6, "Vanilla Extract": 1}

def make_cakes(recipe, ingredients):
    no_cakes = 0
    for ingredient in recipe.keys():
        if ingredient not in ingredients:
            print("You are mising ingredients for this cake!")
            break
        else:
            ing = ingredients[ingredient]
            rec = recipe[ingredient]
            potential_cakes = ing//rec
            if potential_cakes > 0:
                if no_cakes != 0:
                    if potential_cakes < no_cakes:
                        no_cakes = potential_cakes
                    else:
                        continue
                else:
                    no_cakes = potential_cakes
            else:
                print("You do not have enough ingredients for this cake!")
                no_cakes = 0
                break
    return "With the ingredients you have, you can bake {} cakes.".format(int(no_cakes))

                


print(make_cakes(recipe, ingredients))
