import hashlib 

file = open("src/test.txt","rb")
f2=file.read()
md5 = hashlib.md5(f2)
print(md5.hexdigest())