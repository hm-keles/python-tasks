# 1'den 10000 bine kadar Amicable (Dostane) sayıları yazınız.

def division(a) :
    b = 0
    for i in range(1,a) :
        if a % i == 0 :
            b += i
    return b
liste = []
x = 0
while x < 10000 :
    if division(division(x)) == x and division(x) != x :
        liste.append(x)
    x += 1
print(liste)