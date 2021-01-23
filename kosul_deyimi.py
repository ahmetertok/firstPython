age=int(input("Yaşı girin:"))
if age<100:
    if(age<50):
        print("Girilen yaş 0-50 arasında")
    else:
        print("Girilen yaş 50-100 arasında")
else:
    print("Lütfen 0-100 arası bir değer girin")