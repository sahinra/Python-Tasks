# Create a program that allows users to enter a word and get its definition and synonyms.
# (Requires: PyDictionary library or an API like WordNet)

from PyDictionary import PyDictionary


def get_meanings_and_synonyms(word):
    dictionary = PyDictionary()
    meaning = dictionary.meaning(word)
    synonyms = dictionary.synonym(word)

    return meaning, synonyms


def main():
    word = input("Please enter a word: ")

    meaning, synonyms = get_meanings_and_synonyms(word)

    if meaning and synonyms:
        print(f"\nDefinition of '{word}':")
        for part_of_speech, meanings in meaning.items():
            print(f"{part_of_speech.capitalize()}: {', '.join(meanings)}")

        print(f"\nSynonyms of '{word}':")
        print(', '.join(synonyms))
    else:
        print(f"Missing information")
    meaning.max()


if __name__ == "__main__":
    main()