#umrechnen von meilen in kilometer und umgekehrt

km = 1
meilen = 0.621371

Frage = raw_input("Moechtest du Kilometer in Meilen oder Meilen in Kilometer?")
if Frage == "Kilometer":
    Wert = float(raw_input("wie viele Kilometer sind xy in Meilen?"))
    print Wert * meilen
elif Frage == "Meilen":
    Wert = float(raw_input("wie viele Meilen sind xy in Kilometer?"))
    print km / Wert * 100
else:
    print "Error"
