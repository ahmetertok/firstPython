file = open("ders_programi.txt",'r')
data="".join(file.readlines())
file.close()
data+="Python Programlama: 2 Ders 3,5 Saat "
file = open("ders_programi.txt",'a')
file.write(data)
file.close()
