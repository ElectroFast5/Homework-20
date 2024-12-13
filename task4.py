source=open("binary.bin")
store=source.read()
dest=open("empty.exe","w")
dest.write(store)