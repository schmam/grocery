shopping_list = {}                                  # initializes blank shopping list dictionary for user to add to

def main():
    write_list()

def write_list():
    while True:
        try:                                        # if no errors, perform this loop to allow user to enter items
            item = input("").upper()                # sets user input to uppercase to meet program output requirements
            global shopping_list                    # tells program to use global variable shopping_list defined at beginning of program
            if item not in shopping_list:
                shopping_list[item] = 1             # if added item is not in shopping list already, create new key for item in dictionary shopping_list and set number of item to 1
            else:
                shopping_list[item] += 1            # if item has been added to shopping list already, add 1 to number of item
            print(shopping_list)                    # for debugging
            continue
        except EOFError:                            # when user enters ctrl-d, break
            print("")
            print_sorted_list()
            break

def print_sorted_list():
    global shopping_list                            # tells program to use global variable shopping_list defined at beginning of program
    sorted_shopping_list = sorted(shopping_list, key = lambda kv: kv[1])      # no idea, just trying stuff
    print(sorted_shopping_list)

main()
