# 6 - To do list

def to_do_list():

    print("To Do List \n")

    list_to_do = []     # to store the new item
    done_list = []      # to store the removed item

    while True:
        print("Option 1 : View the list")
        print("Option 2 : Add Item")
        print("Option 3 : Mark as done / Remove Item")
        print("Option 4 : completed Item")
        print("Option 5 : Quit\n")

        options = int(input("Enter your options : "))

        # View List
        if options == 1:

            #empty list check
            if not list_to_do:
                print("Your list is empty \n")
            else:
                print("\nTo Do List")
                for item in list_to_do:
                    print(" + " + item)
                print()

        # Add
        elif options == 2:
            new_item = input("Enter your new item : ")
            list_to_do.append(new_item)
            print(" Added " + new_item + " to the list.\n")


        # Version 2 - Remove an item / mark as done
        elif options == 3:
            if not list_to_do:
                print("Your list is empty \n")
            else:
                print("\nTo Do List")       # View list
                for item in list_to_do:
                    print(" + " + item)

               #input to mark as done / remove
                item_to_remove = input("Enter your item to remove : ")
                if item_to_remove in list_to_do:
                    list_to_do.remove(item_to_remove)
                    done_list.append(item_to_remove)        # add the removed item to done_list
                    print(" Removed " + item_to_remove + " from the list.\n")
                    print(" moved the item " + item_to_remove + " to the done list.\n")
                else:
                    print("Item not found in list. Try again.")

         # version 3 - view the done item in new list
        elif options == 4:
            if not list_to_do:
                print("Your list is empty \n")
            else:
                print("\nCompleted List")
                for item in done_list:
                    print(" + " + item)
                print()

        # Exit
        elif options == 5:
            print("Bye!")
            break

to_do_list()

