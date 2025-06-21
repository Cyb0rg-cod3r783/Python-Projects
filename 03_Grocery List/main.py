# Grocery List

grocery_list = []

while True:

    print("Options : add / remove / view")
    action = input("Enter what you want to do : ")

    if (action == "add"):
        item = input("Enter the item you want to add : ")
        grocery_list.append(item)
        print("Item added succesfully!!")

    elif(action == "remove"):
        item = input("Enter the item to be removed : ")
        if item in grocery_list:
            grocery_list.remove(item)
            print("Item removed successfully!!")
        else:
            print("No such item in the list")

    elif(action == "view"):
        print(grocery_list)

    else:
        print("Invalid option entered, please enter a valid opiton")