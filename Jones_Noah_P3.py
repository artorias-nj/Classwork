# This program handles transcript files

###############################################################################
# Functions:

def GatherSemData(x):
    # Prompt user for semester id, and course id and grade
    semesterId = input('Semester ID: ')
    semData.append(semesterId)

    while True:
        # Collect courseId and gradea
        courseItem = []
        courseId = input('Course Id: ')
        if courseId.lower() == 'none':
            break
        # You may want to check if the course Id is one from the catalog
        # before appending it to the list
        if CourseIdExist(courseId) == False:
            print('The course id does not exist!')
            continue
        courseItem.append(courseId)
        courseGrd = input('Course Grade: ')
        if isGradeValid(courseGrd) == False:
            print('The grade is invalid!')
            continue
        courseItem.append(courseGrd)
        semData.append(courseItem)

def VerifyFixContent():
   # Parse the file and fix errors
   loc_error = 0
   x=0
   z=0
   for i in fhandle: 
        if i.startswith("\n"):
            x=0
        print(i)
        if x>0:
            temp=i[0:5]
            print(temp)
            if CourseIdExist(temp)==False:
                print("File is Corrupted")
                quit()
        if i.startswith('Course'):
            x=x+1
   return loc_error

def WriteHdr():
   # Do actual job
   str = ''

def ComputeGPA(y):
    x=-1
    totalch=0
    totalp=0
    save=y[0]
    y.pop(0)
    for i in y:
        x=x+1
        temp1=GetCredHour(y[x][0])
        temp1=int(temp1)
        totalch=totalch+temp1
        temp2=GetGrdPoint(y[x][1])
        temp2=int(temp2)
        temp2=temp1*temp2
        totalp=totalp+temp2
    y.insert(0,save)
    return totalp/totalch

def GetCredHour(courseId):
    creditHr = -1
    for i in range(len(Catalog)):
        if courseId == Catalog[i][0]:
            creditHr = Catalog[i][2]
    return creditHr

def GetGrdPoint(letterGrd):
    gradePoint = -1
    for i in range(len(gradePoints)):
        if letterGrd == gradePoints[i][0]:
            gradePoint = gradePoints[i][1]
    return gradePoint

def GetFilename():
    # This function prompts the user for a filename and returns to the
    # main program
    fname = input('Provide transcript file name (enter none to quit): ')
    return fname

def VerifyFixData(fileHandle):
    # Parse file and fix data
    print('I\'m fixing it too')

def importCatalog():
    # Prompt the user to provide the catalog name
    catalogName = input('Provide the catalog name: ')
    # Open file
    catalogFHandle = open(catalogName,'r')

    catalog = []
    for line in catalogFHandle:
        catalogItem = re.split(r'\t+', line)
        catalog.append(catalogItem)
    return catalog

def CourseIdExist(str):
   valid = False
   for i in Catalog:
      if i[0].lower() == str.lower():
         valid = True
         break
   return valid

def isGradeValid(str):
   valid = False
   for i in gradePoints:
      if i[0].lower() == str.lower():
         valid = True
         break
   return valid


# Import regular expressions module to handle multiple tab characters delimiters
import re

# Create and initialize data structure to store letter grade and corresponding
# points
gradePoints = [['A',4],['B',3],['C',2],['D',1],['F',0]]

# Import the catalog: courseId courseTitle CreditHours
# The catalog is read from a text file (that is provided). The catalog is a
# list of lists:
# Catalog: [[courseId, title, CH], [courseId, title, CH], [courseId, title, CH],
# [courseId, title, CH], ...]
Catalog = list()
Catalog = importCatalog()

# Loop to process as many files as needed
while True:
    # Get the file name to process the transcript or to create a new file
    transc_fname = GetFilename()
    if (transc_fname =='none'):
        # The user is giving the signal to quit
        print('Exiting... Goodbye!')
        quit()

    # Check if the file exists
    try:
        # Attempt to create a new file (assuming there is no file with this
        # name that exists already)
        fhandle = open(transc_fname, 'x')
        # Write the header (student name, id, dob, etc.)
        WriteHdr()
        studentname=input("Please enter full name: ")
        dOb=input("Please enter date of birth: ")
        fhandle=open(transc_fname,"w")
        fhandle.write(studentname)
        fhandle.write("Birth date: "+dOb)
    except:
        # Open and read the file
        fhandle = open(transc_fname, 'r')
        # File read; verify data and try to fix if possible
        # Verify and fix the errors if any
        error = 0
        error = VerifyFixContent() # need to implement this function

        if error > 0:
            # Write the file with whatever was fixed
            WriteFile() # need to implement this function

    # Semester data can be stored in a list as follows (a list of items and
    # nested lists
    # ['Fall 2022', ['CS100', 'A'], ['CS101', 'B'], ['CCC101', 'A']]

    # Get data for the new semester and compute what needs to be computed to be
    # written to the transcript file
    semData = list()
    GatherSemData(semData)
    gpa = ComputeGPA(semData)
    # Write data to the transcript file
    fhandle=open(transc_fname,"w")
    x=0
    for i in semData:
        if(x==0):
            temp=str(semData[x])
            fhandle.write("ID: "+temp)
            fhandle.write("\n")
        if(x>0):
            z=0
            for j in semData[x]:
                temp=str(semData[x][z])
                fhandle.write(temp+"    ")
                z=z+1
            fhandle.write("\n")
        x=x+1
    fhandle.write("GPA is "+str(gpa))



