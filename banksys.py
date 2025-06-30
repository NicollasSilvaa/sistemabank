from datetime import datetime

menu = """

        SELECIONE A OPÇÃO DESEJADA

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opçao = input(menu)

    if opçao == "d":
        valor = float(input("Informe o valor do depósito que deseja realizar: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] Depósito: R$ {valor:.2f}\n"
        else:
            print("Não foi possível realizar o depósito, valor informado é inválido.")

    elif opçao == "s":
        valor = float(input("Informe o valor que deseja sacar: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Você não possui saldo suficiente!")

        elif excedeu_limite:
            print("Você excedeu o valor limite de saques!")

        elif excedeu_saques:
            print("Você excedeu o número de saques diários!")

        elif valor > 0:
            saldo -= valor
            extrato += f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Não foi possível realizar o saque, valor informado é inválido.")

    elif opçao == "e":
        print("\n===================== EXTRATO =====================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo atual da conta: R$ {saldo:.2f}")
        print("=====================================================")

    elif opçao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
