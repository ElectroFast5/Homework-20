def combineFiles(file1,file2):
    a=open(file1).read()
    b=open(file2).read()
    newFile=open("NewFile.txt","w")
    newFile.write(a+"\n\n"+b)

combineFiles(input("Enter first file to merge: "),input("Enter second file to merge: "))