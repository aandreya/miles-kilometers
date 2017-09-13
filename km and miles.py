# 1 milja = 1,6093 kilometra
# 1 km = 0,62 milje

milje = 0;
km = 0;
pretvornik = 0;
i = 0;

while True:
    try:
        pretvornik = int(raw_input("Ali zelis opraviti pretvorbo 1 (millje v kilometre) ali pretvorbo 2 (kilometre v milje)?:     "))

        if pretvornik == 1:
            print " "
            milje = float(raw_input("vnesi milje: "))
            km = milje * 1.6093
            print str(milje) + " milj = " + str(km) + " kilometrov"
            print " "
        elif pretvornik == 2:
            print " "
            km = float(raw_input("vnesi kilometre: "))
            milje = km / 1.6093
            print str(km) + " kilometrov = " + str(milje) + " milj"
            print " "
    except ValueError:
        print " "
        print "Neobstojec izbor"
        print " "