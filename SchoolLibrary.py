# --------------------------------------------------------------------------------------------------------------------*
# SCHOOL LIBRARY: CODED by MR.AratioD. 2016
# --------------------------------------------------------------------------------------------------------------------*

# **********************************************************************************************************************
# FUNCTION: Ask user specify file name to open it as a database
print "Please create in a folder empty ANSI .txt file or open old one. "
fileName = raw_input("Please input full file name with a file type --> ")



# **********************************************************************************************************************
# FUNCTION libraryInAlphabeticalOrder() sorts text file database in a alphabetical order
def libraryInAlphabeticalOrder():
    global libraryDatabase
    global sortingName
    global name

    with open(fileName, 'r') as sortingName:
        libraryDatabase = sorted(name.rstrip('\n') for name in sortingName)

    # print (names)
    for item in libraryDatabase:
        print item


pass

# Print a line to make user interface look nicer***********************************************************************
print ""

# MAIN PROGRAMM*********************************************************************************************************
# FUNCTION: To provide three different fucntions to user
# INTERFACE: All actions will writed in TXT database file

while True:

# QUESTIONS: to user
    print 'Your options--> '
    print '1) Add new book '
    print '2) Print current database '
    print 'Q) Exit the program '
    inputCommand = raw_input("--> ")

# The conditions add new data into database
    if inputCommand.strip() == '1':
        writer = raw_input("Name: Lastname Surname --> ")
        title = raw_input("Title --> ")
        ISBN = raw_input("ISBN --> ")

        inputToFile = "WRITER: " + writer + ", TITLE: " + title + ", ISBN: " + ISBN
        print inputToFile
        inputCommand2 = raw_input("Do you want to update database: -->YES/NO ")

# If YES, then input file into database
        if inputCommand2.strip() == 'YES':
            fileinput = open(fileName, 'a')
            print>> fileinput, inputToFile
            # fileinput.close()
            print ""

# If NO, then programm return to
        if inputCommand2.strip() == 'NO':
            print ""

# The conditions prints out the database
    if inputCommand.strip() == '2':
        fileinput = open(fileName, 'r')
        libraryInAlphabeticalOrder()
        print ""

# This condition break the loop
    if inputCommand.strip() == 'Q':
        break

# **********************END*********************************************************************************************
