import csv
from datetime import date

# fixme add a navigation menu like in pattern


class Fabric:
    def __init__(self, new_woven_or_knit, new_has_stretch, new_stretch_direction, new_vertical_stretch,
                 new_horizontal_stretch, new_fabric_type, new_contents, new_length, new_width, new_weight_class,
                 new_color, new_design, new_directional, new_weight, new_source):
        self.woven_or_knit = new_woven_or_knit
        self.has_stretch = new_has_stretch
        self.stretch_direction = new_stretch_direction
        self.vertical_stretch = new_vertical_stretch
        self.horizontal_stretch = new_horizontal_stretch
        self.fabric_type = new_fabric_type
        self.contents = new_contents
        self.length = new_length
        self.width = new_width
        self.weight_class = new_weight_class
        self.color = new_color
        self.design = new_design
        self.directional = new_directional
        if new_weight:
            self.weight = new_weight
        if new_source:
            self.source = new_source
        self.date_added = date.today()
        self.last_edited = ''


def add_fabric():
    weight_class = [False, False, False]  # light, medium, heavy    # fixme use below
    woven_or_knit = [False, False]  # woven, knit                   # fixme use below

    print("Add new fabric. You may edit these fields later.")
    # Add fabric menu
    print("Woven or knit:")
    woven_or_knit = input()     # fixme update to the above list
    print("Does the fabric stretch (if fabric only has minimal mechanical stretch, input no:")
    has_stretch = (input().lower())     # fixme using the above list
    if woven_or_knit == "knit" or has_stretch == "yes":
        print("Stretch directions:")
        stretch_direction = input()
        print("Vertical stretch percent:")
        vertical_stretch = input()
        print("Horizontal stretch percent:")
        horizontal_stretch = input()
    else:
        stretch_direction = ""
        vertical_stretch = "0"
        horizontal_stretch = "0"
    print("Fabric type:")
    fabric_type = input()
    print("Contents:")
    contents = input()
    print("Fabric length (yards):")     # fixme use Units class
    length = input()
    print("Fabric width (inches):")     # fixme use Units class
    width = input()
    print("Weight classification (light, medium, heavy:)")      # fixme update to the above list
    weight_class = input()
    print("Color(s):")
    color = input()  # fixme make this a list for multicolor
    print("Fabric design (solid for none or tonal):")
    design = input()
    print("Is fabric directional? Yes or no:")
    directional = input()
    print("Weight in GSM (if unknown enter 'unknown'):")
    weight = input()
    print("Where is the fabric from:")
    source = input()
    new_fabric = Fabric(woven_or_knit, has_stretch, stretch_direction, vertical_stretch, horizontal_stretch,
                        fabric_type, contents, length, width, weight_class, color, design, directional, weight, source)
    print("New Fabric Entry:")
    # printing the new entry for review
    print_fabric_summary(new_fabric)

    #  menu after entering the info     # fixme add a separate menu like in pattern
    navigation_choice = ""
    while navigation_choice != ("cancel" or "save"):
        print("Enter 'save' to save this fabric, 'edit' to edit a field, or 'cancel' to return to main menu without "
              "saving.")
        navigation_choice = (input().lower())
        if navigation_choice == "cancel":
            return
        if navigation_choice == "save":
            write_fabric(new_fabric)
            return


