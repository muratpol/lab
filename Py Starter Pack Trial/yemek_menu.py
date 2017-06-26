#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Yemek menüsü ; ing & tr mixledim. laf etme krşm.
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division

secenek1 = "(1) Monday"
secenek2 = "(2) Tuesday"
secenek3 = "(3) Wednesday"
secenek4 = "(4) Thursday"
secenek5 = "(5) Friday"

print secenek1
print secenek2
print secenek3
print secenek4

gun = raw_input(" What's today ? : ")
learname = raw_input(" Wad's your name my kustomır ? : ")

if gun == "1":
     corba1 = raw_input("What's your çorba çeşit ? : ")
     mainyemek1 = raw_input("What's your ana yemek ? : ")
     salata1 = raw_input("What's your salata ? : ")
     drink1 = raw_input("What's your içecek ? : ")

     print "\n\n\nMerhaba hoşgeldin %s. Seçimleriniz en kısa sürede hazırlanacak.\nGün: %s \nÇorba: %s \nAnayemek : %s \nSalata: %s \nİçecek: %s" %(learname, "Pazartesi", corba1, mainyemek1, salata1, drink1)

if gun == "2":
     corba2 = raw_input("What's your çorba çeşit ? : ")
     mainyemek2 = raw_input("What's your ana yemek ? : ")
     salata2 = raw_input("What's your salata ? : ")
     drink2 = raw_input("What's your içecek ? : ")

     print "\n\n\nMerhaba hoşgeldin %s. Seçimleriniz en kısa sürede hazırlanacak.\nGün: %s \nÇorba: %s \nAnayemek : %s \nSalata: %s \nİçecek: %s" %(learname, "Salı", corba2, mainyemek2, salata2, drink2)

if gun == "3":
     corba3 = raw_input("What's your çorba çeşit ? : ")
     mainyemek3 = raw_input("What's your ana yemek ? : ")
     salata3 = raw_input("What's your salata ? : ")
     drink3 = raw_input("What's your içecek ? : ")

     print "\n\n\nMerhaba hoşgeldin %s. Seçimleriniz en kısa sürede hazırlanacak.\nGün: %s \nÇorba: %s \nAnayemek : %s \nSalata: %s \nİçecek: %s" %(learname, "Çarşamba", corba3, mainyemek3, salata3, drink3)

if gun == "4":
     corba4 = raw_input("What's your çorba çeşit ? : ")
     mainyemek4 = raw_input("What's your ana yemek ? : ")
     salata4 = raw_input("What's your salata ? : ")
     drink4 = raw_input("What's your içecek ? : ")

     print "\n\n\nMerhaba hoşgeldin %s. Seçimleriniz en kısa sürede hazırlanacak.\nGün: %s \nÇorba: %s \nAnayemek : %s \nSalata: %s \nİçecek: %s" %(learname, "Perşembe", corba4, mainyemek4, salata4, drink4)

if gun == "5":
     corba5 = raw_input("What's your çorba çeşit ? : ")
     mainyemek5 = raw_input("What's your ana yemek ? : ")
     salata5 = raw_input("What's your salata ? : ")
     drink5 = raw_input("What's your içecek ? : ")

     print "\n\n\nMerhaba hoşgeldin %s. Seçimleriniz en kısa sürede hazırlanacak.\nGün: %s \nÇorba: %s \nAnayemek : %s \nSalata: %s \nİçecek: %s" %(learname, "Cuma", corba4, mainyemek4, salata4, drink4)

else:
	print "Bilinmeyen yahut tatil olan gün'ü seçtiniz"
