f = open('file.txt', 'a', errors='ignore')

f.write('test\r\n')

f.close()

fi = open('file.txt', 'r', errors='ignore')

print(fi.read())

fi.close()
