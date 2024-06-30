import random
x = random.randrange(1, 7) #losuje liczby od 1 do 6
y = 0
print ("Wyrzuć wynik 18 aby wygrać: ")
print ("Wynik rzutu kostką to: ", x)
y += x # jest to skrót działania y = y+x
x = random.randrange(1, 7) #losuje liczby od 1 do 6
print ("Wynik rzutu kostką to: ", x)
y += x# jest to skrót działania y = y+x
x = random.randrange(1, 7) #losuje liczby od 1 do 6
print ("Wynik rzutu kostką to: ", x)
y += x# jest to skrót działania y = y+x
   
if y >= 18:
    print ("Wygrywasz! Wynik to: ", y)
else:
    print ("Spróbuj jeszcze raz! Twój wynik to: ", y)