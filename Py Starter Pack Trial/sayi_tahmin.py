#!/usr/bin/env python
# -*- coding: utf-8 -*-

sayi = 10
while True:
    sor = int(raw_input("Sayi: "))
    if sayi > sor:
         print "up up up!"
    elif sayi < sor:
        print "down!"
    else:
        print "doğru cevap!"
