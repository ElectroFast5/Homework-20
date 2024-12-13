def removeComments(path):
    x=open(path)
    count=[]
    for i in x.readlines():
        if i[0]!="#":
            count.append(i)
    y=open(path,"w")
    y.writelines(count)

removeComments(input("Enter file path: "))