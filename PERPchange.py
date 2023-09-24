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

# def listAllBooks():

#     print("LIST ALL BOOKS IN LIBRARY\n")
#     print("Code. Name, Genre, Years, Author")

#     for i in range (len(listBooks)):

#         print("{}. {}, {}, {}, {}".format
#             (listBooks[i]["Code"],listBooks[i]["Name"],listBooks[i]["Genre"],
#             listBooks[i]["Years"],listBooks[i]["Author"]))

# listAllBooks()
def changeBooks():
    print("LIST ALL BOOKS IN LIBRARY\n")
    print("Code. Name")

    for i in range (len(listBooks)):

        print("{}. {}".format
            (listBooks[i]["Code"],listBooks[i]["Name"]))

    code = int(input("Input books code that you are wanted to change: "))

    for read in listBooks:

        if  read["Code"] == code:

            idxRead = listBooks.index(read)
               
            print("Book that you wanted to change:\n")

            break
    else:

        print("There's NO book with that code.")

        return

    for read in listBooks:

        if  read["Code"] == code:
            idxRead = listBooks.index(read)

        yesNo   = str(input("Do you want to change the content on this Book?\n{}. {} , |{}, |{}, |{} \nInput (Y/N): ".format
                (listBooks[idxRead]["Code"],listBooks[idxRead]["Name"],
                listBooks[idxRead]["Genre"],listBooks[idxRead]["Years"],
                listBooks[idxRead]["Author"]))).capitalize()
        if  yesNo       == "Y":
            print("\nCode, Title, Genre, Years, Author")
            print("{}. {}, {}, {}, {}".format
                (listBooks[idxRead]["Code"],listBooks[idxRead]["Name"],
                listBooks[idxRead]["Genre"],listBooks[idxRead]["Years"],
                listBooks[idxRead]["Author"]))
            name        = str(input("\nInput 'Title' of the Book: ")).title()
            genre       = str(input("Input 'Genre' of the Book: ")).capitalize()
            years       = str(input("Input 'Years' of the Book: "))
            author      = str(input("Input 'Author' of the Book: ")).title()
            updatedBooks  = {
                "Code"      : code,
                "Name"      : name,
                "Genre"     : genre,
                "Years"     : years,
                "Author"    : author
                }
            
            lastYesNo   = str(input("Do you REALLY want to create this data? \nInput (Y/N): ")).capitalize()

            if lastYesNo == "Y":

                for read in listBooks:
                    
                    if read["Code"] == code:

                        idxRead         = listBooks.index(read)
                        listBooks[idxRead].update(updatedBooks)
                        

                break

            else:
                print ("Not Saved")

                break

        else:
            print("Not Saved")
            
            break

changeBooks()