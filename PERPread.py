listBooks = [
    {
        "Code"      :1,
        "Title"      : "Anne of the Green Gables",
        "Genre"     : "English Literature",
        "Years"     : "1908",
        "Author"    : "Lucy M. Montgomery"
    },
    {   
        "Code"      :2,
        "Title"      : "Pride and Prejudice",
        "Genre"     : "English Literature",
        "Years"     : "1813",
        "Author"    : "Jane Austen"
    }
]

# def readBooks():

#     code = int(input("Input books code that you are looking for: "))

#     for read in listBooks:

#         if  read["Code"] == code:
#             idxRead = listBooks.index(read)
               
#             print("Book that you looking for:\n")

#             print("Code, |Name, |Genre, |Years, |Author")

#             print("{}. {} , |{}, |{}, |{}".format
#                 (listBooks[idxRead]["Code"],listBooks[idxRead]["Name"],
#                 listBooks[idxRead]["Genre"],listBooks[idxRead]["Years"],
#                 listBooks[idxRead]["Author"]))

#             break
#     else:

#         print("There's NO book with that code.")

# readBooks()

def listAllBooks():

    while True :

        print("LIST ALL BOOKS IN LIBRARY\n")

        print("Code. Title")

        for i in range (len(listBooks)):

            print("{}. {}".format
                (listBooks[i]["Code"],listBooks[i]["Title"]))
        
        print('''
##################################
LIST MENU \n
1. Details of book
2. CREATE List Books in the library
3. CHANGE List Books in the library
4. DELETE List Books in the library
5. Back to main menu

0. Exit Program
            ''')
        
        inputNums = (input("Input following nums from [0-5]: "))

        if inputNums    == "1":
                
            readBooks()

        # elif inputNums  == "2":

        #     createBooks()

        # elif inputNums  == "3":

        #     changeBooks()

        # elif inputNums  == "4":

        #     deleteBook()

        # elif inputNums  == "5":

        #     mainMenu()
            
        elif inputNums  == "0":
                
            print("\nThank you for your service")

            exit()
        
        else:

            print("\nYou input the wrong number. Input again")

def readBooks():

    print("\n##################################")

    for i in range (len(listBooks)):

            print("{}. {}".format
                (listBooks[i]["Code"],listBooks[i]["Title"]))
            
    print("\n0. Back to List Menu\n")

    while True:
            
            code = (input("Input books code that you are looking for: "))

            if code.isdigit():

                code = int(code)

                for read in listBooks:

                    if  read["Code"] == code:

                        idxRead = listBooks.index(read)

                        print("\n##################################\n")
                        
                        print("Book that you looking for:")

                        print("Code. Title, Genre, Years, Author")

                        print('''
CODE    : {} 
NAME    : {} 
GENRE   : {}
YEARS   : {}
AUTHOR  : {}'''.format
                            (listBooks[idxRead]["Code"],listBooks[idxRead]["Title"],
                            listBooks[idxRead]["Genre"],listBooks[idxRead]["Years"],
                            listBooks[idxRead]["Author"]))
                        
                        readBooks()

                    elif code == 0:
                        
                        listAllBooks()

                        break

                else:
                    
                    print("There's no book with that code!")

                    break
            else:
                
                print("Input valid number!")

                continue

listAllBooks()