def checkInputs(input):
    try:
        input = int(input)
    except:
        print("\nError: input wasn't an integer")
        waitForUser()
    else:
        if input == 0 or input == 1 or input == 2 or input == 3 or input == 4:
            return input
        else:
            print("\nError: input wasn't an option, try again.")
def inputByUser():
    firstInput = input("\nChoose an option:\n\n\t1 to create a new list\n\t2 to add items to the list\n\t3 to remove items from the list\n\t4 to print list\n\t0 to exit\n\nInput: ")
    return firstInput
def inputAppend(list):
    appended = input("What would you like to add to the list?\n")
    list.append(appended)
    return list
def waitForUser():
    input("Press enter to continue...")
def confirm():
    a = 0
    while a == 0:
        question = input("Are you sure you want to continue?\ny for yes, n for no\nInput: ")
        if question.lower() == "y":
            a += 1
            return True
        elif question.lower() == "n":
            a += 1
            return False
        else:
            print("Input must be y for yes or n for no. Try again!")

print("\nShopping List Maker")
i = 1
while i == 1:
    userInput = inputByUser()
    userInput = checkInputs(userInput)
    if userInput == 1:
        if confirm() == True:
            newList = []
            print("\nNew list created.")
            waitForUser()
        else:
            print("Cancelling operation...")
            waitForUser()
            continue
    elif userInput == 2:
        try:
            inputAppend(newList)
        except:        
            print("\nError adding item to list. Does the list exist?")
            waitForUser()
        else:
            print("Item added successfully!")
    elif userInput == 3:
        listPos = input("\nWhat position is the item in that you want to delete?\n")
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
                    print(f'The item selected is "{newList[index]}".')
                except:
                    print("Error selecting item.")
                else:
                    if confirm() == True:
                        try:
                            del newList[index]
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
            print(newList)
            if len(newList) == 1:
                print(f"{len(newList)} item in list.")
            else:
                print(f"{len(newList)} items in list.")
            waitForUser()
        except:
            print("Error printing list. Does the list exist?")
            waitForUser()
    elif userInput == 0:
        if confirm() == True:
            print("Exiting program...")
            exit()
        else:
            continue
