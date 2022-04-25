def checkInputs(input):
    try:
        input = int(input)
    except:
        print("\nError: input wasn't an integer")
        wait()
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

def wait():
    input("Press enter to continue...")

def confirm():
    a = 0
    while a == 0:
        question = input("Are you sure you want to continue?\ny for yes, n for no\nInput: ")
        if question == "y" or question == "Y":
            a += 1
            return True
        elif question == "n" or question == "N":
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
            wait()
        else:
            print("Cancelling operation...")
            wait()
            continue
    elif userInput == 2:
        try:
            if confirm() == True:
                inputAppend(newList)
                wait()
            else:
                print("Cancelling operation...")
                wait()
                continue
        except:
            print("\nError adding item to list. Does the list exist?")
            wait()
    elif userInput == 3:
        listPos = input("\nWhat position is the item in that you want to delete?\n")
        try:
            listPos = int(listPos)
        except:
            print("Input wasn't an integer, try again.")
            wait()
            continue
        else:
            try:
                index = listPos - 1
            except:
                print("Error deleting item from list. Does the list exist?")
                wait()
            else:
                try:
                    if listPos < len(newList) or listPos > len(newList):
                        print("Error deleting item from list. Is the position you inputted not part of the list?")
                        wait()
                        continue
                    else:
                        if confirm() == True:
                            del newList[index]
                            print("Item deleted.")
                            wait()
                        else:
                            print("Cancelling operation...")
                            wait()
                            continue
                except:
                    print("Error deleting item from list. Does the list exist?")
                    wait()
                    continue
    elif userInput == 4:
        try:
            print(newList)
            if len(newList) == 1:
                print(f"{len(newList)} item in list.")
            else:
                print(f"{len(newList)} items in list.")
            wait()
        except:
            print("Error printing list. Does the list exist?")
            wait()
    elif userInput == 0:
        if confirm() == True:
            print("Exiting program...")
            exit()
        else:
            continue