import os

def load_list(file):
    with open(file, "r", encoding="utf-8") as f:
        return set(f.read().splitlines())

DATA_DIR = os.path.join(os.path.dirname(__file__), "../../datasets/")
NAMES = load_list(DATA_DIR + "names.txt")
LOCATIONS = load_list(DATA_DIR + "locations.txt")
ORGS = load_list(DATA_DIR + "organizations.txt")

def ner_tag(tokens):
    result = []
    for t in tokens:
        if t in NAMES:
            result.append((t, "NAME"))
        elif t in LOCATIONS:
            result.append((t, "LOCATION"))
        elif t in ORGS:
            result.append((t, "ORG"))
        else:
            result.append((t, "O"))
    return result
