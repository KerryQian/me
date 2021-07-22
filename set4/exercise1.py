"""All about IO."""


import json
import os
import requests
import inspect
import sys

from requests.models import Response

# Handy constants
LOCAL = os.path.dirname(os.path.realpath(__file__))  # the context of this file
CWD = os.getcwd()  # The curent working directory
if LOCAL != CWD:
    print("Be careful that your relative paths are")
    print("relative to where you think they are")
    print("LOCAL", LOCAL)
    print("CWD", CWD)


def get_some_details():
    """Parse some JSON.

    In lazyduck.json is a description of a person from https://randomuser.me/
    Read it in and use the json library to convert it to a dictionary.
    Return a new dictionary that just has the last name, password, and the
    number you get when you add the postcode to the id-value.
    TIP: Make sure that you add the numbers, not concatinate the strings.
         E.g. 2000 + 3000 = 5000 not 20003000
    TIP: Keep a close eye on the format you get back. JSON is nested, so you
         might need to go deep. E.g to get the name title you would need to:
         data["results"][0]["name"]["title"]
         Look out for the type of brackets. [] means list and {} means
         dictionary, you'll need integer indeces for lists, and named keys for
         dictionaries.
    """
    json_data = open(LOCAL + "/lazyduck.json").read()

    data = json.loads(
        json_data
    )  # loading data from the json_data variable defined above
    last = data["results"][0]["name"][
        "last"
    ]  # use the debugger to fine the filepath of important information
    password = data["results"][0]["login"]["password"]
    postcode = data["results"][0]["location"]["postcode"]
    id = int(data["results"][0]["id"]["value"])
    return {
        "lastName": last,
        "password": password,
        "postcodePlusID": postcode + id,
    }  # print answers


def wordy_pyramid():
    """Make a pyramid out of real words.

    There is a random word generator here:
    https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength=20
    The generator takes a single argument, length (`wordlength`) of the word.
    Visit the above link as an example.
    Use this and the requests library to make a word pyramid. The shortest
    words they have are 3 letters long and the longest are 20. The pyramid
    should step up by 2 letters at a time.
    Return the pyramid as a list of strings.
    I.e. ["cep", "dwine", "tenoner", ...]
    [
    "cep",
    "dwine",
    "tenoner",
    "ectomeric",
    "archmonarch",
    "phlebenterism",
    "autonephrotoxin",
    "redifferentiation",
    "phytosociologically",
    "theologicohistorical",
    "supersesquitertial",
    "phosphomolybdate",
    "spermatophoral",
    "storiologist",
    "concretion",
    "geoblast",
    "Nereis",
    "Leto",
    ]
    TIP: to add an argument to a URL, use: ?argName=argVal e.g. &wordlength=
    """

    pyramid = []
    for x in range(3, 20, 2):  # first loop to make triangle
        url = (
            "https://us-central1-waldenpondpress.cloudfunctions.net/"
            "give_me_a_word?"
            f"wordlength={x}"  # first half of this url is a normal string. wordlength is an fstring because we need
            # to constanly change that value of x which fstring is easily able to do
        )
        r = requests.get(url)  # goes to the url
        word = r.text  # stores the text in the url as "word"
        pyramid.append(word)
    for x in range(20, 3, -2):  # first loop but flipped
        url = (
            "https://us-central1-waldenpondpress.cloudfunctions.net/"
            "give_me_a_word?"
            f"wordlength={x}"
        )
        r = requests.get(url)
        word = r.text
        pyramid.append(word)
    return pyramid


def pokedex(low=1, high=5):
    """Return the name, height and weight of the tallest pokemon in the range low to high.

    Low and high are the range of pokemon ids to search between.
    Using the Pokemon API: https://pokeapi.co get some JSON using the request library
    (a working example is filled in below).
    Parse the json and extract the values needed.

    TIP: reading json can someimes be a bit confusing. Use a tool like
         http://www.jsoneditoronline.org/ to help you see what's going on.
    TIP: these long json accessors base["thing"]["otherThing"] and so on, can
         get very long. If you are accessing a thing often, assign it to a
         variable and then future access will be easier.
    """
    template = "https://pokeapi.co/api/v2/pokemon/{id}"  # id is in a string to be  easily changed. link is inside
    # a variable called "template"
    pokemon = []
    for p in range(low, high):
        url = template.format(
            id=p
        )  # url is now the link in template + the id that is changes every time this loop runs
        r = requests.get(url)
        if (
            r.status_code is 200
        ):  # make a request to the url and return the status code as 'integer'.status_code.
            # (more about status codes in readme.md)
            the_json = json.loads(r.text)  # parses a json string using json.loads()
            pokemon.append(the_json)
        tallest = 0
        current_tallest = "num"
        for p in pokemon:
            height = p["height"]
            if height > tallest:
                tallest = height
                current_tallest = p
    return {
        "name": current_tallest["name"],
        "weight": current_tallest["weight"],
        "height": current_tallest["height"],
    }


def diarist():
    """Read gcode and find facts about it.

    Read in Trispokedovetiles(laser).gcode and count the number of times the
    laser is turned on and off. That's the command "M10 P1".
    Write the answer (a number) to a file called 'lasers.pew' in the Set4 directory.
    TIP: you need to write a string, so you'll need to cast your number
    TIP: Trispokedovetiles(laser).gcode uses windows style line endings. CRLF
         not just LF like unix does now. If your comparison is failing this
         might be why. Try in rather than == and that might help.
    TIP: remember to commit 'lasers.pew' and push it to your repo, otherwise
         the test will have nothing to look at.
    TIP: this might come in handy if you need to hack a 3d print file in the future.
    """

    counter = 0
    mode = "r"  # read mode
    with open("set4/Trispokedovetiles(laser).gcode", mode, encoding="utf-8") as gc:
        # opening with the "with" command opens and closes the file after it is done
        gcode = (
            gc.readlines()
        )  # reading the lines one by one using .readlines() command
        for line in gcode:
            if "M10" in line:
                counter = counter + 1
        # if the string "M10" is in the line, add 1 to the counter

    mode = "w"  # write mode
    with open("set4/lasers.pew", mode, encoding="utf-8") as s:
        # tries to open a file, however file does not exist so a new file is created
        script = s.write(
            str(counter)
        )  # writing the counter into the file using .write()
        for (
            line
        ) in (
            script
        ):  # printing the counter which is stored as a string in integer "script"
            print(script)
        return script


if __name__ == "__main__":
    functions = [
        obj
        for name, obj in inspect.getmembers(sys.modules[__name__])
        if (inspect.isfunction(obj))
    ]
    for function in functions:
        try:
            print(function())
        except Exception as e:
            print(e)
    if not os.path.isfile("lasers.pew"):
        print("diarist did not create lasers.pew")
