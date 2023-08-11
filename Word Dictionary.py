from PyDictionary import PyDictionary

def main():
    dictionary = PyDictionary()

    word = input("Type the word you want: ").strip()

    if word:
        meaning = dictionary.meaning(word)
        if meaning:
            print("Meaning(s) of", word.capitalize() + ":")
            for part_of_speech, definitions in meaning.items():
                print(f"{part_of_speech.capitalize()}:")
                for definition in definitions:
                    print("-", definition)
        else:
            print("Sorry, the meaning couldn't be found for", word)
    else:
        print("Please enter a valid word.")

if __name__ == "__main__":
    main()
