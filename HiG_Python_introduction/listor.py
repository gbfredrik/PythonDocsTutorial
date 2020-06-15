text = input("Skriv in tal: ")
lst = text.split()

for i in range(0, len(lst)):
  lst[i] = int(lst[i])

print(list(reversed(lst)))

print(sorted(lst))
