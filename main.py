import sys
import pdfreader
import fabric
import pattern
import units


# fixme major change: eventually add the ability to save profiles. Could be saving basic measurements? Just sizes?


# fixme currently not operational, but aspirational and would be better
class Menu:
    def __init__(self, menu_option):
        if menu_option == "find match":
            print("You will be able to find a match")
        elif menu_option == "add fabric":
            print("You will be able to add fabric")
        elif menu_option == "remove fabric":
            print("You will be able to remove fabric")
        elif menu_option == 'add pattern':
            print("Make new pattern go brrrr")


def read_measuring_preference():    # fixme update to use the class Units
    file = open("preferences.txt", "r")
    preference = (file.read())
    file.close()
    return preference


def change_measuring_preference(unit):  # fixme update to use the class Units
    try:
        with open("preferences.txt", "w") as file:
            file.write(unit)
            print("Measuring system preference saved successfully.")
    except IOError:
        print("Error: could not update measuring system preference.")
    file.close()

measuring_units = units.Units(read_measuring_preference())

patterns = []  # fixme make this read from a CSV or something on program start
fabrics = []  # fixme make this read from a CSV or something on program start


# fixme potential problem in switching between yards and meters: could change amount of fabric if change too much??
# fixme might have to keep as one or the other then swap?? keep an original amount??? overthinking it?????

# working menu
print("Enter the number that corresponds to your option:")
menu = ("1 - Find match*, 2 - Add fabric, 3 - Remove fabric*, 4 - Add pattern, 5 - Remove pattern*, "
        "6 - Change measuring units (yards or meters), 7 - Quit. (* = option under construction)")

#  fixme add an inventory display option and a queue

menu_selection = ""
while menu_selection != "7":
    print(menu)
    menu_selection = input()
    if menu_selection == '1':
        print("Will put stuff here")
        print(menu)
        menu_selection = input()

    elif menu_selection == '2':  # add fabric
        fabric.add_fabric()
        print(menu)
        menu_selection = input()

    elif menu_selection == '3':  # remove fabric
        print("Will put stuff here.")
        print(menu)
        menu_selection = input()

    elif menu_selection == '4':  # add pattern
        print("Enter 1 to scan a pattern's PDF instructions for faster entry or 2 to enter a pattern manually")
        entry = input()
        if entry == "1":  # scan
            pdf_file = "Weiland Tank Instructions.pdf"
            pattern_text = pdfreader.load_pattern(pdf_file)
            pattern.scan_pattern(pattern_text)
        elif entry == "2":  # manually
            pattern.add_pattern()
        else:
            print("Sorry, {} was not a valid option.", entry)
        print(menu)
        menu_selection = input()

    elif menu_selection == '5':  # remove pattern
        print("Cast it into the fire! But not quite yet.")
        print(menu)
        menu_selection = input()

    elif menu_selection == '6':  # fixme change measuring units, update to use the class Units
        current_unit = read_measuring_preference()
        print("Measuring system is currently set to {}.".format(current_unit))
        if current_unit == "imperial":
            print("Would you like to change to metric measurements? Enter yes to change or no to cancel.")
            yes_or_no = input().lower()
            if yes_or_no == "yes":
                updated_unit = "metric"
                change_measuring_preference(updated_unit)
                print(menu)
                menu_selection = input()
            elif yes_or_no == "no":
                print(menu)
                menu_selection = input()
        elif current_unit == "meters":
            print("Would you like to change to imperial measurements? Enter yes to change or no to cancel.")
            yes_or_no = input().lower()
            if yes_or_no == "yes":
                updated_unit = "meters"
                change_measuring_preference(updated_unit)
                print(menu)
                menu_selection = input()
            elif yes_or_no == "no":
                print(menu)
                menu_selection = input()
    # closing program
    elif menu_selection == '7':
        print("Stopping the program. Goodbye for now and happy sewing!")
        sys.exit()