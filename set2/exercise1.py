"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

# create an array called 'some_words' with 6 items in it
some_words = ["what", "does", "this", "line", "do", "?"]

# this will keep printing results of some_words until it reaches the "?" and then stop
for word in some_words:
    print(
        word
    )  # it printed all the words one after another including the "?" and then stopped looping

# I think this is the same as the above code however it is just a different way of writing the code
for x in some_words:
    print(x)  # did the same thing as the above code

# will print the whole array of: ['what', 'does', 'this', 'line', 'do', '?']
print(some_words)  # printed ['what', 'does', 'this', 'line', 'do', '?']

# if the length of one of the words in some_words is greater than 3 characters, it will print "some_words contains more than 3 words"
if len(some_words) > 3:
    print(
        "some_words contains more than 3 words"
    )  # printed some_words contains more than 3 words


def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    # Prints out my systems specs including system, node, release, version, machine, and processor
    print(platform.uname())  # prints out my system specs.


usefulFunction()
