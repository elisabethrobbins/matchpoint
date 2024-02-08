from pdfminer.high_level import extract_text


def load_pattern(pdf_file):
    try:
        pattern_text = extract_text(pdf_file)
        print("Pattern read successfully.")
        return pattern_text
    except IOError:
        print("Error: Pattern was not read successfully.")


def read_knit(pattern_text):
    if pattern_text.find("knit") != -1:
        return True
    elif pattern_text.find("Knit") != -1:
        return True
    else:
        return False


def read_woven(pattern_text):
    if pattern_text.find("woven") != -1:
        return True
    elif pattern_text.find("Woven") != -1:
        return True
    else:
        return False


def read_light(pattern_text):
    if pattern_text.find("light") != -1:
        return True
    elif pattern_text.find("Light") != -1:
        return True
    else:
        return False


def read_medium(pattern_text):
    if pattern_text.find("medium") != -1:
        return True
    elif pattern_text.find("Medium") != -1:
        return True
    else:
        return False


def read_heavy(pattern_text):
    if pattern_text.find("heavy") != -1:
        return True
    elif pattern_text.find("Heavy") != -1:
        return True
    else:
        return False