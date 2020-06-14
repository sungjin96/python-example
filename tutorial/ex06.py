try:
    f = open('simple.txt', 'R')
    f.write("Test write to simple text!")

except:
    print("ERROR: COULD NOT FIND FILE OR READ DATA!")

else:
    print("SUCCESS!")
    f.close()
