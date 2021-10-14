import json 

fname = 'Recipes.json'

def rewrite():
    # Rewrites the json file 
    with open(fname, 'w') as f:
        json.dump(recipe, f, indent = 4)

def add_recipe():
    # Will add to the recipe dict format will be recipe name and a dictionary of tags 
    rname = input("What is the name of the recipe? \n")
    rvibe = input("What is the vibe of the recipe? \n")
    rtime = int(input("How long does it take to cook the recipe? \n"))
    rlink = input("What is the link? \n")

    tags = {'Vibe': rvibe, 'Time': rtime, 'link': rlink}
    recipe[rname] = tags
    
    rewrite()

def remove_recipe():
    # Removes recipe and alerts user:
    print("Here is a list of your recipes: \n")
    display()
    remove = input("Which would you like to remove?")
    removed = recipe.pop(remove)
    print(f"{removed} has been removed")

    rewrite()


def display():
    #prints out all recipes in a nice way
    for r_name, f in recipe.items():
        print(r_name)

def browse():
    # Goal is to sort through tags to see what value corresponds to each key
    v_or_t = input("Are you looking for a vibe(v) or time(t) to complete?\n")
    
    recipe_list = []

    if v_or_t == "v":
        vibe_select = input("What vibe are you looking for? \n")
        for recipes, tag in recipe.items():
            if vibe_select == tag['Vibe']:
                recipe_list.append(recipes)
    
    elif v_or_t == "t":
        time_select = int(input("How long are you willing to cook for? \n"))
        for recipes, tag in recipe.items():
            if time_select > tag['Time']:
                recipe_list.append(recipes)
    print(recipe_list)

# Does recipe.json exist?
try:
    with open(fname, 'r') as f:
        recipe = json.load(f)
except FileNotFoundError:
    recipe = {}


# Checking to see if the manager is empty, if empty force user to add recipe

if not recipe:
    print("Starting from scratch please add a recipe to begin with")
    add_recipe()
else:
    func_select = input("What would you like to do?\n Add a recipe, Browse or remove a recipe?").lower()
    
    while func_select not in ["a","b","r"]:
        print("Please input a valid response.\n a for add recipe, b for browse or r for removing a recipe")
        func_select = input("What would you like to do?\n Add a recipe, Browse or remove a recipe?").lower()
    
    if func_select == "a":
        add_recipe()
    elif func_select == "b":
        browse()
    else:
        remove_recipe()
