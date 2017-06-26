#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Türk Lirası’nı günlük kura göre Dolar, Euro ve Sterlin’e çeviren bir program yazın. Program kullanıcıdan TL miktar alıp bu miktarı kullanıcıya Dolar, Euro ve Sterlin olarak geri bildirebilmeli.

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division

secenek1 = "(1) dolar"
secenek2 = "(2) euro"
secenek3 = "(3) sterlin"
secenek4 = "(4) riyal"

print secenek1
print secenek2
print secenek3
print secenek4

soru = raw_input("Yapılacak işlemin numarasını girin: ")

if soru == "1":
     kur1 = input("Kaç $'ın var qnq ? : ")
     print "çevrildi ; hesaplarıma göreee ; %s doların %s tl ediyor." %(kur1, kur1 * 3.5)

if soru == "2":
     kur2 = input("Kaç eyro'n var qnq ? : ")
     print "Hesaplarıma göreee ; %s eyro'n %s tl etmekte " %(kur2, kur2 * 4)
if soru == "3":
     print "şu an bu deaktif qnq git kendine dolar al"
if soru == "4":
	print "şu an bu deaktif qnq git kendine dolar al"
else:
  print "Böyle bi tür görmedik"
