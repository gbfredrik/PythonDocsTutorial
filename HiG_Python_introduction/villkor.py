resultat = int(input("Ange ditt resultat: "))

print("Ditt betyg är: ", end = "")
if (resultat >= 48):
  print("A")
elif (resultat >= 40):
  print("B")
elif (resultat >= 32):
  print("C")
elif (resultat >= 24):
  print("D")
elif (resultat >= 16):
  print("E")
elif (resultat >= 0):
  print("F")
else:
  print("Ogiltigt resultat.")
