# print("hello world")

def display():
    print("===============================")
    print("|   <-- Anti-Matter Ltd. -->  |")
    print("===============================")
    print("(1)  Add Item")
    print("(2)  Remove Item")
    print("(3)  Update Item")
    print("(4)  Search In Inventory")
    print("(5)  Show All Item From Inventory")
    print("(99) Exit")
    # while True:
    try:
        choice = int(input("$> Select a option --> : "))
        selection(choice)
        # break
    except Exception:
        print("X: please Enter a Number")
        display()


def addItem():
    print("======================")
    print("|  <-- Add Item -->  |")
    print("======================")
    File = open("inventory.txt", "a")
    item_name = input("$> Which Item you want to add : ")
    item_quantity = input("$> How many Quantity you want to add : ")
    item_price = input("$> How many Price you want to add for Each item : ")
    File.write(item_name +" | " + item_price + " | " + item_quantity + "\n")
    File.close()
    continue_confirmation()


def removeItem():
    print("=======================")
    print("| <-- Remove Item --> |")
    print("=======================")
    item_name = input("$> Which Item you want to Remove or type **all for remove full inventory : ")

    File = open("inventory.txt", "r")
    allline = File.read()
    File.close()

    allline = allline.split("\n")

    newFile = open("inventory.txt", "w")
    if item_name == "**all":
        newFile.write("")
    else:
        for line in allline:
            if line == '':
                continue
            elif not line.startswith(item_name +" | "):
                newFile.write(line + "\n") 
    newFile.close()
    continue_confirmation()


def updateItem():
    print("=========================")
    print("|  <-- Update Item -->  |")
    print("=========================")
    item_name = input("$> Which Item you want to update : ")
    while True:
        try:
            item_quantity = int(input("$> Type How many Quantity You want to Increase or Decrease( - for Decrease) or Enter for not change : "))
            break
        except Exception:
            continue
    item_price = input("$> Type your updated Price or Enter for not change : ")
    with open("inventory.txt", "r") as File:
        allline = File.read()
    # print(allline)
    allline = allline.split("\n")
    with open("inventory.txt", "w") as newFile:
        for line in allline:
            if line.startswith(item_name + " | "):
                item_info = line.split(" | ")
                # Index--> 0 = item name , 1 = item Price, 2 = item Quantity
                if item_price !='':
                    item_info[1] = item_price
                if item_quantity !='':
                    item_info[2] = str(int(item_info[2]) + item_quantity)
                newline = " | ".join(item_info)
                newFile.write(newline + "\n")
                
            elif line == '':
                continue
            else:
                newFile.write(line + "\n")
    continue_confirmation()


def searchItem():
    print("=========================")
    print("|  <-- Search Item -->  |")
    print("=========================")
    item_name = input("$> Which Item information you want to Search : ")
    File = open("inventory.txt", "r")
    allline = File.read()
    File.close()
    allline = allline.split("\n")
    x = 1
    for line in allline:
        if item_name.lower() in line.lower():
            item_info = line.split(" | ")
            # Index--> 0 = item name , 1 = item Price, 2 = item Quantity
            print("\n===============================")
            print("Item ID            :", x)
            print("Item Name          :", item_info[0])
            print("Per Item Price     :", item_info[1] + " $")
            print("Available Quantity :", item_info[2])
            print("===============================\n")
        x += 1
    continue_confirmation()

def allItems():
    print("===========================")
    print("|  <-- Show All Item -->  |")
    print("===========================")
    File = open("inventory.txt", "r")
    allline = File.read()
    File.close()
    allline = allline.split("\n")
    # print(allline)
    x = 1
    for line in allline:
        if line == '':
            continue
        item_info = line.split(" | ")
            # Index--> 0 = item name , 1 = item Price, 2 = item Quantity
        print("\n===============================")
        print("Item ID            :", x)
        print("Item Name          :", item_info[0])
        print("Per Item Price     :", item_info[1] + " $")
        print("Available Quantity :", item_info[2])
        print("===============================\n")
        x += 1
    print("-----------------")
    print(" Total Item :",x-1)
    print("-----------------")
    continue_confirmation()


def selection(choice):
    if choice == 1:
        addItem()
    elif choice == 2:
        removeItem()
    elif choice == 3:
        updateItem()
    elif choice == 4:
        searchItem()
    elif choice == 5:
        allItems()
    elif choice == 99:
        print("Good Bye !!!")
        exit()
    else:
        print("X: Enter a valid Number")
        display()


def continue_confirmation():
    userInput = input("$> Press Enter for Continue or 99 for Exit : ")
    if userInput == "":
        display()
    elif userInput == "99":
        print("Good Bye !!!")
        exit()
    else:
        continue_confirmation()


if __name__ == "__main__":
    display()

