file="./data/fox.txt"
fileobj=open(file)
text=fileobj.read()
fileobj.close()
print(text)
