# Projekt: Alternativ 1

def compute(lhs, op, rhs):
  if (op == '+'):
    res = lhs + rhs
  elif (op == '-'):
    res = lhs - rhs
  elif (op == '*'):
    res = lhs * rhs
  elif (op == '/'):
    res = lhs / rhs
  else:
    print("Felaktig operator!\n")
    return

  print(f"{lhs} {op} {rhs} = {res}\n")

def main():
  while (1):
    text = input("Vad vill du räkna ut: ")
    ins = text.split()
    compute(float(ins[0]), ins[1], float(ins[2]))

if __name__ == "__main__":
    main()

## Obs: Finare lösning av compute()-funktionen men kanske utanför kursens ramar.
# import operator

# ops = {
#   '+': operator.add,
#   '-': operator.sub,
#   '*': operator.mul,
#   '/': operator.truediv
# }

# def compute(lhs, op, rhs):
#   if (op not in ops):
#     print("Felaktig operator!\n")
#   else:
#     print(f"{lhs} {op} {rhs} = {ops.get(op)(lhs, rhs)}\n")
