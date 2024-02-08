import csv
from datetime import date

import pdfreader

pattern_summary = ("Pattern name: {}. Pattern company: {}. Garment type: {}. Woven or knit: {}. Fabric weight "
                   "classification(s): Lightweight: {}, Medium weight: {}, Heavyweight: {}. "
                   "Yards minimum: {}. Yards maximum: {}. My size: {}.")
# fixme: update the yards if able to make that work to switch between metric and imperial, use the class Units


class Pattern:
    def __init__(self, new_name, new_company, new_garment, new_woven_or_knit, new_stretch_direction,
                 new_vertical_stretch, new_horizontal_stretch, new_contents, new_weight_class,
                 new_yards_minimum, new_yards_maximum, new_my_size):
        self.name = new_name
        self.company = new_company
        self.garment = new_garment
        self.woven_or_knit = new_woven_or_knit
        self.stretch_direction = new_stretch_direction  # fixme how to account for patterns when 2 way stretch means 4?
        self.vertical_stretch = new_vertical_stretch
        self.horizontal_stretch = new_horizontal_stretch
        self.contents = new_contents
        self.weight_class = new_weight_class  # currently a boolean list, light medium heavy
        self.yards_minimum = new_yards_minimum
        self.yards_maximum = new_yards_maximum
        self.my_size = new_my_size
        self.date_added = date.today()
        self.last_edited = ''


def pattern_menu(some_pattern):
    print("Enter 'yes' to save this pattern, 'no' to edit another field, or 'cancel' to return to main menu "
          "without saving your change.")
    navigation_choice = (input().lower())
    if navigation_choice == "cancel":
        return
    elif navigation_choice == "yes":
        write_pattern(some_pattern)
        return
    else:
        write_pattern(some_pattern)
        edit_pattern(some_pattern)


def add_pattern():
    weight_class = [False, False, False]  # light, medium, heavy
    woven_or_knit = [False, False]  # woven, knit

    # Add pattern menu and input
    print("Pattern name:")
    name = input()
    print("Pattern company:")
    company = input()
    print("Garment type:")
    garment = input()
    print("Is this pattern suitable for woven fabric? Y or N")
    woven = (input().lower())
    if woven == "y":
        woven_or_knit[0] = True
    print("Is pattern suitable for knit fabric? Y or N")
    knit = (input().lower())
    if knit == "y":
        woven_or_knit[1] = True

    if woven_or_knit[1]:    # suitable for knits
        print("Stretch directions:")
        stretch_direction = input()
        print("Vertical stretch percent:")
        vertical_stretch = input()
        print("Horizontal stretch percent:")
        horizontal_stretch = input()
    else:   # not suitable for knits
        stretch_direction = ""
        vertical_stretch = "0"
        horizontal_stretch = "0"
    print("Fabric contents required: ")
    contents = input()
    print("Fabric weight classification(s):")
    print("Lightweight? Y or N")
    light = (input().lower())
    if light == "y":
        weight_class[0] = True
    print("Medium weight? Y or N")
    medium = (input().lower())
    if medium == "y":
        weight_class[1] = True
    print("Heavyweight? Y or N")
    heavy = (input().lower())
    if heavy == "y":
        weight_class[2] = True

    print("Minimum fabric for my size:")    # fixme update to use the class Units
    yards_minimum = input()
    print("Maximum fabric for my size (excludes directional fabric needs)")  # fixme update to use the class Units
    yards_maximum = input()
    print("My size:")
    my_size = input()
    new_pattern = Pattern(name, company, garment, woven_or_knit, stretch_direction, vertical_stretch,
                          horizontal_stretch, contents, weight_class, yards_minimum, yards_maximum, my_size)
    print("New Pattern Entry:")
    print(pattern_summary.format(new_pattern.name, new_pattern.company, new_pattern.garment,
                                 new_pattern.woven_or_knit, new_pattern.stretch_direction, new_pattern.vertical_stretch,
                                 new_pattern.horizontal_stretch, new_pattern.contents, new_pattern.weight_class,
                                 new_pattern.yards_minimum, new_pattern.yards_maximum, new_pattern.my_size))
    pattern_menu(new_pattern)