def edit_fabric(some_fabric):
    print("Select a category to edit:")
    #  stretch fabric menu
    if some_fabric.has_stretch == "yes":
        print("1 - Woven or knit, 2 - Fabric stretches, 3 - Stretch direction, 4 - Vertical stretch, "
              "5 - Horizontal stretch, 6 - Type, 7 - Contents, 8 - Length, 9 - Width, 10 - Weight classification, "
              "11 - Color, 12 - Design, 13 - Directional, 14 - Weight, 15 - Source.")
        edit_choice = input()
        if edit_choice == "1":
            print("Woven or knit: {}".format(some_fabric.woven_or_knit))
            some_fabric.woven_or_knit = input()
        elif edit_choice == "2":
            print("Fabric stretches: {}".format(some_fabric.has_stretch))
            some_fabric.has_stretch = input()
        elif edit_choice == "3":
            print("Stretch direction: {}".format(some_fabric.stretch_direction))
            some_fabric.stretch_direction = input()
        elif edit_choice == "4":
            print("Vertical stretch: {}".format(some_fabric.vertical_stretch))
            some_fabric.vertical_stretch = input()
        elif edit_choice == "5":
            print("Horizontal stretch: {}".format(some_fabric.horizontal_stretch))
            some_fabric.horizontal_stretch = input()
        elif edit_choice == "6":
            print("Fabric type: {}".format(some_fabric.weight_class))
            some_fabric.weight_class = input()
        elif edit_choice == "7":
            print("Contents:{}".format(some_fabric.contents))
            some_fabric.contents = input()
        elif edit_choice == "8":
            print("Fabric length (yards): {}".format(some_fabric.woven_or_knit))  # fixme update to switchable units?
            some_fabric.length = input()
        elif edit_choice == "9":
            print("Fabric width (inches):")
            some_fabric.width = input()
        elif edit_choice == "10":
            print("Weight classification (light, medium, heavy): {}".format(some_fabric.weight_class))
            some_fabric.weight_class = input()
        elif edit_choice == "11":
            print("Color(s): {}".format(some_fabric.color))
            some_fabric.color = input()  # make this an array for multicolor
        elif edit_choice == "12":
            print("Fabric design (solid for none or tonal): {}".format(some_fabric.design))
            some_fabric.design = input()
        elif edit_choice == "13":
            print("Is fabric directional? Yes or no: {}".format(some_fabric.directional))
            some_fabric.directional = input()
        elif edit_choice == "14":
            print("Weight in GSM (if unknown enter 'unknown'): {}".format(some_fabric.weight))
            some_fabric.weight = input()
        elif edit_choice == "15":
            print("Where is the fabric from: {}".format(some_fabric.source))
            some_fabric.source = input()

    else:   # woven fabric menu
        print("1 - Woven or knit, 2 - Fabric stretches, 3 - Type, 4 - Contents, 5 - Length, 6 - Width, "
              "7 - Weight classification, 8 - Color, 9 - Design, 10 - Directional, 11 - Weight, 12 - Source.")
        edit_choice = input()
        if edit_choice == "1":
            print("Woven or knit: {}".format(some_fabric.woven_or_knit))
            some_fabric.woven_or_knit = input()
        elif edit_choice == "2":
            print("Fabric stretches: {}".format(some_fabric.has_stretch))
            some_fabric.has_stretch = (input().lower())
            if some_fabric.has_stretch == "yes":
                print("Stretch direction:")
                some_fabric.stretch_direction = input()
                print("Vertical stretch:")
                some_fabric.vertical_stretch = input()
                print("Horizontal stretch:")
                some_fabric.horizontal_stretch = input()
        elif edit_choice == "3":
            print("Fabric type: {}".format(some_fabric.weight_class))
            some_fabric.weight_class = input()
        elif edit_choice == "4":
            print("Contents:{}".format(some_fabric.contents))
            some_fabric.contents = input()
        elif edit_choice == "5":
            print("Fabric length (yards): {}".format(some_fabric.woven_or_knit))  # fixme update to switchable units?
            some_fabric.length = input()
        elif edit_choice == "6":
            print("Fabric width (inches):")
            some_fabric.width = input()
        elif edit_choice == "7":
            print("Weight classification (light, medium, heavy): {}".format(some_fabric.weight_class))
            some_fabric.weight_class = input()      # fixme update to the above lists
        elif edit_choice == "8":
            print("Color(s): {}".format(some_fabric.color))
            some_fabric.color = input()  # fixme make this a list, same above
        elif edit_choice == "9":
            print("Fabric design (solid for none or tonal): {}".format(some_fabric.design))
            some_fabric.design = input()
        elif edit_choice == "10":
            print("Is fabric directional? Yes or no: {}".format(some_fabric.directional))
            some_fabric.directional = input()
        elif edit_choice == "11":
            print("Weight in GSM (if unknown enter 'unknown'): {}".format(some_fabric.weight))
            some_fabric.weight = input()
        elif edit_choice == "12":
            print("Where is the fabric from: {}".format(some_fabric.source))
            some_fabric.source = input()
    some_fabric.last_edited = date.today()
    print("Updated Fabric Entry:")
    print_fabric_summary(some_fabric)
    print("Enter 'yes' to save this fabric, 'no' to edit a field, or 'cancel' to return to main menu without saving.")
    # fixme currently 'no' on navigation_choice would neglect to save the current edits
    # fixme add a separate menu like in pattern
    navigation_choice = (input().lower())
    while navigation_choice != "cancel":
        if navigation_choice == "yes":
            write_fabric(some_fabric)
        elif navigation_choice == "no":
            edit_fabric(some_fabric)
        elif navigation_choice == "cancel":
            exit()
        else:
            print("Sorry, I didn't understand your choice of '{}. Please enter 'yes' to save this fabric, 'no' to edit"
                  " a field, or 'cancel' to return to main menu without saving.".format(navigation_choice))
            navigation_choice = (input().lower())


