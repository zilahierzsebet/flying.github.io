# A vers szövege több caesar.txt file-ban van lekódolva a Caesar-rejtjel segítségével.
# A kódolás az angol ABC-t használja és eltolást értékét másik feladatok alapján kapjuk meg.
# A többi feladat eredménye mind szám, feladatok eredményeinek összege a kódolás eltolásának
# értéke. A feltörési feladatok megoldásához bármilyen programozási nyelvet használhatnak a
# résztvevők.

# eltolás = 8 + 4 + 4 -> 16


shift = 16
englishABCU = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
englishABCL = englishABCU.lower()

shiftABCU = englishABCU[shift:] + englishABCU[0:shift]
shiftABCL = shiftABCU.lower()

poem = open('poem.txt','w')

with open('caesar.txt') as file:
  for line in file:
    newLine = ""
    line = line.strip()
    for char in line:
      if englishABCU.find(char) > -1:
        newLine += englishABCU[shiftABCU.find(char)]
      elif englishABCL.find(char) > -1:
        newLine += englishABCL[shiftABCL.find(char)]
      else:
        newLine += char
    poem.write(newLine+'\n')

poem.close()
 