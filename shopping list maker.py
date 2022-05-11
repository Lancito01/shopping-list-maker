import os
def clear():
    os.system('cls')
def show(list):
    try:
        print()
        number = 0
        for item in list:
            number += 1
            print(f'''\t{number}. {item}''')
        if len(list) == 1:
            print(f"\n\t\t{len(list)} item in list.\n")
        else:
            print(f"\n\t\t{len(list)} items in list.\n")
    except:
        return("List doesn't exist.")
def checkInputs(input):
    try:
        input = int(input)
    except:
        print("\nError: input wasn't an integer")
        waitForUser()
    else:
        if input >= 0 and input <=5:
            return input
        else:
            print("\nError: input wasn't an option, try again.")
            waitForUser()
def waitForUser():
    input("Press enter to continue...")
def confirm():
    a = 0
    while a == 0:
        question = input("Are you sure you want to continue?\ny for yes, n for no\n\tInput: ")
        if question.lower() == "y":
            a += 1
            return True
        elif question.lower() == "n" or question.lower() == "back":
            a += 1
            cancelling()
            return False
        else:
            print("Input must be y for yes or n for no. Try again!")
def move(list, index, to):
    index -= 1
    to -= 1
    saveItem = list[index]
    del list[index]
    list.insert(to, saveItem)
def cancelling():
    print("Cancelling operation. Returning to main menu...\n")
    waitForUser()
while True:
    clear()
    print(f"""Shopping list maker
    Choose an option:
    
    \t1 to create a new list
    \t2 to add items to the list
    \t3 to remove items from the list
    \t4 to move items in list
    \t5 to edit items
    \t0 to exit
    
    \t\t- Type "back" to come back to this menu at any time""")
    try:
        if len(list) != 0:
            print("Current list:")
            show(list)
    except:
        print()
    userInput = input("Input: ")
    userInput = checkInputs(userInput)
    if userInput == 1:
        if confirm() == True:
            list = []
            print("\nNew list created.")
            waitForUser()
        else:
            print("Cancelling operation...")
            waitForUser()
            continue
    elif userInput == 2:
        appended = input("What would you like to add to the list?\n\tInput: ")
        if appended.lower() == "back":
            print("Cancelling operation. Returning to main menu...\n")
            waitForUser()
        else:
            try:
                list.append(appended)
            except:        
                print("\nError adding item to list. Does the list exist?")
                waitForUser()
            else:
                print("Item added successfully!")
                waitForUser()
    elif userInput == 3:
        try:
            if len(list):
                listPos = input("\nWhat position is the item in that you want to delete?\n\tInput: ")
                if listPos.lower() == "back":
                    cancelling()
                else:
                    try:
                        listPos = int(listPos)
                    except:
                        print("Input wasn't an integer, try again.")
                        waitForUser()
                        continue
                    else:
                        try:
                            index = listPos - 1
                        except:
                            print("Error deleting item from list. Does the list exist?")
                            waitForUser()
                        else:
                            try:
                                print(f'The item selected is "{list[index]}".')
                            except:
                                print("Error selecting item. Is it out of bounds?")
                                waitForUser()
                            else:
                                if confirm() == True:
                                    try:
                                        del list[index]
                                    except:
                                        print("Error deleting item from list.")
                                        waitForUser()
                                    else:
                                        print("Item deleted.")
                                        waitForUser()
                                else:            
                                    print("Cancelling operation...")
                                    waitForUser()
                                    continue
        except:
            print("List doesn't exist. Try again!")
            waitForUser()                        
    elif userInput == 4:
        try:
            if len(list):
                fromWhat = input("\tWhat position is the item in that you want to move?\n\t\tInput: ")
                try:
                    fromWhat = int(fromWhat)
                except:
                    if fromWhat.lower() == "back":
                        cancelling()
                    else:
                        print("\nInput wasn't an integer. Try again!\n")
                        waitForUser()
                else:
                    toWhat = input("\tTo what position do you want to move the item?\n\t\tInput: ")
                    try:
                        toWhat = int(toWhat)
                    except:
                        if toWhat.lower() == "back":
                            cancelling()
                        else:
                            print("\nInput wasn't an integer. Try again!\n")
                            waitForUser()
                    else:
                        if fromWhat > len(list) or toWhat > len(list):
                            print("Out of bounds!")
                            waitForUser()
                        else:
                            try:
                                move(list, fromWhat, toWhat)
                            except:
                                print("Error moving item.\n")
                                waitForUser()
                            else:
                                print("Item moved successfully!\n")
                                waitForUser()
        except:
            print("List doesn't exist. Try again!")
            waitForUser()
    elif userInput == 5:
        try:
            if len(list):
                indexEdit = input("What position is the item in that you want to edit?\nInput: ")
                try:
                    indexEdit = int(indexEdit)
                except:
                    if indexEdit == "back":
                        cancelling()
                    else:
                        print("Input wasn't an integer. Try again!")
                        waitForUser()
                else:
                    realIndex = indexEdit - 1
                    original = list[realIndex]
                    edited = input(f"\n\tWhat would you like {original} to be edited to?\n\t\tInput: ")
                    print(f'"{original}" will be edited to "{edited}."')
                    if confirm() == True:
                        try:
                            del list[realIndex]
                            list.insert(realIndex, edited)
                        except:
                            print("Error editing item.")
                            waitForUser()
                        else:
                            print("Item edited successfully!")
                            waitForUser()
        except:
            print("List doesn't exist. Try again!")
            waitForUser()
    elif userInput == 0:
        if confirm() == True:
            print("Exiting program...")
            exit()
        else:
            continue
