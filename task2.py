def countWords(filePath,word):
    x=open("sample.txt")
    count=0
    for i in x.readlines():
        count+=i.count(word)
    return count

file=input("Enter file path: ")
string=input("Enter word to count: ")
print(countWords(file,string))