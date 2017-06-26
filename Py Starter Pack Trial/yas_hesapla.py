#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Ana görevi doğum yılı sorup yaş hesaplamak olan bir program yazın. Yazdığınız program kullanıcıya ismiyle hitap edip, ona yaşını söyleyebilmeli.

question = "Adın ne ? : "

question2 = "Doğum yılın ne ? : "

isim = raw_input(question)

hesapla = int(raw_input(question2))

print "Merhaba %s , Yaşın = %s" %(isim, 2017 - hesapla)
