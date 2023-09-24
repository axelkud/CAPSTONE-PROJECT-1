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

listAllBooks()