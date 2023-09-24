####### PERPUSTAKAAN #######

listBooks = [
    {
        "Code"      :1,
        "Title"     : "Anne of the Green Gables",
        "Genre"     : "English Literature"      ,
        "Years"     : "1908"                    ,
        "Author"    : "Lucy M. Montgomery"      
    },
    {   
        "Code"      :2,
        "Title"     : "Pride and Prejudice"     ,
        "Genre"     : "English Literature"      ,
        "Years"     : "1813"                    ,
        "Author"    : "Jane Austen"
    },
    {
        "Code"      :3,
        "Title"     : "Dilan 1990"              ,
        "Genre"     : "Novel"                   ,
        "Years"     : "2014"                    ,
        "Author"    : "Pidi Baiq"
    },
    {
        "Code"      :4,
        "Title"     : "Manusia Setengah Salmon" ,
        "Genre"     : "Comedy"                  ,
        "Years"     : "2011"                    ,
        "Author"    : "Raditya Dika"            
    }
]

#########  LIST ALL BOOKS  ####################

def listAllBooks():

    while True :

        print("LIST ALL BOOKS IN LIBRARY\n")

        print("CODE. TITLE")

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

        elif inputNums  == "2":

            createBooks()

        elif inputNums  == "3":

            changeBooks()

        elif inputNums  == "4":

            deleteBook()

        elif inputNums  == "5":

            mainMenu()
            
        elif inputNums  == "0":
                
            print("\nThank you for your service")

            exit()
        
        else:

            print("\nYou input the wrong number. Input again")
                

##########  READ  ################