def scan_pattern(pattern_text):
    woven_or_knit = [False, False]  # woven, knit
    weight_class = [False, False, False]  # light, medium, heavy

    print("Pattern name:")
    name = input()
    print("Pattern company:")
    company = input()
    print("Garment type:")
    garment = input()

    # Woven and/or knit
    if pdfreader.read_woven(pattern_text):
        woven_or_knit[0] = True
    elif pdfreader.read_knit(pattern_text):
        woven_or_knit[1] = True
    elif woven_or_knit == "":
        print("Unable to determine if woven and/or knit pattern. Is pattern suitable for woven fabric? Y or N")
        woven = (input().lower())
        if woven == "y":
            woven_or_knit[0] = True
        print("Is pattern suitable for knit fabric? Y or N")
        knit = (input().lower())
        if knit == "y":
            woven_or_knit[1] = True
    if woven_or_knit == "knit":
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
    print("Fabric contents required: ")
    contents = input()

    # Fabric weight classification(s)
    light = pdfreader.read_light(pattern_text)
    medium = pdfreader.read_medium(pattern_text)
    heavy = pdfreader.read_heavy(pattern_text)
    if light:
        weight_class[0] = True
    if medium:
        weight_class[1] = True
    if heavy:
        weight_class[2] = True
    print("Weight class: Light: {}, Medium: {}, Heavy: {}".format(weight_class[0], weight_class[1],
                                                                  weight_class[2]))
    print("Minimum fabric for my size:")    # fixme update to use the class Units
    yards_minimum = input()
    print("Maximum fabric for my size (excludes directional fabric needs)")  # fixme update to use the class Units
    yards_maximum = input()
    print("My size:")
    my_size = input()
    new_pattern = Pattern(name, company, garment, woven_or_knit, stretch_direction, vertical_stretch,
                          horizontal_stretch, contents, weight_class, yards_minimum, yards_maximum, my_size)
    print("New Pattern Entry:")
    print(pattern_summary.format(new_pattern.name, new_pattern.company, new_pattern.garment,
                                 new_pattern.woven_or_knit, new_pattern.weight_class[0],
                                 new_pattern.weight_class[1], new_pattern.weight_class[2], new_pattern.yards_minimum,
                                 new_pattern.yards_maximum, new_pattern.my_size))
    pattern_menu(new_pattern)


def edit_pattern(some_pattern):
    navigation_choice = ""
    while navigation_choice != ("cancel" or "save"):
        print("Select a pattern category to change:")
        print("1 - Pattern name, 2 - Pattern company, 3 - Garment type, 4 - Woven or knit, 5 - Fabric weight "
              "classification(s), 6 - Yards minimum, 7 - Yards maximum, 8 - My size")
        edit_choice = (input().lower())
        if edit_choice == "1":
            print("Pattern name: {}".format(some_pattern.name))
            some_pattern.name = input()
        if edit_choice == "2":
            print("Pattern company: {}".format(some_pattern.company))
            some_pattern.company = input()
        elif edit_choice == "3":
            print("Garment type:{}".format(some_pattern.garment))
            some_pattern.garment = input()
        elif edit_choice == "4":    # fixme this display is inelegant
            print("Woven: {}. Knit: {}".format(some_pattern.woven_or_knit[0], some_pattern.woven_or_knit[1]))
            print("Is this pattern suitable for woven fabric? Y or N")
            woven = (input().lower())
            if woven == "y":
                some_pattern.woven_or_knit[0] = True
            print("Is pattern suitable for knit fabric? Y or N")
            knit = (input().lower())
            if knit == "y":
                some_pattern.woven_or_knit[1] = True
        elif edit_choice == "5":
            print("Weight classification (light, medium, heavy:{})".format(some_pattern.weight_class))
            print("Lightweight? Y or N")
            light = (input().lower())
            if light == "y":
                some_pattern.weight_class[0] = True
            else:
                some_pattern.weight_class[0] = False
            print("Medium weight? Y or N")
            medium = (input().lower())
            if medium == "y":
                some_pattern.weight_class[1] = True
            else:
                some_pattern.weight_class[1] = False
            print("Heavyweight? Y or N")
            heavy = (input().lower())
            if heavy == "y":
                some_pattern.weight_class[2] = True
            else:
                some_pattern.weight_class[2] = False
            some_pattern.weight_class = input()
        elif edit_choice == "6":    # fixme update to use the class Units
            print("Yards minimum:{}".format(some_pattern.yards_minimum))
            some_pattern.yards_minimum = input()
        elif edit_choice == "7":    # fixme update to use the class Units
            print("Yards maximum: {}".format(some_pattern.yards_maximum))
            some_pattern.yards_maximum = input()
        elif edit_choice == "8":
            print("My size: {}".format(some_pattern.my_size))
            some_pattern.my_size = input()
        print("Updated Pattern Entry:")
        print(pattern_summary.format(some_pattern.name, some_pattern.company, some_pattern.garment,
                                     some_pattern.woven_or_knit, some_pattern.weight_class,
                                     some_pattern.yards_minimum, some_pattern.yards_maximum, some_pattern.my_size))
        pattern_menu(some_pattern)


def write_pattern(some_pattern):
    try:
        with open('pattern.csv', mode='a') as file:
            fieldnames = ['name', 'company', 'garment', 'woven_or_knit', 'weight_class',
                          'yards_minimum', 'yards_maximum', 'my_size']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow({'name': some_pattern.name, 'company': some_pattern.company,
                             'garment': some_pattern.garment, 'woven_or_knit': some_pattern.woven_or_knit,
                             'weight_class': some_pattern.weight_class, 'yards_minimum': some_pattern.yards_minimum,
                             'yards_maximum': some_pattern.yards_maximum, 'my_size': some_pattern.my_size})
            print("Pattern entry or update saved successfully.")
    except IOError:
        print("Error: could not update pattern entry.")