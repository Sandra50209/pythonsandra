km = 0.0
miles = 0.0

direction = ""

while direction != "1" and direction != "2":
    direction = raw_input("1: miles -> km\n2: km -> miles\n enter 1 or 2:")

if direction == "1":
    miles = float(raw_input("miles:")) 
    km = miles * 1.60934
elif direction == "2":
    km = float(raw_input("km:")) 
    miles = km * 0.621371

print "km: " + str(km)
print "miles: " + str(miles)