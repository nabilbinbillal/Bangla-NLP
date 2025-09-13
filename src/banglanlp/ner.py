def load_dataset(file_path):
    with open(file_path, encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]

NAMES = set(load_dataset("datasets/names.txt"))
LOCATIONS = set(load_dataset("datasets/locations.txt"))
ORGANIZATIONS = set(load_dataset("datasets/organizations.txt"))

def ner_tag(tokens):
    tagged = []
    for word in tokens:
        if word in NAMES:
            tagged.append((word, "NAME"))
        elif word in LOCATIONS:
            tagged.append((word, "LOCATION"))
        elif word in ORGANIZATIONS:
            tagged.append((word, "ORG"))
        else:
            tagged.append((word, "O"))
    return tagged
