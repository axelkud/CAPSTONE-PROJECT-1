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

def createBooks():
    
    listAllBooks()
    
    code = int(input("Input 'NEW' books code: "))

    for read in listBooks:

        if read["Code"] == code:
            idxRead = listBooks.index(read)
               
            print("\nBook with that code 'ALREADY ON THE LIBRARY': \n{}. {} ".format
                (listBooks[idxRead]["Code"],listBooks[idxRead]["Name"]))
            
            break

    else:

        yesNo   = str(input("Do you want to make new Books? \nInput (Y/N): ")).capitalize()
        if  yesNo       == "Y":

            name        = str(input("Input 'Title' of the Book: ")).title()
            genre       = str(input("Input 'Genre' of the Book: ")).capitalize()
            years       = str(input("Input 'Years' of the Book: "))
            author      = str(input("Input 'Author' of the Book: ")).title()
            savedBooks  = {
                "Code"      : len(listBooks)+1,
                "Name"      : name,
                "Genre"     : genre,
                "Years"     : years,
                "Author"    : author
                }
            
            lastYesNo   = str(input("Do you REALLY want to create this data? \nInput (Y/N): ")).capitalize()

            if lastYesNo    == "Y":

                listBooks.append(savedBooks)
            
            else:

                print("Not Saved")

        else:

            print("Not Saved")

createBooks()