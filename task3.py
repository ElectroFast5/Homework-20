commonWords=["a","I","the","it","cat","sat","on","mat","astronomical"]
counts={}

def countWords(filePath):
    for word in commonWords:
        x=open("sample.txt")
        count=0
        for i in x.readlines():
            count+=i.count(word)
        counts.update({word:count})
    return counts

file=input("Enter file path: ")
print(countWords(file))