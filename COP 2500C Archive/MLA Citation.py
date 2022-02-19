# Gradi Tshielekeja Mbuyi
# COP 2500C
# MLA Citation Generator
# Nov 8, 2021

# changes string to title
# removes spaces in front and at the end of string
def userInput(a):
    a = a.strip()
    a = a.title()

    return a

# MLA formating
# inspired by scribbr.com/mla-citation-generator/
def book():

    # asks user for the book's title/name
    # saves input in a variable
    print("\n-Information on the book-")
    title = input("\nBook Title: ")
    title = userInput(title)

    # asks user for the publisher's name
    # asks user for the publication date
    # saves each input in two variable
    print("\n-Information on the publisher-")
    publisher = input("\nPlubisher: ")
    publisher = userInput(publisher)

    publication = int(input("Year of publicantion: "))

    # ask users about the author(s)
    print("\n-Information on the author(s)-")

    # in case there are multiple author
    # empty list for author names
    multipleLastName = []
    multipleFirstName = []

    # ask user how many author are credited in the book
    numAuthor = int(input("\nHow many author(s) are credited in the book? "))

    # if user inputs a number less than 1
    # user indicates that there's no author credited
    if(numAuthor < 1):

        # error will be used to break the while loop
        error = 0

        # while loop will be used to make sure user input "Yes" or "No"
        while(error == 0):

            # ask user if there's an organization credited
            # saves user's response
            organization = input("\nIs an organization credited for the book? ")
            organization = userInput(organization)

            # if user input "Yes" or "No"
            # loop breaks
            if(organization == "Yes" or organization == "No"):

                error = 1
                
                # if there's an organization credited
                # asks user to input organization name
                # loop stops
                if(organization == "Yes"):
                    organizationName = input("\nOrganization: ")
                    organizationName = userInput(organizationName)
                    
                else:

                    # if there's no organization credited
                    # loop stops
                    if(organization == "No"):
                        organizationName = ""
                        
            # if user inputs anything else but "No" or "Yes"
            # loop continues / ask user to answer the question properly
            else:

                print("\nInvalid input... (Please try again)")
                error = 0

    # user indicates that there's one author credited    
    elif(numAuthor == 1):

        # ask user to input author's first and last name
        lastName = input("\nAuthor's last name: ")
        lastName = userInput(lastName)

        firstName = input("Author's first name: ")
        firstName = userInput(firstName)

    # user indicates that there's two authors credited
    elif(numAuthor == 2):

        # program uses lists to save both of the author's name
        for x in range(1, numAuthor+1):
            print("\nAuthor #", x, ":", sep="")

            lastName = input("\nAuthor's last name: ")
            lastName = userInput(lastName)

            firstName = input("Author's first name: ")
            firstName = userInput(firstName)

            multipleLastName.append(lastName)
            multipleFirstName.append(firstName)

    # user indicates that there's more than two author's credited
    # program ask for the main author's name
    elif(numAuthor > 2):
        lastName = input("\nMain author's last name: ")
        lastName = userInput(lastName)

        firstName = input("Main author's first name: ")
        firstName = userInput(firstName)

    # program prints the citation given that there's no author credited 
    if(numAuthor < 1):

        # programs prints the citation given that there's an organization credited
        if(organization == "Yes"):
            print("\n-MLA Citation Format-")

            print("\nWorks Cited entry:")
            print(organizationName, ". ", title, ". ", publisher, ", ", publication, ".", sep="")
        
            print("\nIn-text citation: ")
            print("Parenthetical: (", organizationName, " -Page Number-)", sep = "")
            print("Narrative: ", organizationName, " (-Page Number-)", sep = "")

        # program prints the citation given that there's no organization or author credited
        elif(organization == "No"):
            print("\n-Format-")
            
            print("\nWorks Cited entry: \n")
            print(title, ". ", publisher, ", ", publication, ".", sep="")

    # program prints the citation given that there's one author credited 
    elif(numAuthor == 1):
        print("\n-MLA Citation Format-")

        print("\nWorks Cited entry:")
        print(lastName, ", ", firstName, ". ", title, ". ", publisher, ", ", publication, ".", sep="")
        
        print("\nIn-text citation: ")
        print("Parenthetical: (", lastName, " -Page Number-)", sep = "")
        print("Narrative: ", lastName, " (-Page Number-)", sep = "")

    # program prints the citation given that there's two authors credited     
    elif(numAuthor == 2):
        print("\n-MLA Citation Format-")

        print("\nWorks Cited entry:")
        print(multipleLastName[0], ", ", multipleFirstName[0], ", and ", multipleFirstName[1], " ", multipleLastName[1] ,". ", title, ". ", publisher, ", ", publication, ".", sep="")

        print("\nIn-text citation: ")
        print("Parenthetical: (", multipleLastName[0], " and ", multipleLastName[1], " -Page Number-)", sep = "")
        print("Narrative: ", multipleLastName[0], " and ", multipleLastName[1], " (-Page Number-)", sep = "")

    # program prints the citation given that there's more than two authors credited 
    elif(numAuthor > 2):
        print("\n-MLA Citation Format-")

        print("\nWorks Cited entry: ")
        print(lastName, ", ", firstName, ", et al. ", title, ". ", publisher, ", ", publication, ".", sep="")
        
        print("\nIn-text citation: ")
        print("Parenthetical: (", lastName, " et al. -Page Number-)", sep = "")
        print("Narrative: ", lastName, " et al. (-Page Number-)", sep = "")


# where the program starts
# purpose: this will help UCF students properly cite their book sources when working on Essays/Papers

# title of the program
print("\nMLA CITATION (BOOK)")


# this loops gives the user the ability to use the program as long as they want
# can "end" the program
end = False
while(end == False):

    # MLA formating
    # function is called for the first time
    book()

    # this variable can break or continue the loop
    error = 0

    # this while loop will run at least 1 time
    while(error == 0):

        # ask user if they want to cite another book
        retry = input("\nWould you like to cite another book? ")
        retry = userInput(retry)

        # breaks the while loop
        # restarts the program
        if(retry == "Yes"):
            end = False
            error = 1

        # breaks the while loop
        # ends the program
        elif(retry == "No"):
            end = True
            error = 1

            print("\nYou're all done!")

        # continues the while loop
        # ask users to properly respond to the question
        else:
            print("\nInvalid input... (Please try again)")
            error = 0
