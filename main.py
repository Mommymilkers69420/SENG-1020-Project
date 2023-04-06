from LinkedList import LinkedList

# Changed -
    # Added check for if the number is between 1 through 5
    # Added print statement if the input is anything other than 1 through 5
    # Cosmetic Output Changes

# Needs to be fixed/Added
    # Add check for repeated word in add word
    # Cant add numbers as words or symbols\
    # check to see if word is in dictionary before deleted, was deleting words not in dictionary
    # let user know if word is not in dictionary when deleting

def main():
    dictionary = LinkedList()
    while True:
        print("********************")
        print("1. Add word")
        print("2. Search word")
        print("3. Display dictionary")
        print("4. Delete word")
        print("5. Quit")
        print("********************")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5")
            continue

        if choice == 1:
            word = input("Enter new word: ")
            definition = input("Enter definition: ")
            dictionary.add_word(word, definition)
            print(word, "was added")
        elif choice == 2:
            word = input("Search word: ")
            definition = dictionary.search_word(word)
            if definition is not None:
                    print(word + " - " + definition)
            else:
                    print("Word not found, try again")
        elif choice == 3:
            dictionary.display_words()
        elif choice == 4:
            word = input("Enter word to delete: ")
            dictionary.delete_word(word)
            print(word, "was deleted")
        elif choice == 5:
            break
        else:
            print("Invalid choice")


if __name__ == '__main__':
    main()
