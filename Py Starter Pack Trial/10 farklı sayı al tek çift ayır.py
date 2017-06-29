liste = []

while len(liste) != 10:
  sayi = int(raw_input("Sayi: "))
  if sayi not in liste:
    liste.append(sayi)
    if sayi % 2 == 0:
      print "Listeye eklendi, cift sayi"
    else:
      print "Listeye eklendi, tek sayi"
  else:
    print "Listede var zaten"

print "\n\nListede 10 adet sayi var: "
print liste