def readBooks():

    print("\n##################################")

    for i in range (len(listBooks)):

            print("{}. {}, {}".format
                (listBooks[i]["Code"],listBooks[i]["Title"],listBooks[i]["Genre"]))
            
    print("\n0. Back to List Menu\n")

    while True:
            
            code = (input("Input books code that you are looking for: "))

            if code.isdigit():

                code = int(code)

                for read in listBooks:

                    if  read["Code"] == code:

                        idxRead = listBooks.index(read)

                        print("\n##################################\n")
                        
                        print("Book that you are looking for:")

                        print('''
    CODE    : {} 
    TITLE   : {} 
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
                    
                    print("\nThere's NO book with that code!\n")

                    continue
            else:
                
                print("Input VALID number!")

                continue

###########  CREATE  ###################

def createBooks():

    while True:
            
        print('''
##################################
Create MENU \n
1. List Books in the library
2. Create List Books in the library
3. Back to main menu
              
0. EXIT
            ''')

        inputNums = (input("Input following nums from [0-3]: "))

        if inputNums    == "1":

            listAllBooks()

        elif inputNums  == "2":

            code = (input("\nInput 'NEW' books code: "))

            if code.isdigit():

                code = int(code)

                for read in listBooks:

                    if read["Code"] == code:

                        idxRead = listBooks.index(read)

                        print("\n##################################")
                        
                        print("\nBook that you looking for 'ALREADY ON THE LIBRARY': \n{}. {} ".format
                            (listBooks[idxRead]["Code"],listBooks[idxRead]["Title"]))
                        
                        break
                else:

                    yesNo   = str(input("Do you want to make new Books? \nInput (Y/N): ")).capitalize()

                    if  yesNo       == "Y":

                        title       = str(input("Input 'Title' of the Book: ")).title()
                        genre       = str(input("Input 'Genre' of the Book: ")).capitalize()
                        years       = str(input("Input 'Years' of the Book: "))
                        author      = str(input("Input 'Author' of the Book: ")).title()

                        savedBooks  = {
                            "Code"      : code,
                            "Title"     : title,
                            "Genre"     : genre,
                            "Years"     : years,
                            "Author"    : author
                            }
                        
                        lastYesNo   = str(input('''
Do you REALLY want to create this data?
    CODE    : {} 
    TITLE   : {} 
    GENRE   : {}
    YEARS   : {}
    AUTHOR  : {}
                                                                                                
Input (Y/N): 
            '''.format(savedBooks["Code"],savedBooks["Title"],savedBooks["Genre"],
                       savedBooks["Years"],savedBooks["Author"]))).capitalize()

                        if lastYesNo    == "Y":

                            listBooks.append(savedBooks)

                        else:

                            print("\nBook data not created")

                    else:

                        print("\nBook data not created")

            else:
                
                print("Input VALID number!")

                continue


        elif inputNums  == "3":

            mainMenu()



        elif inputNums  == "0":
                
            print("\nThank you for your service")

            exit()
        
        else:

            print("\nYou input the wrong number. Input again")


##########  CHANGE  #################

def changeBooks():

    while True:
            
        print('''
##################################
Change MENU \n
1. List Books in the library
2. Change List Books in the library
3. Back to main menu
              
0. EXIT
            ''')

        inputNums = (input("Input following nums from [0-3]: "))

        if inputNums    == "1":

            listAllBooks()

        elif inputNums  == "2":

            print("\n##################################")

            code = (input("Input books code that you are wanted to change: "))

            if code.isdigit():

                code = int(code)

                for read in listBooks:

                    if  read["Code"] == code:

                        idxRead = listBooks.index(read)
                        
                        print("Book that you wanted to change:\n")

                        break

                else:

                    print("\nThere's NO book with that code.")

                    continue
            else:

                print("Input VALID number!")

                continue
            
            for read in listBooks:

                if  read["Code"] == code:

                    idxRead = listBooks.index(read)

                yesNo   = str(input('''
Do you want to change the content on this Book?
    CODE    : {} 
    TITLE   : {} 
    GENRE   : {}
    YEARS   : {}
    AUTHOR  : {} 
                                                                      
Input (Y/N): '''.format
                        (listBooks[idxRead]["Code"],listBooks[idxRead]["Title"],
                        listBooks[idxRead]["Genre"],listBooks[idxRead]["Years"],
                        listBooks[idxRead]["Author"]))).capitalize()

                if  yesNo       == "Y":

                    print("\nCode, Title, Genre, Years, Author")
                    print("{}. {}, {}, {}, {}".format
                        (listBooks[idxRead]["Code"],listBooks[idxRead]["Title"],
                        listBooks[idxRead]["Genre"],listBooks[idxRead]["Years"],
                        listBooks[idxRead]["Author"]))
                    
                    title       = str(input("\nInput 'Title' of the Book: ")).title()
                    genre       = str(input("Input 'Genre' of the Book: ")).capitalize()
                    years       = str(input("Input 'Years' of the Book: "))
                    author      = str(input("Input 'Author' of the Book: ")).title()

                    updatedBooks  = {
                        "Code"      : code,
                        "Title"     : title,
                        "Genre"     : genre,
                        "Years"     : years,
                        "Author"    : author
                        }
                    
                    lastYesNo   = str(input('''
Do you REALLY want to change this data?
    CODE    : {} 
    TITLE   : {}
    GENRE   : {}
    YEARS   : {}
    AUTHOR  : {}
                                            
Input (Y/N): 
            '''.format(updatedBooks["Code"],updatedBooks["Title"],updatedBooks["Genre"],
                         updatedBooks["Years"],updatedBooks["Author"]))).capitalize()



                    if lastYesNo == "Y":

                        for read in listBooks:
                            
                            if read["Code"] == code:

                                idxRead         = listBooks.index(read)
                                listBooks[idxRead].update(updatedBooks)
                                
                        break

                    else:

                        print ("\nBook data not changed")

                        break

                else:

                    print("\nBook data not changed")
                    
                    break

        elif inputNums  == "3":

            mainMenu()

        elif inputNums  == "0":
                
            print("\nThank you for your service")

            exit()
        
        else:

            print("\nYou input the wrong number. Input again")
    
#############  DELETE  ##############

def deleteBook():

    while True:
            
        print('''
##################################
Delete MENU \n
1. List Books in the library
2. Delete List Books in the library
3. Back to main menu

0. EXIT
            ''')

        inputNums = (input("Input following nums from [0-3]: "))

        if inputNums    == "1":

            listAllBooks()

        elif inputNums  == "2":

            print("\n##################################")

            code = input("Input books code that you want to delete: ")

            if code.isdigit():

                code = int(code)

                for read in listBooks:

                    if read["Code"] == code:

                        idxRead = listBooks.index(read)
                        
                        print("\nBook that you wanted to delete:")
                        
                        break

                else:

                    print("There's NO book with that code")

                    continue

            else:

                print("Input VALID number!")

                continue
                
            for read in listBooks:

                if read["Code"] == code:

                    idxRead = listBooks.index(read)

                yesNo = str(input('''
Is this the book that you want to delete?
    CODE    : {} 
    TITLE   : {} 
    GENRE   : {}
    YEARS   : {}
    AUTHOR  : {}

Input (Y/N): '''.format
                    (listBooks[idxRead]["Code"],listBooks[idxRead]["Title"],listBooks[idxRead]["Genre"],
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

                        print("\nBook data not deleted")
                
                        break
                    
                else:

                    print("\nBook data not deleted")

                    break           

        elif inputNums  == "3":

            mainMenu()

        elif inputNums  == "0":
                
            print("\nThank you for your service")

            exit()
        
        else:

            print("\nYou input the wrong number. Input again")

def mainMenu():
    while True:

        print("############## WORLD LIBRARY ##############")
        print('''
MAIN MENU \n
1. List Books in the library
2. Create List Books in the library
3. Change List Books in the library
4. Delete List Books in the library
              
0. EXIT
            ''')
        
        inputNums = (input("Input following nums from [0-4]: "))

        if inputNums    == "1":
                
                listAllBooks()

        elif inputNums  == "2":
                
                createBooks()

        elif inputNums  == "3":
                
                changeBooks()

        elif inputNums  == "4":
                
                deleteBook()

        elif inputNums  == "0":

            print("\nThank you for your service")

            exit()

        else:

            print("\nYou input the wrong number. Input again")

mainMenu()


