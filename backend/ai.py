import spacy

nlp = spacy.load("en_core_web_sm")


def extract_places(user_message: str):
    doc = nlp(user_message)

    places = []
    for ent in doc.ents:
        if ent.label_ in ["GPE", "LOC", "FAC"]:
            places.append(ent.text)

    words = user_message.lower().split()

    source = None
    destination = None

    # Improved rule-based extraction
    if "from" in words and "to" in words:
        from_index = words.index("from") + 1
        to_index = words.index("to") + 1

        source = words[from_index].title()

        # Join all words after "to"
        destination = " ".join(words[to_index:]).replace("?", "").title()

    # Priority to spaCy entities if found
    if len(places) >= 2:
        source = places[0]
        destination = places[1]

    return {
        "source": source,
        "destination": destination
    }
