file = open("ders_programi.txt",'r')
data = "".join(file.readlines())
data += "\t"+"Python Programlama-2: 4 Modül 2 Saat"
file.close()
file = open("ders_programi.txt",'w')
file.write(data)
print("sona eklendi")
file.close()