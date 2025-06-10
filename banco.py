import datetime
#deposito, saque, extrato

saldo = 0
quantidade_saques = 0
historico = []

def deposito(saldo, valor_entrada):
  if valor_entrada <= 0:
    print("Valor incorreto")
  else:
    saldo += valor_entrada
    data_hora_atual = datetime.datetime.now()
    historico.append(["+ ",valor_entrada,data_hora_atual.strftime("%d/%m/%Y")])
    print(f"Depositado, {valor_entrada}\nSaldo Atual, {saldo}")
    return saldo  

def saque(saldo, valor_entrada):
  global quantidade_saques
  print(f"Saldo atual, {saldo}")
  if valor_entrada <= 0:
    print("Valor incorreto")
    return saldo 
  elif saldo < valor_entrada:
    print("Saldo insuficiente")
    return saldo
  elif valor_entrada > 500:
    print("Valor de saque maior que o permitido")
    return saldo
  elif quantidade_saques >= 3:
    print("Quantidade de saques excedida")
    return saldo
  else:
    quantidade_saques += 1
    saldo -= valor_entrada
    data_hora_atual = datetime.datetime.now()
    historico.append(["- ",valor_entrada,data_hora_atual.strftime("%d/%m/%Y")])
    print(f"Saque, {valor_entrada}\nSaldo Atual, {saldo}")
    
    return saldo   

def extrato(historico, saldo):
    print("=" * 35)
    print("|{:^33}|".format("EXTRATO BANCÁRIO"))
    print("=" * 35)
    print("| {:^10} | {:^18} |".format("Data", "Transação"))
    print("-" * 35)

    if not historico:
        print("| {:^31} |".format("Não foram reaçizadas movimentações"))
        print("-" * 35)
    else:
        for item in historico:
            tipo = item[0]
            valor = f"R$ {item[1]:.2f}"
            data = item[2]
            print("| {:10} | {:>3} {:>12} |".format(data, tipo, valor))

    print("-" * 35)
    print("| {:<23} {:>9} |".format("Saldo Atual:", f"R$ {saldo:.2f}"))
    print("=" * 35)


while True: 
  valor_entrada = int(input("\n\nQual transação deseja fazer?\n 1 = Deposito\n 2 = Saque\n 3 = Extrato\n 0 = Sair\n\n"))
  if valor_entrada == 1:
    valor = float(input("Valor do deposito: "))
    saldo = deposito(saldo, valor)
  elif valor_entrada == 2:
    valor = float(input("Valor do saque: "))
    saldo = saque(saldo,valor)
  elif valor_entrada == 3:
    extrato(historico, saldo)
  elif valor_entrada == 0:
    break
  else:
    print("Valor incorreto, por favor digite novamente")


  
