#Rules for If-Statements:

#1. Every if-statement must have an else.
#2. If this else should never run because it doesn’t make sense, then you must use a die function in
#the else that prints out an error message and dies, just like we did in the last exercise. This will
#find many errors.
#3. Never nest if-statements more than two deep and always try to do them one deep.
#4. Treat if-statements like paragraphs, where each if-elif-else grouping is like a set of sentences.
#Put blank lines before and after.
#5. Your Boolean tests should be simple. If they are complex, move their calculations to variables
#earlier in your function and use a good name for the variable.


#Rules for Loops:

#1. Use a while-loop only to loop forever, and that means probably never. This only applies to Python;
#other languages are different.
#2. Use a for-loop for all other kinds of looping, especially if there is a fixed or limited number of
#things to loop over.


#Tips for Debugging:

#1. Do not use a ”debugger.” A debugger is like doing a full-body scan on a sick person. You do not
#get any specific useful information, and you find a whole lot of information that doesn’t help and
#is just confusing.
#2. The best way to debug a program is to use print to print out the values of variables at points in
#the program to see where they go wrong.
#3. Make sure parts of your programs work as you work on them. Do not write massive files of code
#before you try to run them. Code a little, run a little, fix a little.


# HOMEWORK ----> GAME TIME:


print("""You come across 2 portals that take you to different time periods.
Do you choose Portal #1 or Portal #2? """)

portal = input("> ")

if portal == "1":
    print("You landed in ancient Egypt.")
    print("What do you do?")
    print("1. Visit the pyramids")
    print("2. See the pharaoh")

    egypt = input("> ")

    if egypt == "1":
        print("The workers and peasants stare at you, and the priest gives you a curse. Nice!")
    elif egypt == "2":
        print("You visit the pharaoh and he worships you as a God's prophet. Awesome!")
    else:
        print(f"You open your eyes and you realize it was a dream")
        print("You're confused but just shrug it off.")

elif portal == "2":
    print("You landed in the middle ages in Europe, what do you do?")
    print("1. Write the Canterbury Tales")
    print("2. Research the Bubonic Plague")
    print("3. Join a ministry full of monks and priests")

    middleage = input("> ")
    if middleage == "1":
        print("Congrats! You wrote an influential book and impacted history!")
    elif middleage == "2":
        print("You inform the public that you created a vaccine and the priests call you the devil. Nice!")
    elif middleage == "3":
        print("You spend your days reading manuscripts and decorating illuminated manuscripts for rich people. Sweet!")
    else:
        print("You contact the Plague and perish.")

else:
    print("Well, I guess a time-traveling portal isn't that cool anyways ¯\_(-_-)_/¯ ")
