
while True:
  x = float(input("Zadej první číslo: ")) 
  y = float(input("Zadej druhé číslo: "))
  z = input("Zadej početní operaci [+,-,*,/] pro mocninu a odmocninu zadejte **,//: ")

  plus = "+"
  minus = "-"
  deleno = "/"
  krat = "*"
  Mocnina = "**"
  odmocnina = "//"
  
  if z == plus:
    print(x+y)
  elif z == minus:
    print(x-y)
  elif z == krat:
    print(x*y)
  elif y == 0 and z == deleno:
   print("Nulou nelze dělit")
  elif z == deleno:
    print(x/y)
  elif z == Mocnina:
    print(x**y)
  elif z == odmocnina:
    print(x**(1/y))
  elif z == "konec":
    print("Ukončuju kalkulačku..")
    break
  else:
    print("Neplatná operace")