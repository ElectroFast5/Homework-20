def writeInFile(file,text):
    open(file,'w').write(text)

writeInFile(input("Enter file name: "),input("Enter text: "))