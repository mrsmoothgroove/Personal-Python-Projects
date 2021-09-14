import ast

d = open("Recipies.txt", "r+")
data = d.read()

manager = ast.literal_eval(data)


def writetofile():  # adds content to the text file
    f = open("Recipies.txt", "w")
    f.write(str(manager))


def add_recp():  # adds one recipe to
    recp_name = input("What is the recipe name?\n")
    time = input("How long does it take to cook?\n")
    vibe = input("What is the vibe?\n")
    ingredients = input("What are the ingredients?\n")
    instructions = input("What are the instructions?\n")
    manager[recp_name] = ((time, vibe), ingredients, instructions)

    writetofile()


def remove_recp():
    d.truncate()  # clears content of text file

    print("Here are the recipes,\n")
    for recp in list(manager.keys()):
        print(recp)
    recp_remove = input("What would you like to remove?\n")
    manager.pop(recp_remove)

    writetofile()


def browse_recp():  # will use conditional logic to filter out recipe according tp tag
    a = 1
    print(a)


question = input("What would you like to do?\nAdd, Remove or Browse\n")

if question.lower() == "add":
    add_recp()

if question.lower() == "remove":
    remove_recp()


