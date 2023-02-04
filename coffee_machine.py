def coffee_machine():
  water = int(input("Write how many ml of water the coffee machine has: "))
  milk = int(input("Write how many ml of milk the coffee machine has: "))
  coffee = int(input("Write how many g of coffee beans the coffee machine has: "))

  cups = int(input("Write how many cups of coffee you will need: "))

  cup = min(water/200,milk/50,coffee/15)
  more = cup-cups
  if int(cup)==cups:
    print('Yes,I can make that amount of coffee')

  elif int(cup)>cups:
    print(f'Yes,I can make that amount of coffee(and more {int(more)} than that')

  else:
    print(f'No,I can make only {int(cup)} cups of coffee')

  return

coffee_machine()