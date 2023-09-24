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

def listAllBooks():

    print("LIST ALL BOOKS IN LIBRARY\n")
    print("Code. Name, Genre, Years, Author")

    for i in range (len(listBooks)):

        print("{}. {}, {}, {}, {}".format
            (listBooks[i]["Code"],listBooks[i]["Name"],listBooks[i]["Genre"],
            listBooks[i]["Years"],listBooks[i]["Author"]))

# listAllBooks()

def deleteBook():

    listAllBooks()

    code = int(input("Input books code that you want to delete: "))

    for read in listBooks:

        if read["Code"] == code:

            idxRead = listBooks.index(read)
            
            print("\nBook that you wanted to delete:")
            
            break

    else:
        print("There's NO book with that code")

        return
    
    for read in listBooks:

        if read["Code"] == code:

            idxRead = listBooks.index(read)

        yesNo = str(input("Is this the book that you want to delete?\n{}. {}, {}, {}, {} \nInput (Y/N): ".format
            (listBooks[idxRead]["Code"],listBooks[idxRead]["Name"],listBooks[idxRead]["Genre"],
            listBooks[idxRead]["Years"],listBooks[idxRead]["Author"]))).capitalize()
        
        if yesNo == "Y":

            lastYesNo = str(input("DO YOU REALLY WANT TO DELETE?:\nInput (Y/N): ")).capitalize()

            if lastYesNo == "Y":

                for read in listBooks:

                    if read["Code"] == code:

                        idxRead = listBooks.index(read)

                        del listBooks[idxRead]

                break

            else:

                print("Book data not deleted")
        
                break
        
        else:

            print("Book data not deleted")

            break



deleteBook()