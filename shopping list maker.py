def checkInputs(input):
    try:
        input = int(input)
    except:
        print("\nError: input wasn't an integer")
        waitForUser()
    else:
        if input == 0 or input == 1 or input == 2 or input == 3 or input == 4 or input == 5 or input == 6:
            return input
        else:
            print("\nError: input wasn't an option, try again.")
def inputByUser():
    firstInput = input("""Choose an option:
    
    \t1 to create a new list
    \t2 to add items to the list
    \t3 to remove items from the list
    \t4 to print list
    \t5 to move items in list
    \t6 to edit items
    \t0 to exit
    
    \t\t- Type "back" to come back to this menu at any time
    Input: """)
    return firstInput
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
print("\nShopping List Maker")
while True:
    userInput = inputByUser()
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
    elif userInput == 3:
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
                        print("Error selecting item.")
                    else:
                        if confirm() == True:
                            try:
                                del list[index]
                            except:
                                print("Error deleting item from list. Is the item selected out of bounds?")
                            else:
                                print("Item deleted.")
                                waitForUser()
                        else:            
                            print("Cancelling operation...")
                            waitForUser()
                            continue
    elif userInput == 4:
        try:
            print()
            number = 1
            for item in list:
                print(f'''\t{number}. {item}''')
                number += 1
            if len(list) == 1:
                print(f"\n{len(list)} item in list.\n")
            else:
                print(f"\n{len(list)} items in list.\n")
            waitForUser()
        except:
            print("Error printing list. Does the list exist?")
            waitForUser()
    elif userInput == 5:
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
                try:
                    move(list, fromWhat, toWhat)
                except:
                    print("Error moving item.\n")
                else:
                    print("Item moved successfully!\n")
    elif userInput == 6:
        indexEdit = input("What position is the item in that you want to edit?")
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
    elif userInput == 0:
        if confirm() == True:
            print("Exiting program...")
            exit()
        else:
            continue
