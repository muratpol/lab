# -*- coding: cp1254 -*-
while True:
        s = raw_input("Bir sayı girin: ")
        if s == "iptal":
              break
        if len(s) <= 3:
              print "En fazla üç haneli bir sayı girin."
              continue
