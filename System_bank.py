print("Banco Okuizumi v1")


menu ="""

    ========== Okuizumi Bank ===========
    
    [d] - Depositar
    [s] - Sacar
    [e] - Extrato
        
    [q] - Sair

    =====================================
=>"""

saldo = 0
limite = 1500
extrato = ""

numero_saques = 0
LIMITE_SAQUES = 10

while True:

    opcao = input(menu)

    #Saldo
    if opcao == "d":
        valor = float(input("Deseja Despositar quanto na sua conta?? R$"))
        
        if valor > 0: 
            saldo += valor
            extrato += f"Depósito: R$ {valor: .2f}\n" #Exibir no extrato
        else:
            print("Operação falhou! O valor informado é inválido.")

    #Saque
    elif opcao == "s":
        valor = float(input("Desaja sacar quanto? R$"))
        
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo: 
            print("Operação falhou! Você não tem saldo o suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0: 
            saldo -= valor
            extrato += f"Saque: R$ {valor: .2f} \n" #Exibir no Extrato
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido")

    #Extrato
    elif opcao == "e":
        print("\n========== EXTRATO ==========")
        print("Não foram realizadas movimentações na conta." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo: .2f}")
        print("=============================")


    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")


