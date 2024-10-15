f = open("file1.txt", 'r')
f2 = open ("file2.txt", 'w')
text=f.read()
f2.write (text)

f.close()
f2.close()