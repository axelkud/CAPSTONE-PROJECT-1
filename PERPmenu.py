listBooks = [
    {
        "Code"      :1,
        "Name"      : "Anne of the Green Gables",
        "Genre"     : "English Literature",
        "Years"     : "1908",
        "Author"    : "Lucy M. Montgomery"
    },
    {   
        "Code"      :2,
        "Name"      : "Pride and Prejudice",
        "Genre"     : "English Literature",
        "Years"     : "1813",
        "Author"    : "Jane Austen"
    }
]

def mainMenu():
    while True:
        print("############## WORLD LIBRARY ##############\n")
        print('''
MAIN MENU \n
1. List Books in the library
2. Create List Books in the library
3. Change List Books in the library
4. Delete List Books in the library
5. EXIT
            ''')
        
        inputNums = int(input("Input following nums from [1-5]: "))

        if inputNums    == 1:
                
                listAllBooks()

        elif inputNums  == 2:
                
                createBooks()

        elif inputNums  == 3:
                
                changeBooks()

        elif inputNums  == 4:
                
                deleteBook()

        elif inputNums  == 5:

            print("\nThank you for your service")

            break

        else:

            print("\nYou input the wrong number. Input again")

mainMenu()
