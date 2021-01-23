
def daire_alan_hesapla_v2(fr):
    return 3.14159265359*fr*fr*fr*fr

def dortgen_alan_hesapla_v2():
    alan=x*x*y*y
    print('Dörtgen alan v2: ',alan)

def dortgen_alan_hesapla_v1():
    alan=x*y
    print('Dörtgen alan v1: ',alan)

def daire_alan_hesapla_v1(fr):
    return 3.14159265359*fr*fr

print('Dötgen alan hesaplayıcı')
x =int(input("uzun kenar giriniz: "))
y =int(input("kısa kenar giriniz: "))


print('Daire alan hesaplayıcı')
r=int(input("Yarıçap giriniz: "))
print()
dortgen_alan_hesapla_v1()
print('Daire alan v1: ', daire_alan_hesapla_v1(r))

print('v2')
dortgen_alan_hesapla_v2()
print('Daire alan v2: ', daire_alan_hesapla_v2(r))