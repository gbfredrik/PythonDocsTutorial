import math

num = int(input("Ange tabell: "))
print("--------------------")
print(f"{num}:ans tabell")
print("--------------------")

for i in range(11):
  print(f"{i:2} * {num} = {i * num:{3 + int(math.log10(num))}}")
  # Nu är visserligen log10 odefinierat för noll som input, men vi kanske kan anta att det är ett trivialt gränsfall eftersom inte annat nämns i uppgiften. 