def print_fabric_summary(some_fabric):
    if some_fabric.has_stretch == "no":
        no_stretch = ("Woven or knit: {}. Stretch: {}. Length: {}. Width: {}. Weight classification: {}. Color(s): {}. "
                      "Design: {}. Directional: {}. Weight: {}. Source: {}. Added: {}.")
        print(no_stretch.format(some_fabric.woven_or_knit,
                                some_fabric.has_stretch,
                                some_fabric.fabric_type,
                                some_fabric.contents,
                                some_fabric.length,
                                some_fabric.width,
                                some_fabric.weight_class,
                                some_fabric.color,
                                some_fabric.design,
                                some_fabric.directional,
                                some_fabric.weight,
                                some_fabric.source,
                                some_fabric.date_added))

    elif some_fabric.has_stretch == "yes":
        stretch = ("Woven or knit: {}. Stretch: {}. Stretch: {} ways. Vertical stretch: {}. Horizontal stretch: {}. "
                   "Fabric content: {}. Contents: {} Length: {}. Width: {}. Weight classification: {}. "
                   "Color(s): {}. Design: {}. Directional: {}. Weight: {}. Source: {}. Added: {}.")
        print(stretch.format(some_fabric.woven_or_knit,
                             some_fabric.has_stretch,
                             some_fabric.stretch_direction,
                             some_fabric.vertical_stretch,
                             some_fabric.horizontal_stretch,
                             some_fabric.fabric_type,
                             some_fabric.contents,
                             some_fabric.length,
                             some_fabric.width,
                             some_fabric.weight_class,
                             some_fabric.color,
                             some_fabric.design,
                             some_fabric.directional,
                             some_fabric.weight,
                             some_fabric.source,
                             some_fabric.date_added))


def write_fabric(some_fabric):
    try:
        with open('fabric.csv', mode='a') as file:
            fieldnames = ['woven_or_knit', 'has_stretch', 'stretch_direction', 'vertical_stretch',
                          'horizontal_stretch', 'contents', 'length', 'width', 'weight_class',
                          'color', 'design', 'directional', 'weight', 'source', 'date_added', 'last_edited']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow({'woven_or_knit': some_fabric.weight_class,
                             'has_stretch': some_fabric.has_stretch,
                             'stretch_direction': some_fabric.stretch_direction,
                             'vertical_stretch': some_fabric.vertical_stretch,
                             'horizontal_stretch': some_fabric.horizontal_stretch,
                             'contents': some_fabric.contents,
                             'length': some_fabric.length,
                             'width': some_fabric.width,
                             'weight_class': some_fabric.weight_class,
                             'color': some_fabric.color,
                             'design': some_fabric.design,
                             'directional': some_fabric.directional,
                             'weight': some_fabric.weight,
                             'source': some_fabric.source,
                             'date_added': some_fabric.date_added,
                             'last_edited': some_fabric.last_edited
                             })
            print("Fabric entry or update saved successfully.")
    except IOError:
        print("Error: could not update fabric entry.")