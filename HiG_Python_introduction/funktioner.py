from random import randint

# Funktion som slumpar fram ett antal kast till en lista
def slumpaTärningskastTillLista(antalKast, lista):
    for i in range(antalKast):
        tärningskast = randint(1,6)
        lista.append(tärningskast)

# Funktion som beräknar medelvärdet på tal i en lista
def beräknaMedelvärde(lista):
    summa = 0
    for element in lista:
        summa = summa + element
    medelvärde = summa / len(lista)
    return medelvärde


# Fråga användaren om indata
antalKast = int(input('Hur många tärningskast vill du göra? '))

# Skapa en tom lista
lista = []

# Anropa funktionen som slumpar fram tärningskast till en lista
slumpaTärningskastTillLista(antalKast, lista)

# Anropa funktionen som beräknar medelvärdet för elementen i en lista
medelVärde = beräknaMedelvärde(lista)
# Skriv ut medelvärdet
print('Medelvärdet av tärningskasten är:', medelVärde)

# Skriv ut en frekvenstabell
for i in range(1, 7):
    antal = lista.count(i)
    print('Antal ', i, ':or = ', antal, sep='')  
