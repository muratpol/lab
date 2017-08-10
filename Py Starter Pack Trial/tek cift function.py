# -*- coding: utf-8 -*-
print "cikmak icin 'q' basiniz.\n"
while True:
    def tek():
        print "Girdiğiniz sayı bir tek sayıdır!\n"
    def cift():
        print "Girdiğiniz sayı bir çift sayıdır!\n"
    sayi = raw_input("Lütfen bir sayı giriniz: ")
    if sayi == "q":
        exit()
    elif int(sayi) % 2 == 0:
        cift()
    else:
        tek()
