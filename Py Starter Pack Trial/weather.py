# -*- coding: cp1254 -*-
soru = raw_input("Şehrinizin adını tamamı küçük \
harf olacak şekilde yazınız: ")

cevap = {"istanbul":"gök gürültülü ve sağanak yağışlı",
"ankara":"açık ve güneşli", "izmir":"bulutlu"}

print cevap.get(soru,"Bu şehre ilişkin havadurumu \
bilgisi bulunmamaktadır.")
