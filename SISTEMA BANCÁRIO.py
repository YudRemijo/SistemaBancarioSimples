saldo = 0
depositos = []
saques = []

while True:
    print("---- Menu ----")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Extrato")
    print("4. Sair")

    opcao = input("Número da opção: ")

    if opcao == "1":
        valor = float(input("Valor a ser depositado: "))
        if valor > 0:
            depositos.append(valor)
            saldo += valor
            print('************************************************')
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
            print('************************************************')
        else:
            print('************************************************')
            print("O valor do depósito deve ser positivo.")
            print('************************************************')
    elif opcao == "2":
        valor = float(input("Valor a ser sacado: "))
        if saldo >= valor and valor <= 500 and len(saques) < 3:
            saques.append(valor)
            saldo -= valor
            print('************************************************')
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            print('************************************************')
        elif saldo < valor:
            print("Saldo insuficiente para realizar o saque. Faça um novo depósito.")
        elif valor > 500:
            print("O valor do saque não pode ultrapassar o limite de R$ 500,00.")
        else:
            print("Limite diário de 3 saques atingido.")
    elif opcao == "3":
        if not depositos and not saques:
            print("Não foram realizadas movimentações.")
        else:
            print("Extrato:")
            for deposito in depositos:
                print(f"Depósito: R$ {deposito:.2f}")
            for saque in saques:
                print(f"Saque: R$ {saque:.2f}")
            print('************************************************')
            print(f"Saldo atual: R$ {saldo:.2f}")
            print(('************************************************'))
    elif opcao == "4":
        print('************************************************')
        print("Finalizando o programa...")
        print('************************************************')
        break
    else:
        print("Opção inválida. Tente uma das opções sugeridas no MENU.")