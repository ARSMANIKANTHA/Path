file1=open("f11.txt","r")
file2=open("f22.txt","r")
f3=file1.read()
f4=file2.read()
file1.close()
file2.close()
file1=open("f11.txt","w")
file1.write(f4)
file1.close()
file2=open("f22.txt","w")
file2.write(f3)
file2.close()
file1=open("f11.txt","r")
file2=open("f22.txt","r")
print(file1.read())
print(file2.read())


