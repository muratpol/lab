# userdan inputlanan datayi listede var mi yok mu diye karsilastir yoksa ekle varsa worning!
list = []
while True:
    obj = raw_input("Meyve ismi: ")
    if obj not in list:
        print "listede yok ekleniyor"
        list.append(obj)
    else:
        print obj, " bu listede var!"
