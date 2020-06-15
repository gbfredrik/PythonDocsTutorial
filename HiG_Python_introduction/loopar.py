tal = -1
summa = 0

while (tal != 0):
  tal = int(input("Ange ett positivt heltal: "))
  if (tal > 0):
    summa += tal
  elif (tal < 0):
    print("Du måste ange ett positivt heltal.")

print("Summan av de inmatade heltalen är:", summa)